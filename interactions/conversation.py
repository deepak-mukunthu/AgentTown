from typing import List, Dict, Any
from datetime import datetime
import random
import os
from anthropic import Anthropic

from agents.base_agent import Agent
from locations.location import Location


class ConversationManager:
    """Manages conversations between agents using Claude"""

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=api_key) if api_key else None

        # Fallback conversation templates if no API key
        self.conversation_templates = [
            {
                "opener": "Hey {other}, how's your day going?",
                "response": "Pretty good, {self}! Just enjoying the atmosphere here. How about you?"
            },
            {
                "opener": "Hi {other}! Have you been to the {location} before?",
                "response": "Yes, I love this place! It's one of my favorites. What brings you here?"
            },
            {
                "opener": "Good to see you, {other}!",
                "response": "You too, {self}! Beautiful day, isn't it?"
            }
        ]

    def generate_conversation(
        self,
        agent1: Agent,
        agent2: Agent,
        location: Location,
        current_time: datetime
    ) -> Dict[str, Any]:
        """Generate a conversation between two agents"""

        if self.client:
            return self._generate_with_claude(agent1, agent2, location, current_time)
        else:
            return self._generate_with_templates(agent1, agent2, location)

    def _generate_with_claude(
        self,
        agent1: Agent,
        agent2: Agent,
        location: Location,
        current_time: datetime
    ) -> Dict[str, Any]:
        """Generate conversation using Claude API"""

        # Get relevant memories for both agents
        context = f"conversation at {location.name}"
        agent1_memories = agent1.retrieve_relevant_memories(context, count=3)
        agent2_memories = agent2.retrieve_relevant_memories(context, count=3)

        # Build context string
        memory_context = ""
        if agent1_memories:
            memory_context += f"\n{agent1.name}'s recent memories:\n"
            for m in agent1_memories:
                memory_context += f"- {m.content}\n"

        if agent2_memories:
            memory_context += f"\n{agent2.name}'s recent memories:\n"
            for m in agent2_memories:
                memory_context += f"- {m.content}\n"

        prompt = f"""You are simulating a brief, natural conversation between two people in a virtual town.

Agent 1: {agent1.name}
Personality: {', '.join(agent1.personality_traits)}
Style: {agent1.conversation_style}

Agent 2: {agent2.name}
Personality: {', '.join(agent2.personality_traits)}
Style: {agent2.conversation_style}

Location: {location.name} - {location.description}
Time: {current_time.strftime('%H:%M')}
{memory_context}

Generate a brief, natural conversation (2-4 exchanges) between these two agents. Keep it casual and authentic to their personalities.

Format your response as a JSON object:
{{
  "exchanges": [
    {{"speaker": "AgentName", "message": "What they said"}},
    ...
  ]
}}
"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Parse response
            content = response.content[0].text

            # Simple JSON extraction
            import json
            if "```json" in content:
                json_str = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                json_str = content.split("```")[1].split("```")[0].strip()
            else:
                json_str = content.strip()

            conversation = json.loads(json_str)
            return conversation

        except Exception as e:
            print(f"Error generating conversation with Claude: {e}")
            return self._generate_with_templates(agent1, agent2, location)

    def _generate_with_templates(
        self,
        agent1: Agent,
        agent2: Agent,
        location: Location
    ) -> Dict[str, Any]:
        """Generate conversation using templates (fallback)"""

        template = random.choice(self.conversation_templates)

        opener = template["opener"].format(
            other=agent2.name,
            self=agent1.name,
            location=location.name
        )

        response = template["response"].format(
            other=agent1.name,
            self=agent2.name,
            location=location.name
        )

        return {
            "exchanges": [
                {"speaker": agent1.name, "message": opener},
                {"speaker": agent2.name, "message": response}
            ]
        }
