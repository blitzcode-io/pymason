# installer.py
import os
import shutil
from util.file_manager import ensure_directory, list_subdirectories, get_data_directory

class PythonInstaller:
    def __init__(self, version="3.11.0"):
        self.version = version
        self.install_dir = os.path.join(get_data_directory(), self.version)
        ensure_directory(self.install_dir)

    def install_silently(self):
        # ... (installation logic unchanged)
        pass

    def get_installation_path(self):
        return self.install_dir

class PythonManager:
    def __init__(self):
        self.python_root = get_data_directory()

    def list_installed_pythons(self):
        """Returns a list of installed Python versions."""
        if not os.path.exists(self.python_root):
            return []
        return list_subdirectories(self.python_root)

    def uninstall_python(self, version):
        """Uninstalls the specified Python version."""
        version_path = os.path.join(self.python_root, version)
        if os.path.exists(version_path):
            print(f"Uninstalling Python {version}...")
            shutil.rmtree(version_path)
            print(f"Python {version} uninstalled.")
        else:
            print(f"Python {version} is not installed.")
