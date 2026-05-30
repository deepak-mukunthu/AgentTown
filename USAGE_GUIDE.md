# Usage Guide

## Two Ways to Run Agent Town

### 🖥️ Command Line Mode

Best for: Scripting, logging, headless servers

```bash
python main.py --steps 100 --speed 1.5
```

**Output:**
- Text-based updates in terminal
- Rich formatting with colors
- Step-by-step conversation logs
- Statistics every 10 steps

**Pros:**
- Lightweight
- Easy to redirect output to files
- Works over SSH
- Great for automation

**Cons:**
- No real-time visual overview
- Harder to track multiple agents
- Must read through logs

---

### 🌐 Web Dashboard Mode

Best for: Monitoring, demos, presentations

```bash
python web_app.py
# Then open http://localhost:5000 in your browser
```

**Features:**

#### 1. **Live Statistics**
Top of page shows:
- Number of active agents
- Number of locations
- Total memories created

#### 2. **Interactive Controls**
- ▶️ **Start**: Begin the simulation
- ⏸️ **Stop**: Pause the simulation
- 🔄 **Reset**: Restart with new agents

#### 3. **Location Panel**
Each location displays:
- Name and description
- Current capacity (e.g., "3/10")
- Agent badges showing who's present
- Visual hover effects

#### 4. **Agent Panel**
Each agent card shows:
- 📍 Current location
- ✨ Personality traits
- 💬 Conversation style
- 🧠 Number of memories

#### 5. **Real-Time Updates**
- Updates every 2 seconds automatically
- No page refresh needed
- Smooth transitions when agents move

**Pros:**
- Visual overview at a glance
- Easy to demo to others
- Beautiful, modern UI
- Real-time updates

**Cons:**
- Requires web browser
- Uses more resources
- Need network access (localhost)

---

## Comparison Table

| Feature | Command Line | Web Dashboard |
|---------|-------------|---------------|
| Real-time visual | ❌ | ✅ |
| Conversation logs | ✅ | ❌ |
| Resource usage | Low | Medium |
| Remote access | SSH only | Browser-based |
| Setup complexity | Simple | Simple |
| Screenshots | Terminal only | Full UI |
| Multi-user viewing | No | Yes |

---

## Common Use Cases

### Scenario 1: Quick Test
```bash
# Start with CLI for fast iteration
python main.py --steps 10 --speed 3.0
```

### Scenario 2: Demo/Presentation
```bash
# Use web dashboard for visual appeal
python web_app.py
# Show in browser to audience
```

### Scenario 3: Long-Running Simulation
```bash
# CLI with output redirect
python main.py --steps 1000 --speed 2.0 > simulation.log 2>&1 &
```

### Scenario 4: Development/Debugging
```bash
# Web dashboard for monitoring while developing
python web_app.py
# Keep browser open, make code changes, reset simulation
```

---

## Advanced Tips

### CLI Mode

**Save output to file:**
```bash
python main.py --steps 100 > output.log
```

**Run in background:**
```bash
nohup python main.py --steps 500 &
```

**Custom configuration:**
```bash
python main.py --config config/custom.json --steps 200
```

### Web Dashboard Mode

**Change port:**
Edit `web_app.py`, last line:
```python
socketio.run(app, port=8080)  # Use port 8080
```

**Slower/faster updates:**
Edit `web_app.py`, `simulation_loop()` function:
```python
time.sleep(1.0)  # Faster updates (1 second)
time.sleep(5.0)  # Slower updates (5 seconds)
```

**Add HTTPS (for remote access):**
```python
socketio.run(app, 
    certfile='cert.pem',
    keyfile='key.pem',
    host='0.0.0.0')
```

---

## Keyboard Shortcuts (CLI)

- `Ctrl+C`: Stop simulation gracefully
- `Ctrl+Z`: Pause (can resume with `fg`)

---

## Environment Variables

Both modes support:
```bash
export ANTHROPIC_API_KEY="your-key-here"  # Enable Claude conversations
export SIMULATION_SPEED="2.0"              # Default speed
export MAX_AGENTS="10"                     # Agent count
export LOG_LEVEL="INFO"                    # Logging verbosity
```

---

## Troubleshooting

### Web Dashboard Won't Start

**Issue:** Port 5000 already in use
```bash
# Find what's using the port
lsof -i :5000
# Kill it or change the port in web_app.py
```

**Issue:** Can't access from another computer
```bash
# Make sure firewall allows port 5000
# Or use SSH tunnel:
ssh -L 5000:localhost:5000 user@remote-server
```

### CLI Output Garbled

**Issue:** Terminal doesn't support colors
```bash
# Disable rich output
export NO_COLOR=1
python main.py
```

---

## Which Should You Use?

Choose **CLI** if:
- Running on a server without GUI
- Automating or scripting
- Need detailed conversation logs
- Want minimal resource usage

Choose **Web Dashboard** if:
- Demoing to stakeholders
- Need visual overview
- Monitoring multiple metrics
- Sharing with team members
- Creating screenshots/recordings

**Pro Tip:** Run both! Use CLI for logging and web dashboard for monitoring:
```bash
# Terminal 1
python main.py > detailed.log

# Terminal 2  
python web_app.py
# (connects to same simulation state if you modify to share state)
```

Enjoy your Agent Town! 🏘️
