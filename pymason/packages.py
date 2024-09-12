# package.py
import subprocess
from config import POETRY_EXECUTABLE

class PackageManager:
    def add_package(self, package_name):
        """Adds a package using Poetry."""
        print(f"Adding package {package_name} using Poetry...")
        subprocess.run([POETRY_EXECUTABLE, 'add', package_name], check=True)
        print(f"Package {package_name} added successfully.")

    def remove_package(self, package_name):
        """Removes a package using Poetry."""
        print(f"Removing package {package_name} using Poetry...")
        subprocess.run([POETRY_EXECUTABLE, 'remove', package_name], check=True)
        print(f"Package {package_name} removed successfully.")
