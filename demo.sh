#!/bin/bash

# Agent Town Quick Demo Script
# This script sets up and runs the Agent Town simulation

set -e  # Exit on error

echo "🏘️  Agent Town - Quick Demo Setup"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    echo "Please install Python 3.10+ from https://www.python.org/"
    exit 1
fi

echo -e "${GREEN}✓${NC} Python 3 found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment created"
else
    echo -e "${GREEN}✓${NC} Virtual environment exists"
fi
echo ""

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Check if packages are installed
if ! python -c "import flask" 2>/dev/null; then
    echo -e "${YELLOW}Installing dependencies...${NC}"
    pip install -q -r requirements.txt
    echo -e "${GREEN}✓${NC} Dependencies installed"
else
    echo -e "${GREEN}✓${NC} Dependencies already installed"
fi
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Note:${NC} No .env file found"
    echo "  The simulation will work with template conversations."
    echo "  To enable Claude-powered conversations, create a .env file:"
    echo "  cp .env.example .env"
    echo "  Then add your ANTHROPIC_API_KEY"
    echo ""
fi

# Ask user which mode to run
echo -e "${BLUE}How would you like to run Agent Town?${NC}"
echo ""
echo "  1) 🌐 Web Dashboard (Recommended - Visual & Interactive)"
echo "  2) 🖥️  CLI Mode (Terminal-based)"
echo "  3) 🧪 Quick Test (10 steps, fast speed)"
echo ""
read -p "Enter choice [1-3]: " choice

echo ""

case $choice in
    1)
        echo -e "${GREEN}Starting Web Dashboard...${NC}"
        echo ""
        echo "📍 Dashboard will be available at: ${BLUE}http://localhost:3000${NC}"
        echo ""
        echo "🎮 What to do:"
        echo "  1. Open http://localhost:3000 in your browser"
        echo "  2. Click the '▶️ Start' button"
        echo "  3. Watch agents interact, move, and drama unfold!"
        echo ""
        echo "⚠️  Press Ctrl+C to stop the server"
        echo ""
        sleep 2
        python web_app.py
        ;;
    2)
        echo -e "${GREEN}Starting CLI Mode...${NC}"
        echo ""
        echo "Running 50 steps at normal speed..."
        echo ""
        python main.py --steps 50 --speed 1.0
        ;;
    3)
        echo -e "${GREEN}Running Quick Test...${NC}"
        echo ""
        echo "10 steps at 3x speed for quick demo..."
        echo ""
        python main.py --steps 10 --speed 3.0
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac
