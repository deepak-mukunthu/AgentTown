# Agent Town 🏘️

A multi-agent simulation where AI agents live, interact, and form a virtual community. Agents have personalities, memories, and can engage in dynamic conversations with each other.

## Features

- **Autonomous Agents**: Each agent has unique personality traits and behaviors
- **Dynamic Interactions**: Agents can initiate conversations and respond to each other
- **Memory System**: Agents remember past interactions and use them to inform future behavior
- **Spatial Environment**: Agents move around a virtual town with different locations
- **Emergent Behaviors**: Complex social dynamics emerge from simple agent rules

## Architecture

- `agents/` - Agent definitions and personality configurations
- `engine/` - Core simulation engine and orchestration
- `memory/` - Agent memory storage and retrieval systems
- `locations/` - Town geography and location definitions
- `interactions/` - Conversation and interaction logic
- `main.py` - Entry point for running the simulation

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the simulation
python main.py

# Run with custom configuration
python main.py --config config/custom.json
```

## Configuration

Edit `config/default.json` to customize:
- Number of agents
- Simulation speed
- Agent personality distributions
- Available locations
- Interaction rules

## Example Output

```
[09:15] Alice enters the Coffee Shop
[09:16] Alice: "Good morning! Beautiful day, isn't it?"
[09:17] Bob enters the Coffee Shop
[09:17] Bob: "Morning Alice! Yes, perfect weather for a walk later."
[09:18] Alice remembers previous conversation about hiking
[09:18] Alice: "Speaking of walks, did you ever check out that trail I mentioned?"
```

## License

MIT License - Feel free to use and modify for your own projects!
