#!/usr/bin/env python3
"""
Agent Town - A multi-agent simulation
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from agents.agent_factory import AgentFactory
from locations.location import Location
from engine.simulation import SimulationEngine


def load_config(config_path: str) -> dict:
    """Load configuration from JSON file"""
    with open(config_path, 'r') as f:
        return json.load(f)


def setup_environment():
    """Setup environment variables"""
    load_dotenv()

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Warning: ANTHROPIC_API_KEY not found in environment")
        print("   Conversations will use simple templates instead of Claude API")
        print("   To use Claude API, create a .env file with your API key")
        print()


def create_locations(location_configs: list) -> list[Location]:
    """Create location objects from config"""
    locations = []
    for config in location_configs:
        location = Location(
            name=config["name"],
            description=config["description"],
            capacity=config.get("capacity", 10)
        )
        locations.append(location)
    return locations


def main():
    parser = argparse.ArgumentParser(description="Run the Agent Town simulation")
    parser.add_argument(
        "--config",
        default="config/default.json",
        help="Path to configuration file"
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=50,
        help="Number of simulation steps to run"
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=1.0,
        help="Simulation speed multiplier (higher = faster)"
    )

    args = parser.parse_args()

    console = Console()

    # Display welcome banner
    console.print(Panel.fit(
        "[bold cyan]🏘️  Agent Town Simulation[/bold cyan]\n"
        "A multi-agent world where AI agents interact and form communities",
        border_style="cyan"
    ))

    # Setup environment
    setup_environment()

    # Load configuration
    try:
        config = load_config(args.config)
    except FileNotFoundError:
        console.print(f"[red]Error: Config file not found: {args.config}[/red]")
        sys.exit(1)

    # Create locations
    locations = create_locations(config["locations"])
    location_names = [loc.name for loc in locations]

    # Create agents
    num_agents = config["simulation"]["max_agents"]
    console.print(f"\n[yellow]Creating {num_agents} agents...[/yellow]")
    agents = AgentFactory.create_agents(num_agents, location_names)

    for agent in agents:
        console.print(f"  • {agent.name} ({', '.join(agent.personality_traits)}) - {agent.conversation_style}")

    # Create simulation engine
    time_step = config["simulation"]["time_step_seconds"]
    simulation = SimulationEngine(
        agents=agents,
        locations=locations,
        time_step_seconds=time_step,
        console=console
    )

    # Display initial status
    console.print("\n[bold green]Starting simulation...[/bold green]\n")
    simulation.display_status()

    # Run simulation
    try:
        for step in range(args.steps):
            simulation.step()

            # Display status every 10 steps
            if (step + 1) % 10 == 0:
                console.print("\n" + "="*60)
                simulation.display_status()
                stats = simulation.get_statistics()
                console.print(f"\n[bold]Statistics:[/bold]")
                console.print(f"  Steps completed: {stats['step_count']}")
                console.print(f"  Simulation time: {stats['current_time']}")
                console.print(f"  Total memories: {stats['total_memories']}")

            # Add delay based on speed
            time.sleep(1.0 / args.speed)

    except KeyboardInterrupt:
        console.print("\n\n[yellow]Simulation interrupted by user[/yellow]")

    # Final statistics
    console.print("\n" + "="*60)
    console.print("[bold green]Simulation Complete![/bold green]\n")
    simulation.display_status()

    stats = simulation.get_statistics()
    console.print(f"\n[bold]Final Statistics:[/bold]")
    console.print(f"  Steps completed: {stats['step_count']}")
    console.print(f"  Simulation time: {stats['current_time']}")
    console.print(f"  Total memories: {stats['total_memories']}")
    console.print(f"  Average memories per agent: {stats['total_memories'] / len(agents):.1f}")


if __name__ == "__main__":
    main()
