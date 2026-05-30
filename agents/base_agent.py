from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
import random


class Memory(BaseModel):
    """Represents a single memory for an agent"""
    timestamp: datetime
    content: str
    importance: float = Field(ge=0.0, le=1.0)
    related_agents: List[str] = Field(default_factory=list)
    location: Optional[str] = None


class Agent(BaseModel):
    """Base agent class with personality and memory"""
    name: str
    personality_traits: List[str]
    current_location: str
    memories: List[Memory] = Field(default_factory=list)
    conversation_style: str = "friendly"

    class Config:
        arbitrary_types_allowed = True

    def add_memory(self, content: str, importance: float, location: Optional[str] = None, related_agents: Optional[List[str]] = None):
        """Add a new memory to the agent's memory store"""
        memory = Memory(
            timestamp=datetime.now(),
            content=content,
            importance=importance,
            related_agents=related_agents or [],
            location=location or self.current_location
        )
        self.memories.append(memory)

        # Keep only most recent/important memories
        if len(self.memories) > 100:
            self.memories = sorted(self.memories, key=lambda m: m.importance, reverse=True)[:100]

    def retrieve_relevant_memories(self, context: str, count: int = 5) -> List[Memory]:
        """Retrieve memories relevant to the current context"""
        # Simple relevance: check if context words appear in memory
        context_words = set(context.lower().split())

        scored_memories = []
        for memory in self.memories:
            memory_words = set(memory.content.lower().split())
            overlap = len(context_words & memory_words)
            score = overlap * memory.importance
            scored_memories.append((score, memory))

        scored_memories.sort(reverse=True, key=lambda x: x[0])
        return [m for _, m in scored_memories[:count]]

    def move_to(self, location: str):
        """Move agent to a new location"""
        self.current_location = location
        self.add_memory(f"Moved to {location}", importance=0.3, location=location)

    def should_interact(self, probability: float = 0.3) -> bool:
        """Determine if agent should initiate interaction"""
        return random.random() < probability

    def should_move(self, probability: float = 0.2) -> bool:
        """Determine if agent should move to a new location"""
        return random.random() < probability

    def get_personality_description(self) -> str:
        """Get a description of the agent's personality"""
        return f"{self.name} is {', '.join(self.personality_traits)}"

    def __str__(self) -> str:
        return f"{self.name} at {self.current_location}"
