"""
Holds application configuration loaded from config.json
"""

import json

with open("config.json", "r") as f:
    config = json.load(f)
