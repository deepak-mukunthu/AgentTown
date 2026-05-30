import random
from typing import List
from .base_agent import Agent


class AgentFactory:
    """Factory for creating agents with diverse personalities"""

    FIRST_NAMES = [
        "Alice", "Bob", "Charlie", "Diana", "Emma", "Frank",
        "Grace", "Henry", "Iris", "Jack", "Kate", "Leo",
        "Maya", "Noah", "Olivia", "Paul", "Quinn", "Ruby"
    ]

    PERSONALITY_TRAITS = [
        "friendly", "curious", "thoughtful", "energetic",
        "creative", "analytical", "empathetic", "adventurous",
        "calm", "witty", "optimistic", "pragmatic"
    ]

    CONVERSATION_STYLES = [
        "casual", "formal", "enthusiastic", "philosophical",
        "humorous", "direct", "thoughtful", "inquisitive"
    ]

    ROLES = {
        "artist": {
            "traits": ["creative", "thoughtful", "empathetic"],
            "preferred_locations": ["Coffee Shop", "Park", "Community Center"],
            "style": "thoughtful"
        },
        "scholar": {
            "traits": ["analytical", "curious", "thoughtful"],
            "preferred_locations": ["Library", "Coffee Shop"],
            "style": "philosophical"
        },
        "explorer": {
            "traits": ["adventurous", "energetic", "curious"],
            "preferred_locations": ["Park", "Town Square"],
            "style": "enthusiastic"
        },
        "socialite": {
            "traits": ["friendly", "optimistic", "witty"],
            "preferred_locations": ["Town Square", "Coffee Shop", "Community Center"],
            "style": "casual"
        },
        "resident": {
            "traits": ["calm", "pragmatic", "friendly"],
            "preferred_locations": [],
            "style": "casual"
        },
        "villain": {
            "traits": ["aggressive", "volatile", "unpredictable"],
            "preferred_locations": ["Town Square", "Park"],
            "style": "direct"
        },
        "doctor": {
            "traits": ["empathetic", "calm", "analytical"],
            "preferred_locations": ["Library", "Community Center"],
            "style": "formal"
        }
    }

    @classmethod
    def create_agent(cls, name: Optional[str] = None, starting_location: str = "Town Square", role: Optional[str] = None) -> Agent:
        """Create a single agent with random personality"""
        if name is None:
            name = random.choice(cls.FIRST_NAMES)

        # Assign role if not provided
        if role is None:
            role = random.choice(list(cls.ROLES.keys()))

        role_config = cls.ROLES[role]

        # Use role-based traits, with some randomization
        base_traits = role_config["traits"]
        extra_traits = random.sample([t for t in cls.PERSONALITY_TRAITS if t not in base_traits],
                                     random.randint(0, 2))
        traits = base_traits + extra_traits

        conversation_style = role_config["style"]

        return Agent(
            name=name,
            personality_traits=traits,
            current_location=starting_location,
            conversation_style=conversation_style,
            role=role,
            preferred_locations=role_config["preferred_locations"]
        )

    @classmethod
    def create_agents(cls, count: int, starting_locations: List[str]) -> List[Agent]:
        """Create multiple agents with diverse personalities"""
        used_names = set()
        agents = []

        # Always create exactly 1 villain and 1 doctor
        villain_created = False
        doctor_created = False

        for i in range(count):
            # Ensure unique names
            available_names = [n for n in cls.FIRST_NAMES if n not in used_names]
            if not available_names:
                name = f"Agent_{i}"
            else:
                name = random.choice(available_names)

            used_names.add(name)

            # Randomly assign starting location
            location = random.choice(starting_locations)

            # Assign special roles first
            if not villain_created:
                role = "villain"
                villain_created = True
            elif not doctor_created:
                role = "doctor"
                doctor_created = True
            else:
                # Random role for remaining agents (excluding villain and doctor)
                role = random.choice(["artist", "scholar", "explorer", "socialite", "resident"])

            agent = cls.create_agent(name=name, starting_location=location, role=role)
            agents.append(agent)

        return agents
