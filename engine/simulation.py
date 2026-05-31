from typing import List, Dict, Optional
from datetime import datetime, timedelta
import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agents.base_agent import Agent
from locations.location import Location
from interactions.conversation import ConversationManager


class SimulationEngine:
    """Core engine for running the agent town simulation"""

    def __init__(
        self,
        agents: List[Agent],
        locations: List[Location],
        time_step_seconds: int = 60,
        console: Optional[Console] = None
    ):
        self.agents = agents
        self.locations = {loc.name: loc for loc in locations}
        self.time_step_seconds = time_step_seconds
        self.current_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        self.step_count = 0
        self.console = console or Console()
        self.conversation_manager = ConversationManager()
        self.recent_events = []  # Track recent events (conversations, movements)
        self.max_events = 50  # Keep last 50 events

        # Place agents in their starting locations
        for agent in agents:
            if agent.current_location in self.locations:
                self.locations[agent.current_location].add_agent(agent.name)

    def step(self):
        """Execute one simulation step"""
        self.step_count += 1
        self.current_time += timedelta(seconds=self.time_step_seconds)

        self.console.print(f"\n[bold cyan]Step {self.step_count} - {self.current_time.strftime('%H:%M')}[/bold cyan]")

        # Shuffle agent order for fairness
        agent_order = list(self.agents)
        random.shuffle(agent_order)

        for agent in agent_order:
            self._agent_action(agent)

    def _agent_action(self, agent: Agent):
        """Determine and execute an action for an agent"""
        if agent.status == "dead":
            return  # Dead agents can't act

        current_location = self.locations[agent.current_location]

        # Special actions for villain
        if agent.role == "villain":
            self._villain_action(agent)
            return

        # Special actions for doctor
        if agent.role == "doctor":
            self._doctor_action(agent)
            return

        # Check if agent wants to move
        if agent.should_move(probability=0.15):
            self._move_agent(agent)
            return

        # Check if agent wants to interact
        if agent.should_interact(probability=0.4):
            other_agents = self._get_agents_at_location(agent.current_location)
            other_agents = [a for a in other_agents if a.name != agent.name and a.status == "alive"]

            if other_agents:
                self._initiate_interaction(agent, random.choice(other_agents))

    def _move_agent(self, agent: Agent):
        """Move an agent to a new location"""
        current_location = self.locations[agent.current_location]

        # Choose a new location (different from current)
        available_locations = [name for name in self.locations.keys() if name != agent.current_location]

        # Use agent's preferred location if available
        new_location_name = agent.get_preferred_next_location(available_locations)
        if not new_location_name:
            new_location_name = random.choice(available_locations)

        new_location = self.locations[new_location_name]

        # Check capacity
        if not new_location.can_accept_agent():
            return

        # Move the agent
        current_location.remove_agent(agent.name)
        new_location.add_agent(agent.name)
        agent.move_to(new_location_name)

        # Log event
        self._add_event({
            "type": "movement",
            "agent": agent.name,
            "from": current_location.name,
            "to": new_location_name,
            "time": self.current_time.strftime("%H:%M")
        })

        self.console.print(f"  🚶 [yellow]{agent.name}[/yellow] moved from {current_location.name} to [green]{new_location_name}[/green]")

    def _initiate_interaction(self, agent1: Agent, agent2: Agent):
        """Initiate a conversation between two agents"""
        location = self.locations[agent1.current_location]

        # Generate conversation
        conversation = self.conversation_manager.generate_conversation(
            agent1, agent2, location, self.current_time
        )

        # Log conversation event
        self._add_event({
            "type": "conversation",
            "location": location.name,
            "participants": [agent1.name, agent2.name],
            "exchanges": conversation["exchanges"],
            "time": self.current_time.strftime("%H:%M")
        })

        # Display conversation
        self._display_conversation(conversation, location.name)

        # Store memories for both agents
        for exchange in conversation["exchanges"]:
            speaker = agent1 if exchange["speaker"] == agent1.name else agent2
            listener = agent2 if exchange["speaker"] == agent1.name else agent1

            speaker.add_memory(
                f"I said to {listener.name}: {exchange['message']}",
                importance=0.6,
                location=location.name,
                related_agents=[listener.name]
            )

            listener.add_memory(
                f"{speaker.name} said to me: {exchange['message']}",
                importance=0.6,
                location=location.name,
                related_agents=[speaker.name]
            )

    def _display_conversation(self, conversation: Dict, location: str):
        """Display a conversation in formatted output"""
        self.console.print(f"\n  💬 [bold magenta]Conversation at {location}[/bold magenta]")

        for exchange in conversation["exchanges"]:
            speaker = exchange["speaker"]
            message = exchange["message"]
            self.console.print(f"    [cyan]{speaker}:[/cyan] \"{message}\"")

    def _villain_action(self, agent: Agent):
        """Villain-specific actions"""
        # Increase anger gradually
        agent.increase_anger(0.05)

        # Villain moves more when angry
        if agent.anger_level > 0.3 and agent.should_move(probability=0.3):
            self._move_agent(agent)
            return

        # Check if angry enough to attack
        if agent.is_angry() and self.step_count - agent.last_kill_step > 10:
            other_agents = self._get_agents_at_location(agent.current_location)
            # IMPORTANT: Villain cannot kill the doctor (game balance)
            potential_victims = [a for a in other_agents if a.name != agent.name and a.status == "alive" and a.role not in ["villain", "doctor"]]

            if potential_victims:
                victim = random.choice(potential_victims)
                self._villain_attack(agent, victim)
                return

        # Sometimes just have a threatening conversation
        if random.random() < 0.2:
            other_agents = self._get_agents_at_location(agent.current_location)
            other_agents = [a for a in other_agents if a.name != agent.name and a.status == "alive"]
            if other_agents:
                self._initiate_interaction(agent, random.choice(other_agents))

    def _villain_attack(self, villain: Agent, victim: Agent):
        """Villain attacks and kills a victim"""
        location = self.locations[villain.current_location]

        # Kill the victim
        victim.kill()
        villain.decrease_anger(0.5)
        villain.last_kill_step = self.step_count

        # Log the dramatic event
        self._add_event({
            "type": "attack",
            "attacker": villain.name,
            "victim": victim.name,
            "location": location.name,
            "time": self.current_time.strftime("%H:%M")
        })

        self.console.print(f"  ⚠️  [red bold]{villain.name} attacked {victim.name} at {location.name}! {victim.name} is dead![/red bold]")

        # Add memories
        villain.add_memory(
            f"I attacked {victim.name} in a fit of rage at {location.name}",
            importance=1.0,
            location=location.name,
            related_agents=[victim.name]
        )

        victim.add_memory(
            f"I was attacked by {villain.name} at {location.name}",
            importance=1.0,
            location=location.name,
            related_agents=[villain.name]
        )

    def _doctor_action(self, agent: Agent):
        """Doctor-specific actions"""
        # Doctor has immunity - if somehow killed, self-resurrect immediately
        if agent.status == "dead":
            agent.resurrect()
            self._add_event({
                "type": "self_resurrection",
                "doctor": agent.name,
                "location": agent.current_location,
                "time": self.current_time.strftime("%H:%M")
            })
            self.console.print(f"  ⚡ [cyan bold]{agent.name} (Doctor) used divine powers to self-resurrect![/cyan bold]")
            return

        # Check for dead agents at current location
        agents_here = self._get_agents_at_location(agent.current_location)
        dead_agents = [a for a in agents_here if a.status == "dead" and a.name != agent.name]

        if dead_agents:
            # Resurrect a dead agent
            patient = random.choice(dead_agents)
            self._doctor_resurrect(agent, patient)
            return

        # Move to find patients (check all locations for dead agents)
        for loc_name, location in self.locations.items():
            agents_at_loc = self._get_agents_at_location(loc_name)
            if any(a.status == "dead" for a in agents_at_loc):
                # Move towards location with dead agents
                if loc_name != agent.current_location and random.random() < 0.7:
                    available_locations = [name for name in self.locations.keys() if name != agent.current_location]
                    # Try to move towards the location with dead agents
                    if loc_name in available_locations:
                        self._move_agent_to(agent, loc_name)
                        return

        # If no dead agents, move around or interact normally
        if agent.should_move(probability=0.2):
            self._move_agent(agent)
        elif agent.should_interact(probability=0.4):
            other_agents = self._get_agents_at_location(agent.current_location)
            other_agents = [a for a in other_agents if a.name != agent.name and a.status == "alive"]
            if other_agents:
                self._initiate_interaction(agent, random.choice(other_agents))

    def _doctor_resurrect(self, doctor: Agent, patient: Agent):
        """Doctor resurrects a dead agent"""
        location = self.locations[doctor.current_location]

        # Resurrect the patient
        patient.resurrect()

        # Log the miraculous event
        self._add_event({
            "type": "resurrection",
            "doctor": doctor.name,
            "patient": patient.name,
            "location": location.name,
            "time": self.current_time.strftime("%H:%M")
        })

        self.console.print(f"  ✨ [green bold]{doctor.name} resurrected {patient.name} at {location.name}! {patient.name} is alive again![/green bold]")

        # Add memories
        doctor.add_memory(
            f"I miraculously brought {patient.name} back to life at {location.name}",
            importance=1.0,
            location=location.name,
            related_agents=[patient.name]
        )

        patient.add_memory(
            f"I was brought back to life by {doctor.name} at {location.name}",
            importance=1.0,
            location=location.name,
            related_agents=[doctor.name]
        )

    def _move_agent_to(self, agent: Agent, target_location: str):
        """Move agent to a specific location"""
        current_location = self.locations[agent.current_location]
        new_location = self.locations[target_location]

        # Check capacity
        if not new_location.can_accept_agent():
            return

        # Move the agent
        current_location.remove_agent(agent.name)
        new_location.add_agent(agent.name)
        agent.move_to(target_location)

        # Log event
        self._add_event({
            "type": "movement",
            "agent": agent.name,
            "from": current_location.name,
            "to": target_location,
            "time": self.current_time.strftime("%H:%M")
        })

        self.console.print(f"  🚶 [yellow]{agent.name}[/yellow] moved from {current_location.name} to [green]{target_location}[/green]")

    def _get_agents_at_location(self, location_name: str) -> List[Agent]:
        """Get all agents at a specific location"""
        agent_names = self.locations[location_name].agents
        return [agent for agent in self.agents if agent.name in agent_names]

    def display_status(self):
        """Display current status of the simulation"""
        table = Table(title="Agent Town Status")
        table.add_column("Location", style="cyan")
        table.add_column("Agents", style="yellow")
        table.add_column("Count", style="green")

        for location_name, location in self.locations.items():
            agents_str = ", ".join(location.agents) if location.agents else "Empty"
            table.add_row(location_name, agents_str, str(len(location.agents)))

        self.console.print(table)

    def _add_event(self, event: Dict):
        """Add an event to the recent events list"""
        self.recent_events.append(event)
        # Keep only the most recent events
        if len(self.recent_events) > self.max_events:
            self.recent_events = self.recent_events[-self.max_events:]

    def get_statistics(self) -> Dict:
        """Get simulation statistics"""
        total_memories = sum(len(agent.memories) for agent in self.agents)

        location_counts = {
            name: len(loc.agents)
            for name, loc in self.locations.items()
        }

        return {
            "step_count": self.step_count,
            "current_time": self.current_time.strftime("%H:%M"),
            "total_agents": len(self.agents),
            "total_memories": total_memories,
            "location_distribution": location_counts
        }
