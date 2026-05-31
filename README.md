# Agent Town 🏘️

A multi-agent simulation where AI agents live, interact, and form a virtual community. Agents have personalities, memories, and can engage in dynamic conversations with each other.

**🎭 NEW:** Features a malicious villain (😈) who gets angry and kills others, and a mysterious doctor (⚕️) who resurrects the dead!

## ⚡ Quick Start

```bash
./demo.sh
```

Then open **http://localhost:3000** and click **▶️ Start**!

See [QUICKSTART.md](QUICKSTART.md) for detailed setup.

## Features

### Core Simulation
- **Autonomous Agents**: Each agent has unique personality traits and behaviors
- **Dynamic Interactions**: Agents can initiate conversations and respond to each other
- **Memory System**: Agents remember past interactions and use them to inform future behavior
- **Spatial Environment**: Agents move around a virtual town with different locations
- **Emergent Behaviors**: Complex social dynamics emerge from simple agent rules

### 7 Unique Roles
- 😈 **Villain**: Gets angry and attacks others when rage exceeds 60%
- ⚕️ **Doctor**: Resurrects dead agents and searches for casualties
- 🎨 **Artist**: Creative personality, prefers inspiring locations
- 📚 **Scholar**: Analytical, loves libraries and discussions
- 🧭 **Explorer**: Adventurous, moves 2x more frequently
- 🎭 **Socialite**: Friendly, interacts 2x more frequently
- 🏠 **Resident**: Balanced behavior with no special traits

### Life & Death Drama
- **Anger System**: Villain's rage builds gradually (visual anger bar)
- **Attack Mechanics**: Villain kills when anger reaches threshold
- **Death Status**: Agents can die and become inactive (💀)
- **Resurrection**: Doctor brings dead agents back to life (✨)
- **Real-time Events**: Watch attacks and resurrections in activity feed

## Architecture

- `agents/` - Agent definitions and personality configurations
- `engine/` - Core simulation engine and orchestration
- `memory/` - Agent memory storage and retrieval systems
- `locations/` - Town geography and location definitions
- `interactions/` - Conversation and interaction logic
- `main.py` - Entry point for running the simulation

## Getting Started

### Option 1: Command Line (Terminal)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the simulation
python main.py

# Run with custom configuration
python main.py --config config/custom.json
```

### Option 2: Web Dashboard (Browser) 🌐

```bash
# Install dependencies
pip install -r requirements.txt

# Start the web dashboard
python web_app.py

# Open your browser to http://localhost:5000
```

The web dashboard provides a **real-time visual interface** to monitor agents, locations, and interactions. See [WEB_README.md](WEB_README.md) for details.

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
