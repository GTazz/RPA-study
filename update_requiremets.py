import subprocess
import sys
import os

def update_requirements():
    """
    Gets the current Python version and installed packages (pip freeze)
    and writes them to requirements.txt.
    """
    try:
        # Get Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        python_version_comment = f"# Python {python_version}\n"

        # Get installed packages using pip freeze
        result = subprocess.run([sys.executable, '-m', 'pip', 'freeze'], capture_output=True, text=True, check=True)
        packages = result.stdout

        # Define the requirements file path relative to the script
        script_dir = os.path.dirname(__file__)
        requirements_path = os.path.join(script_dir, 'requirements.txt')


        # Write to requirements.txt
        with open(requirements_path, 'w') as f:
            f.write(python_version_comment)
            f.write(packages)

        print(f"Successfully updated {requirements_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error running pip freeze: {e}")
        print(f"Stderr: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_requirements()