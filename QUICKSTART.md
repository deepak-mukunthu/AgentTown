# ⚡ Quick Start Guide

Get Agent Town running in **under 2 minutes**!

---

## 🚀 **Super Quick Start (One Command)**

### macOS/Linux:
```bash
./demo.sh
```

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python web_app.py
```

Then open: **http://localhost:3000**

---

## 📋 **Step-by-Step (If you prefer)**

### 1. **Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. **Choose Your Mode**

#### Option A: Web Dashboard (Recommended) 🌐
```bash
python web_app.py
```
Then open: **http://localhost:3000**
Click **▶️ Start** button!

#### Option B: Terminal Mode 🖥️
```bash
python main.py --steps 50
```

---

## 🎮 **What to Expect**

### You'll See:
- **8 agents** with unique roles and personalities
- **😈 1 Villain** who gets angry and kills others
- **⚕️ 1 Doctor** who resurrects the dead
- **6 regular agents** (artists, scholars, explorers, etc.)

### Events You'll Witness:
- 💬 **Conversations** between agents
- 🚶 **Agents moving** between locations
- ⚠️ **ATTACKS** when the villain gets angry!
- ✨ **RESURRECTIONS** when the doctor saves someone!

---

## 🎯 **What to Do in the Dashboard**

1. **Click "▶️ Start"** (top right button)
2. **Watch the Villain** (😈 with red border)
   - See the anger bar fill up
3. **Wait for Drama** 
   - Attack happens when anger reaches 60%
4. **Watch the Doctor** (⚕️ with blue border)
   - Rushes to resurrect victims
5. **Read Activity Feed** (right panel)
   - See all conversations, movements, attacks, resurrections

---

## ⌨️ **Quick Commands**

### Run different scenarios:
```bash
# Quick test (10 steps)
python main.py --steps 10 --speed 3.0

# Full simulation (100 steps)
python main.py --steps 100 --speed 1.5

# Long run (500 steps)
python main.py --steps 500 --speed 2.0
```

### Web dashboard on different port:
Edit last line of `web_app.py`:
```python
socketio.run(app, port=8080, ...)  # Change 3000 to 8080
```

---

## 🐛 **Troubleshooting**

### Port Already in Use?
```bash
# Kill existing process
lsof -i :3000
kill -9 <PID>

# Or use different port (edit web_app.py)
```

### Import Errors?
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Demo Script Won't Run?
```bash
# Make it executable
chmod +x demo.sh

# Or run directly with bash
bash demo.sh
```

---

## 📺 **Video Tutorial (If Made)**

Coming soon: Screen recording showing:
1. Running `./demo.sh`
2. Opening browser to localhost:3000
3. Clicking Start
4. Watching villain attack someone
5. Watching doctor resurrect them

---

## 🎓 **Next Steps**

Once you've seen the basic simulation:

1. **Read the guides:**
   - `VILLAIN_DOCTOR_GUIDE.md` - Understand the drama
   - `DASHBOARD_FEATURES.md` - Learn all features
   - `USAGE_GUIDE.md` - CLI vs Web comparison

2. **Customize it:**
   - Change villain anger rate
   - Adjust number of agents
   - Modify personality traits
   - Add new roles

3. **Experiment:**
   - Run longer simulations
   - Watch emergent patterns
   - Track statistics
   - Analyze conversations

---

## 💡 **Pro Tips**

- **Best view:** Maximize browser window for 3-column layout
- **Coolest moment:** When villain's anger bar hits 60%+ 😈
- **Most dramatic:** Watching someone die then get resurrected ✨
- **Interesting pattern:** Scholars stay in library, explorers roam
- **Hidden feature:** Click Reset to get different agents!

---

## 🎉 **You're Ready!**

That's it! You should now see your Agent Town simulation running.

**Enjoy the drama!** 🏘️😈⚕️✨

---

## 📞 **Need Help?**

Check these files:
- `README.md` - Full documentation
- `WEB_README.md` - Web dashboard details
- `TESTING.md` - Known working setup

Or create an issue on GitHub!
