import json

SETTINGS_FILE = 'tabels.json'

def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"ip": "127.0.0.1", "error_count": 3, "timeout": 1}
    except json.JSONDecodeError:
        return {"ip": "127.0.0.1", "error_count": 3, "timeout": 1}

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)
