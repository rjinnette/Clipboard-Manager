#!/bin/zsh

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title cb
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description uses clipboard creator

cd /Users/ryanjinnette/Documents/Code/ClipBoard/
source venv/bin/activate
python3 Clipboard_Creator.py
deactivate

