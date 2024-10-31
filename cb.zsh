#!/bin/zsh

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title cb
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description uses clipboard creator

cd /Users/ryanjinnette/Code/ClipBoard/
source /Users/ryanjinnette/Code/ClipBoard/venv/bin/activate
pip list
which python3
python Clipboard_Creator.py
deactivate

