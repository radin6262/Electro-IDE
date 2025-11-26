import subprocess
import sys
import os

def run_main_app(app_file="main.py"):
    """
    Launches the main app in a new PowerShell window and exits the updater.
    """
    if os.path.exists(app_file):
        subprocess.Popen([
            "powershell",
            "-NoExit",  # optional: keep the PowerShell window open
            "-Command",
            f'python "{os.path.abspath(app_file)}"'
        ])
        print(f"Main app '{app_file}' launched. Exiting updater...")
        sys.exit(0)
    else:
        print(f"Cannot run '{app_file}', file not found.")

run_main_app()