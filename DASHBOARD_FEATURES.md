# Dashboard Features

## 🌐 Access the Dashboard

**URL:** http://localhost:3000

---

## 📊 **Three-Panel Layout**

### 1. **Locations Panel** (Left)
- Shows all 5 locations in the town
- Displays current occupancy (e.g., "3/10")
- Lists agents present at each location with colored badges
- Location descriptions
- Hover effects for better UX

### 2. **Agents Panel** (Middle)
- Individual card for each agent
- **Role icons**:
  - 🎨 Artist
  - 📚 Scholar
  - 🧭 Explorer
  - 🎭 Socialite
  - 🏠 Resident
- Current location
- Personality traits
- Conversation style
- Memory count (updates in real-time)

### 3. **Live Activity Feed** (Right) ⭐ NEW!
- **Real-time conversation monitoring**
- **Movement tracking**
- Color-coded events:
  - 🟢 Green border = Conversations
  - 🟠 Orange border = Movements
- Auto-scrolls to show latest activity
- Shows last 20 events

---

## 💬 **Conversation Monitoring**

### What You'll See:
```
[09:15] 💬 Conversation at Coffee Shop
Between Alice and Bob

Alice: "Hey Bob, how's your day going?"
Bob: "Pretty good, thanks! Just enjoying the atmosphere here..."
```

### Features:
- Timestamp for each conversation
- Location where conversation happened
- Participant names
- Full conversation exchanges
- Speaker names highlighted in green
- Quoted messages for easy reading

---

## 🚶 **Movement Tracking**

### What You'll See:
```
[09:16] 🚶 Alice moved from Coffee Shop to Park
```

### Features:
- Timestamp
- Agent name
- Origin and destination locations
- Clean, readable format

---

## 🎭 **Role-Based Behaviors**

### 5 Agent Roles with Unique Behaviors:

#### 🎨 **Artist**
- **Personality:** Creative, thoughtful, empathetic
- **Preferred Locations:** Coffee Shop, Park, Community Center
- **Behavior:** Seeks inspiring environments
- **Conversation Style:** Thoughtful

#### 📚 **Scholar**
- **Personality:** Analytical, curious, thoughtful
- **Preferred Locations:** Library, Coffee Shop
- **Behavior:** 
  - Moves 50% less than normal (stays to study)
  - Interacts 20% more (loves discussions)
- **Conversation Style:** Philosophical

#### 🧭 **Explorer**
- **Personality:** Adventurous, energetic, curious
- **Preferred Locations:** Park, Town Square
- **Behavior:** Moves 2x more frequently (always exploring)
- **Conversation Style:** Enthusiastic

#### 🎭 **Socialite**
- **Personality:** Friendly, optimistic, witty
- **Preferred Locations:** Town Square, Coffee Shop, Community Center
- **Behavior:** Interacts 2x more frequently (loves people)
- **Conversation Style:** Casual

#### 🏠 **Resident**
- **Personality:** Calm, pragmatic, friendly
- **Preferred Locations:** None (goes anywhere)
- **Behavior:** Balanced, no special modifiers
- **Conversation Style:** Casual

---

## 🎮 **Interactive Controls**

### Top Right Buttons:
1. **▶️ Start** - Begin the simulation
2. **⏸️ Stop** - Pause the simulation
3. **🔄 Reset** - Create new agents and restart

---

## 📈 **Live Statistics**

Top of dashboard shows:
- 👥 **Total Agents** (typically 8)
- 📍 **Number of Locations** (5)
- 🧠 **Total Memories** (increases as agents interact)

Updates every 2 seconds automatically via WebSocket!

---

## 🔄 **Real-Time Updates**

### How It Works:
- WebSocket connection to server
- Updates every 2 seconds
- No page refresh needed
- Smooth, instant updates

### What Updates in Real-Time:
- Agent locations change
- Memory counts increase
- Activity feed adds new events
- Location occupancy updates
- Statistics refresh

---

## 🎨 **Visual Design**

### Color Scheme:
- **Purple gradient background** (#667eea to #764ba2)
- **White panels** with shadows
- **Green accents** for agents and conversations
- **Orange accents** for movement events
- **Purple accents** for UI elements

### Typography:
- Clean, modern Segoe UI font
- Bold headers
- Color-coded text for different elements
- Readable font sizes

---

## 💡 **Usage Tips**

### Getting Started:
1. Open http://localhost:3000
2. Click "▶️ Start"
3. Watch the Activity Feed come alive!

### What to Watch For:
- **Explorers** moving around frequently
- **Socialites** starting lots of conversations
- **Scholars** hanging out in the Library
- **Artists** gathering at creative spaces
- Memory counts increasing as agents interact

### Best Experience:
- Keep Activity Feed visible on right side
- Watch how roles affect behavior
- Notice preferred location patterns
- See how conversations build memories

---

## 🐛 **Troubleshooting**

### Activity Feed Not Updating?
- Check if simulation is started (click ▶️)
- Verify WebSocket connection in browser console
- Try refreshing the page

### Server Not Running?
```bash
cd /Users/dmukunthu/Documents/PersonalProjects/AgentTown
source venv/bin/activate
python web_app.py
```

### Port 3000 Already in Use?
Edit `web_app.py` last line to use a different port:
```python
socketio.run(app, port=8888, ...)
```

---

## 🚀 **Future Enhancements**

Potential additions:
- Filter activity feed by type (conversations only, movements only)
- Search/filter conversations by agent
- Export conversation logs
- Adjust simulation speed from UI
- Click on agent to see full memory history
- Heatmap showing popular locations
- Conversation sentiment analysis

---

Enjoy watching your Agent Town come alive! 🏘️✨
