# cli.py
import click
from installer import PythonInstaller, PythonManager
from projects import ProjectManager
from packages import PackageManager

@click.group()
def cli():
    pass

# ------------------- Python Management Group -------------------
@click.group()
def python():
    """Commands to manage Python versions."""
    pass

@click.command()
@click.option('--version', default='3.11.0', help='Specify the Python version to install')
def install(version):
    """Installs Python silently in the specified directory."""
    installer = PythonInstaller(version)
    installer.install_silently()

@click.command()
@click.argument('version')
def uninstall(version):
    """Uninstalls the specified Python version."""
    manager = PythonManager()
    manager.uninstall_python(version)

@click.command()
def list():
    """Lists all installed Python versions."""
    manager = PythonManager()
    installed_versions = manager.list_installed_pythons()
    if installed_versions:
        click.echo("Installed Python versions:")
        for version in installed_versions:
            click.echo(f"- {version}")
    else:
        click.echo("No Python versions installed.")

python.add_command(install)
python.add_command(uninstall)
python.add_command(list)

# ------------------- Project Management Group -------------------
@click.group()
def projects():
    """Commands to manage projects."""
    pass

@click.command()
@click.argument('project_name')
@click.option('--copier', help='URL of the Copier template repository to use')
def new(project_name, copier):
    """Creates a new project using Poetry or Copier."""
    project_manager = ProjectManager()
    if copier:
        project_manager.create_from_copier(project_name, copier)
    else:
        project_manager.create_poetry_project(project_name)

@click.command()
@click.option('--venv-path', help='Optional path to specify custom location for virtual environment')
def install(venv_path):
    """Installs dependencies using Poetry and sets up the virtual environment."""
    project_manager = ProjectManager()
    project_manager.install_dependencies(venv_path)

projects.add_command(new)
projects.add_command(install)

# ------------------- Package Management Group -------------------
@click.group()
def package():
    """Commands to manage packages using Poetry."""
    pass

@click.command()
@click.argument('package_name')
def add(package_name):
    """Adds a package using Poetry."""
    package_manager = PackageManager()
    package_manager.add_package(package_name)

@click.command()
@click.argument('package_name')
def remove(package_name):
    """Removes a package using Poetry."""
    package_manager = PackageManager()
    package_manager.remove_package(package_name)

package.add_command(add)
package.add_command(remove)

cli.add_command(python)
cli.add_command(projects)
cli.add_command(package)

if __name__ == '__main__':
    cli()
