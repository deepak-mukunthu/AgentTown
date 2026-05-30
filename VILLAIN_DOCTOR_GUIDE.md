# 😈 Villain & ⚕️ Doctor Guide

## 🎭 The Drama Unfolds

Your Agent Town just got MUCH more interesting! Now featuring life-or-death drama with a **malicious villain** who kills and a **mysterious doctor** who resurrects the dead!

---

## 😈 **THE VILLAIN**

### Profile
- **Role Icon:** 😈
- **Personality:** Aggressive, volatile, unpredictable
- **Preferred Locations:** Town Square, Park (public areas for maximum chaos)
- **Conversation Style:** Direct and threatening

### The Anger System

The villain has an **anger meter** that builds over time:

```
😡 Anger: ▓▓▓▓▓▓▓▓▓░ (90% - DANGER!)
```

- **0-30%**: Calm, mostly harmless
- **30-60%**: Agitated, moves around more
- **60-100%**: ENRAGED - Will attack!

### Attack Mechanics

When anger exceeds **60%**:
1. Villain looks for victims at current location
2. Chooses a random living agent (excluding other villains)
3. **KILLS THEM INSTANTLY** 💀
4. Anger drops by 50% after successful attack
5. Must wait 10 simulation steps before next kill (cooldown)

### Behavior Patterns

- **Anger builds**: +5% every simulation step
- **Moves more when angry**: 30% chance to move when anger > 30%
- **Less social**: 50% less likely to have normal conversations
- **Threatening**: Occasionally has menacing conversations
- **Cooldown system**: Prevents rapid killing sprees

### What You'll See

```
[09:15] ⚠️ ATTACK at Town Square
😈 Victor attacked Alice
💀 Alice is dead!
```

**Activity Feed Display:**
- Red background warning
- Bold red text
- Shows attacker name, victim name, location
- Skull emoji for dramatic effect

---

## ⚕️ **THE DOCTOR**

### Profile
- **Role Icon:** ⚕️
- **Personality:** Empathetic, calm, analytical
- **Preferred Locations:** Library, Community Center (places of learning)
- **Conversation Style:** Formal and professional

### The Resurrection Power

The doctor has ONE mission: **Save lives!**

### Healing Mechanics

The doctor continuously:
1. **Scans current location** for dead agents
2. If found, **instantly resurrects them** ✨
3. If none found, **moves towards locations with casualties**
4. Prioritizes finding and healing the dead

### Behavior Patterns

- **Always searching**: Moves 1.5x more than normal agents
- **Smart pathfinding**: 70% chance to move towards dead agents
- **Automatic healing**: Resurrects on contact, no delay
- **Can save anyone**: Works on all victims regardless of role
- **Never stops**: Continuously patrols for casualties

### What You'll See

```
[09:17] ✨ RESURRECTION at Town Square
⚕️ Dr. Emma resurrected Alice
✅ Alice is alive again!
```

**Activity Feed Display:**
- Blue background (miracle!)
- Blue text
- Shows doctor name, patient name, location
- Sparkle emoji for magic effect

---

## 💀 **LIFE & DEATH STATUS**

### Alive Agents
- **Status:** ✅ Alive
- **Card:** Normal colors, bright
- **Behavior:** Can move, talk, interact normally

### Dead Agents
- **Status:** 💀 DEAD
- **Card:** Dark gray, semi-transparent, skull emoji
- **Behavior:** Cannot move, talk, or do anything
- **Waiting:** Need doctor to resurrect them

### The Cycle of Life

```
😈 Villain gets angry (60%+)
    ↓
⚠️  Attacks random victim
    ↓
💀 Agent dies (marked as dead)
    ↓
⚕️  Doctor senses death
    ↓
🚶 Doctor moves to location
    ↓
✨ Doctor resurrects victim
    ↓
✅ Agent alive again!
    ↓
😈 Villain anger builds again...
```

---

## 🎮 **HOW TO WATCH THE DRAMA**

### Step 1: Start the Dashboard
```bash
python web_app.py
# Open http://localhost:3000
```

### Step 2: Identify Key Players

Look for these in the **Agents Panel**:
- **😈 [Name]** - The Villain (red border)
- **⚕️ [Name]** - The Doctor (blue border)

### Step 3: Monitor the Villain

Watch the **anger bar** under villain's card:
```
😡 Anger: ▓▓▓░░░░░░░ (30%)
```

When it reaches **60%+**, someone is about to die!

### Step 4: Watch the Activity Feed

The right panel shows all dramatic events:
- 🚶 Movement (orange)
- 💬 Conversations (green)
- **⚠️ ATTACKS** (red background!)
- **✨ RESURRECTIONS** (blue background!)

### Step 5: Observe the Patterns

