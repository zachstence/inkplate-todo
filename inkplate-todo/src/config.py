"""
Loads application configuration from JSON files
"""

import json

config = {}

try:
    with open("secret/network.json", "r") as f:
        parsed = json.load(f)
        ssid = parsed["ssid"]
        password = parsed["password"]

        config["network"] = {
            "ssid": ssid,
            "password": password,
        }
except OSError as e:
    print("Unable to load network credentials",)


print(f"Loaded config\n{json.dumps(config)}")
