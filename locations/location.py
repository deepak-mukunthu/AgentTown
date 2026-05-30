from typing import List, Optional
from pydantic import BaseModel, Field


class Location(BaseModel):
    """Represents a location in the town"""
    name: str
    description: str
    capacity: int = 10
    agents: List[str] = Field(default_factory=list)

    def can_accept_agent(self) -> bool:
        """Check if location can accept another agent"""
        return len(self.agents) < self.capacity

    def add_agent(self, agent_name: str) -> bool:
        """Add an agent to this location"""
        if self.can_accept_agent() and agent_name not in self.agents:
            self.agents.append(agent_name)
            return True
        return False

    def remove_agent(self, agent_name: str) -> bool:
        """Remove an agent from this location"""
        if agent_name in self.agents:
            self.agents.remove(agent_name)
            return True
        return False

    def get_agent_count(self) -> int:
        """Get number of agents at this location"""
        return len(self.agents)

    def is_empty(self) -> bool:
        """Check if location has no agents"""
        return len(self.agents) == 0

    def __str__(self) -> str:
        return f"{self.name} ({len(self.agents)}/{self.capacity})"
