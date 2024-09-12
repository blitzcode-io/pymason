# util/project_manager.py
import os
import toml
import subprocess

def clone_copier_template(project_name, template_url):
    """Clones a project template using Copier."""
    subprocess.run(['copier', template_url, project_name], check=True)

def update_pyproject_with_bench_section(project_dir):
    """Adds a [bench.tool] section to the pyproject.toml file."""
    pyproject_path = os.path.join(project_dir, 'pyproject.toml')
    
    if os.path.exists(pyproject_path):
        # Load the current pyproject.toml
        with open(pyproject_path, 'r') as f:
            pyproject_data = toml.load(f)
        
        # Get the Python version being used
        python_version = os.popen('python --version').read().strip().split()[1]
        
        # Add the [bench.tool] section
        if 'bench' not in pyproject_data:
            pyproject_data['bench'] = {}
        
        pyproject_data['bench']['tool'] = {
            'python_version': python_version
        }
        
        # Write the updated pyproject.toml back to the file
        with open(pyproject_path, 'w') as f:
            toml.dump(pyproject_data, f)
        
        print(f"[bench.tool] section added to pyproject.toml with Python version {python_version}.")
    else:
        print("pyproject.toml not found, unable to add [bench.tool] section.")
