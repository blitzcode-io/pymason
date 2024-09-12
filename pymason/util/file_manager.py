# file_manager.py
import os
from pathlib import Path

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_subdirectories(path):
    """Lists all subdirectories in a given directory."""
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def get_data_directory():
    if os.name == 'nt':
        appdata = os.getenv('APPDATA')
        if appdata:
            return Path(appdata) / "pymason" / "python"
        else:
            raise EnvironmentError("APPDATA environment variable is not set.")

    else:  # Linux/macOS
        xdg_data_home = os.getenv('XDG_DATA_HOME', Path.home() / '.local' / 'share')
        return Path(xdg_data_home) / "pymason" / "python"