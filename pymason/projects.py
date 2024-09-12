# projects.py
import os
import subprocess
from config import POETRY_EXECUTABLE
from util.project_manager import clone_copier_template, update_pyproject_with_bench_section

class ProjectManager:
    def create_poetry_project(self, project_name):
        """Creates a new project using 'poetry new'."""
        print(f"Creating new Poetry project: {project_name}")
        subprocess.run([POETRY_EXECUTABLE, 'new', project_name], check=True)

        # Add [bench.tool] section to pyproject.toml
        project_dir = os.path.join(os.getcwd(), project_name)
        update_pyproject_with_bench_section(project_dir)

    def create_from_copier(self, project_name, template_url):
        """Creates a new project from a Copier template."""
        print(f"Cloning project from template: {template_url}")
        clone_copier_template(project_name, template_url)

        # Check if the cloned project has a pyproject.toml, otherwise run 'poetry init'
        pyproject_path = os.path.join(project_name, 'pyproject.toml')
        if not os.path.exists(pyproject_path):
            print("Template does not have a pyproject.toml. Running 'poetry init'...")
            subprocess.run([POETRY_EXECUTABLE, 'init'], cwd=project_name, check=True)

        # Add [bench.tool] section to pyproject.toml
        project_dir = os.path.join(os.getcwd(), project_name)
        update_pyproject_with_bench_section(project_dir)

    def install_dependencies(self, venv_path=None):
        """Installs dependencies using Poetry and sets up the virtual environment."""
        project_dir = os.getcwd()

        # Set default virtual environment path to .venv in the current directory
        if venv_path is None:
            venv_path = os.path.join(project_dir, '.venv')

        print(f"Setting virtual environment path to: {venv_path}")
        os.environ['POETRY_VIRTUALENVS_PATH'] = venv_path

        # Run poetry install
        print("Installing dependencies using Poetry...")
        subprocess.run([POETRY_EXECUTABLE, 'install'], cwd=project_dir, check=True)

        print("Dependencies installed and virtual environment set up.")
