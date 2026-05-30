#!/usr/bin/env python3
"""
Web-based monitoring dashboard for Agent Town
"""

import json
import threading
import time
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from dotenv import load_dotenv

from agents.agent_factory import AgentFactory
from locations.location import Location
from engine.simulation import SimulationEngine


# Load environment
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'agent-town-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global simulation state
simulation = None
simulation_thread = None
simulation_running = False


def load_config(config_path: str = "config/default.json") -> dict:
    """Load configuration from JSON file"""
    with open(config_path, 'r') as f:
        return json.load(f)


def create_locations(location_configs: list) -> list:
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


def initialize_simulation():
    """Initialize the simulation"""
    global simulation

    config = load_config()
    locations = create_locations(config["locations"])
    location_names = [loc.name for loc in locations]

    num_agents = config["simulation"]["max_agents"]
    agents = AgentFactory.create_agents(num_agents, location_names)

    simulation = SimulationEngine(
        agents=agents,
        locations=locations,
        time_step_seconds=config["simulation"]["time_step_seconds"]
    )

    return simulation


def get_simulation_state():
    """Get current simulation state as JSON"""
    if not simulation:
        return None

    state = {
        "step_count": simulation.step_count,
        "current_time": simulation.current_time.strftime("%H:%M"),
        "agents": [],
        "locations": {},
        "recent_events": simulation.recent_events[-20:]  # Last 20 events
    }

    # Add agent information
    for agent in simulation.agents:
        state["agents"].append({
            "name": agent.name,
            "personality": ", ".join(agent.personality_traits),
            "style": agent.conversation_style,
            "location": agent.current_location,
            "memory_count": len(agent.memories),
            "role": agent.role,
            "status": agent.status,
            "anger_level": agent.anger_level if agent.role == "villain" else 0
        })

    # Add location information
    for loc_name, location in simulation.locations.items():
        state["locations"][loc_name] = {
            "name": location.name,
            "description": location.description,
            "agents": location.agents,
            "capacity": location.capacity,
            "count": len(location.agents)
        }

    return state


def run_simulation_step():
    """Run one simulation step and emit updates"""
    global simulation

    if simulation and simulation_running:
        simulation.step()
        state = get_simulation_state()
        socketio.emit('simulation_update', state)


def simulation_loop():
    """Background thread for running simulation"""
    global simulation_running

    while simulation_running:
        run_simulation_step()
        time.sleep(2.0)  # 2 seconds per step


@app.route('/')
def index():
    """Render main dashboard"""
    return render_template('dashboard.html')


@app.route('/api/status')
def status():
    """Get current simulation status"""
    state = get_simulation_state()
    if state:
        return jsonify(state)
    return jsonify({"error": "Simulation not initialized"}), 404


@app.route('/api/start', methods=['POST'])
def start_simulation():
    """Start the simulation"""
    global simulation, simulation_thread, simulation_running

    if not simulation:
        initialize_simulation()

    if not simulation_running:
        simulation_running = True
        simulation_thread = threading.Thread(target=simulation_loop, daemon=True)
        simulation_thread.start()
        return jsonify({"status": "started"})

    return jsonify({"status": "already_running"})


@app.route('/api/stop', methods=['POST'])
def stop_simulation():
    """Stop the simulation"""
    global simulation_running

    simulation_running = False
    return jsonify({"status": "stopped"})


@app.route('/api/reset', methods=['POST'])
def reset_simulation():
    """Reset the simulation"""
    global simulation, simulation_running

    simulation_running = False
    if simulation_thread:
        simulation_thread.join(timeout=3)

    simulation = None
    initialize_simulation()

    return jsonify({"status": "reset"})


@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    if simulation:
        state = get_simulation_state()
        socketio.emit('simulation_update', state)


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')


if __name__ == '__main__':
    print("🏘️  Agent Town Web Dashboard")
    print("=" * 50)
    print("Initializing simulation...")

    initialize_simulation()

    print(f"✓ Created {len(simulation.agents)} agents")
    print(f"✓ Set up {len(simulation.locations)} locations")
    print()
    print("Starting web server...")
    print("🌐 Open your browser to: http://localhost:3000")
    print()

    socketio.run(app, debug=False, host='127.0.0.1', port=3000, allow_unsafe_werkzeug=True)
