# Agent Town Web Dashboard 🌐

A real-time web-based monitoring dashboard for Agent Town simulation.

## Features

- **Live Updates**: Watch agents move and interact in real-time using WebSocket
- **Interactive Controls**: Start, stop, and reset the simulation from your browser
- **Visual Location Map**: See which agents are at each location
- **Agent Profiles**: View personality traits, conversation styles, and memory counts
- **Statistics Dashboard**: Track simulation progress with live stats

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Web App

```bash
python web_app.py
```

### 3. Open Your Browser

Navigate to: **http://localhost:5000**

## Dashboard Features

### Header Section
- **Current Time**: Simulation time (starts at 09:00)
- **Step Counter**: Number of simulation steps completed
- **Controls**: Start/Stop/Reset buttons

### Statistics Panel
- Total number of agents
- Number of locations
- Total memories created across all agents

### Locations Panel
- Visual cards for each location
- Shows capacity and current occupancy
- Lists agents present at each location
- Hover effects for better UX

### Agents Panel
- Individual agent cards
- Shows current location
- Displays personality traits
- Shows conversation style
- Memory count

## How It Works

The web dashboard uses:
- **Flask**: Web server framework
- **Socket.IO**: Real-time bidirectional communication
- **Threading**: Background simulation loop
- **REST API**: Control endpoints for start/stop/reset

### API Endpoints

- `GET /api/status` - Get current simulation state
- `POST /api/start` - Start the simulation
- `POST /api/stop` - Stop the simulation
- `POST /api/reset` - Reset to initial state

### WebSocket Events

- `connect` - Client connects, receives initial state
- `simulation_update` - Server broadcasts state updates every step

## Customization

### Change Update Speed

Edit `web_app.py`, line in `simulation_loop()`:
```python
time.sleep(2.0)  # Change to adjust seconds per step
```

### Modify Appearance

Edit `templates/dashboard.html` CSS section to customize:
- Colors
- Layout
- Fonts
- Animations

### Add More Stats

Extend `get_simulation_state()` in `web_app.py` to include:
- Most active agents
- Conversation counts
- Location visit frequencies

## Running in Production

For production deployment, use a proper WSGI server:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn --worker-class eventlet -w 1 web_app:app
```

Or deploy to platforms like:
- Heroku
- Railway
- Render
- DigitalOcean

## Troubleshooting

### Port Already in Use
```bash
# Change port in web_app.py:
socketio.run(app, port=5001)  # Use different port
```

### WebSocket Connection Issues
- Check firewall settings
- Ensure port 5000 is accessible
- Try Chrome/Firefox (better WebSocket support)

### Simulation Not Updating
- Check browser console for errors
- Verify Socket.IO connection in Network tab
- Ensure simulation is started (click Start button)

## Screenshots

The dashboard displays:
- 📊 Real-time statistics
- 📍 Interactive location cards
- 👥 Agent profiles with personality info
- ⚡ Live updates without page refresh

## Technologies Used

- **Backend**: Flask, Flask-SocketIO
- **Frontend**: Vanilla JavaScript, Socket.IO Client
- **Styling**: Custom CSS with gradient backgrounds
- **Communication**: WebSocket for real-time updates

Enjoy monitoring your Agent Town! 🏘️✨