**Typical scenario:**
1. Villain anger slowly builds
2. Villain moves to busy location (Town Square)
3. **[09:15] ⚠️ ATTACK!** - Someone dies
4. Victim's card turns dark with 💀
5. Doctor notices and starts moving
6. **[09:18] ✨ RESURRECTION!** - Victim saved!
7. Cycle repeats...

---

## 📊 **STATISTICS TO WATCH**

### Deaths Counter
Count the number of attack events in activity feed

### Resurrections Counter
Count the number of resurrection events

### Death Rate
How often does villain attack? (Every ~20 steps typically)

### Save Rate
Does doctor arrive in time? (Usually yes!)

### Villain Anger Trend
Watch the anger bar fill up over time

---

## 🎬 **EPIC SCENARIOS**

### Scenario 1: Mass Casualty
- Villain goes on killing spree
- Multiple agents dead
- Doctor frantically moves between locations
- Can doctor save everyone?

### Scenario 2: Near Miss
- Villain and doctor at same location
- Villain attacks someone
- Doctor immediately resurrects them
- Instant save!

### Scenario 3: The Hunt
- Agent dies at remote location
- Doctor must travel across town
- Dead agent waits...
- Will help arrive in time? (Yes, always!)

### Scenario 4: Anger Overflow
- Villain anger at 100%
- But no other agents nearby
- Villain roams looking for victims
- Dramatic tension builds...

---

## 🔥 **PRO TIPS**

### Watch the Anger Bar!
The red bar under villain's card is your early warning system.

### Track Dead Agents
Dark gray cards with 💀 = currently dead, waiting for doctor

### Doctor's Movement
If doctor suddenly moves, they probably sensed a death!

### Cooldown Period
After an attack, villain has 10-step cooldown. Watch the step counter!

### Memory System
Both victim and attacker remember the attack forever (importance: 1.0)
Doctor and patient remember resurrection (importance: 1.0)

---

## 🎨 **VISUAL GUIDE**

### Agent Card Colors

| Role | Border Color | Icon |
|------|--------------|------|
| Villain | 🔴 Red | 😈 |
| Doctor | 🔵 Blue | ⚕️ |
| Dead Agent | ⚫ Dark Gray | 💀 |
| Others | 🟢 Green | Various |

### Activity Feed Colors

| Event | Background | Icon |
|-------|------------|------|
| Attack | 🔴 Light Red | ⚠️ |
| Resurrection | 🔵 Light Blue | ✨ |
| Conversation | ⚪ White | 💬 |
| Movement | ⚪ White | 🚶 |

---

## ⚙️ **CONFIGURATION**

### Adjust Villain Aggression

Edit `agents/base_agent.py`:
```python
# Line: increase_anger()
agent.increase_anger(0.05)  # Change to 0.1 for faster anger
```

### Adjust Attack Threshold

Edit `agents/base_agent.py`:
```python
# Line: is_angry()
return self.anger_level > 0.6  # Change to 0.4 for earlier attacks
```

### Adjust Cooldown

Edit `engine/simulation.py`:
```python
# Line: villain_action()
if ... and self.step_count - agent.last_kill_step > 10:  # Change 10 to 5 for faster attacks
```

### Adjust Doctor Speed

Edit `agents/base_agent.py`:
```python
# Line: should_move() for doctor
probability *= 1.5  # Change to 2.0 for ultra-fast doctor
```

---

## 🐛 **TROUBLESHOOTING**

### Villain Never Attacks?
- Check anger bar - may not have reached 60% yet
- Villain needs other agents at same location
- Wait longer, anger builds gradually

### Doctor Doesn't Resurrect?
- Dead agent must be at same location as doctor
- Doctor will move there automatically
- Be patient, doctor is on the way!

### Too Many Deaths?
- Lower villain anger increase rate
- Increase attack threshold
- Increase cooldown period

### Not Enough Action?
- Increase villain anger rate
- Lower attack threshold
- Decrease cooldown period

---

## 🎉 **FUN FACTS**

- Villain anger increases **every single step**
- Doctor can sense deaths **anywhere in town**
- Dead agents remember being killed (even while dead!)
- Villain memories include the attack
- Doctor always prioritizes healing over conversation
- Villain role is **always** assigned first
- Doctor role is **always** assigned second
- Only 1 villain and 1 doctor per simulation
- Villain can't attack other villains (professional courtesy?)
- Doctor can resurrect anyone, even villains (Hippocratic Oath!)

---

Enjoy the drama! Your Agent Town just became a soap opera! 🎭💀✨

## 🌟 **Coming Soon** (Ideas for Future)

- 👮 Police role to arrest villain
- 🛡️ Guardian role to protect others
- ⚖️ Judge role to put villain on trial
- 💊 Poison mechanic (slow death)
- 🏥 Hospital location for healing
- 📊 Kill/save statistics dashboard
- 🎯 Villain targeting preferences
- 🕵️ Detective role to investigate deaths

The possibilities are endless! 🚀
