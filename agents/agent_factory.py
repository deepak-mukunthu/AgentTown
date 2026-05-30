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

    @classmethod
    def create_agent(cls, name: Optional[str] = None, starting_location: str = "Town Square") -> Agent:
        """Create a single agent with random personality"""
        if name is None:
            name = random.choice(cls.FIRST_NAMES)

        # Select 2-4 personality traits
        num_traits = random.randint(2, 4)
        traits = random.sample(cls.PERSONALITY_TRAITS, num_traits)

        conversation_style = random.choice(cls.CONVERSATION_STYLES)

        return Agent(
            name=name,
            personality_traits=traits,
            current_location=starting_location,
            conversation_style=conversation_style
        )

    @classmethod
    def create_agents(cls, count: int, starting_locations: List[str]) -> List[Agent]:
        """Create multiple agents with diverse personalities"""
        used_names = set()
        agents = []

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

            agent = cls.create_agent(name=name, starting_location=location)
            agents.append(agent)

        return agents
