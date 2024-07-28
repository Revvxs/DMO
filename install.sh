#!/bin/bash

# Update and install dependencies
pkg update && pkg upgrade -y
pkg install python git -y
pip install colorama ipinfo

# Clone the repository
git clone https://github.com/yourusername/termux-tool.git

# Navigate to the repository directory
cd termux-tool

# Make the Python script executable
chmod +x dmo_tool.py

# Run the script
python dmo_tool.py
