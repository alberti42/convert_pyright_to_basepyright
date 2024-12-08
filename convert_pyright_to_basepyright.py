#! python3

import json5
import json
import sys
from pathlib import Path

def pyright_to_basedpyright(file_path):
    # Read the .sublime-project file
    try:
        with open(file_path, 'r') as f:
            data = json5.load(f)  # Use json5 for permissive parsing
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading file {file_path}: {e}")
        return
    
    # Navigate to the settings section
    settings = data.get("settings", {}).get("LSP", {}).get("LSP-pyright", {})
    
    if not settings:
        print(f"No LSP-pyright settings found in {file_path}")
        return

    # Extract old settings
    pyright_settings = settings.get("settings", {})
    
    # Convert to basedpyright settings
    basedpyright_settings = {
        "venvStrategies": ["env_var_virtual_env"],
        "venv": pyright_settings.get("python.venvPath", "").split("/")[-1],  # Extract venv name
        "venvPath": pyright_settings.get("python.venvPath", ""),
        "python.pythonPath": pyright_settings.get("python.pythonPath", ""),
        "basedpyright.analysis.extraPaths": pyright_settings.get("python.analysis.extraPaths", []),
        "basedpyright.analysis.typeCheckingMode": pyright_settings.get("python.analysis.typeCheckingMode", "standard"),
        "basedpyright.analysis.reportOptionalSubscript": pyright_settings.get("python.analysis.reportOptionalSubscript", "error"),
    }

    # Replace LSP-pyright with LSP-basedpyright
    data["settings"]["LSP"].pop("LSP-pyright", None)
    data["settings"]["LSP"]["LSP-basedpyright"] = {"settings": basedpyright_settings}
    
    # Save the updated file
    try:
        with open(file_path, 'w') as f:
            # Use json.dumps for standard JSON formatting when saving
            json.dump(data, f, indent=4)
        print(f"File {file_path} updated successfully.")
    except IOError as e:
        print(f"Error writing file {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_pyright_to_basedpyright.py <path_to_sublime_project>")
        sys.exit(1)
    
    project_file = sys.argv[1]
    if not Path(project_file).is_file():
        print(f"File {project_file} does not exist.")
        sys.exit(1)
    
    pyright_to_basedpyright(project_file)
