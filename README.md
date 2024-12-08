# Sublime Project Pyright to Basedpyright Converter

This utility converts Sublime Text `.sublime-project` files configured for `LSP-pyright` to use `LSP-basedpyright`. `LSP-basedpyright` extends the functionality of `LSP-pyright` by providing enhanced support for Python projects in Sublime Text.

## Features

- Automatically converts `LSP-pyright` settings to `LSP-basedpyright` settings.
- Extracts and maps `LSP-pyright` configurations (e.g., `venvPath`, `pythonPath`) to the appropriate `LSP-basedpyright` settings.
- Processes multiple project files in bulk using standard Linux commands like `find`.

## Requirements

- Python 3.8+
- `json5` library (`pip install json5`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pyright-to-basedpyright.git
    cd pyright-to-basedpyright
    ```
2. Install the required Python library:
    ```bash
    pip install json5
    ```

## Usage

### Convert a Single Project File

Run the script with the path to a `.sublime-project` file:
```bash
python convert_pyright_to_basedpyright.py <path_to_sublime_project>
```

For example:
```bash
python convert_pyright_to_basedpyright.py ~/Projects/myproject.sublime-project
```

### Batch Conversion

You can use `find` to process all `.sublime-project` files under a specific directory. Replace `<PROJECTS_DIR>` with the directory path containing your Sublime Text projects:
```bash
find <PROJECTS_DIR> -name '*.sublime-project' -exec python3 convert_pyright_to_basedpyright.py "{}" \;
```

For example:
```bash
find ~/Projects -name '*.sublime-project' -exec python3 convert_pyright_to_basedpyright.py "{}" \;
```

### What the Script Does
- Reads the `.sublime-project` file using `json5` for permissive parsing.
- Extracts existing `LSP-pyright` settings.
- Converts the settings to the `LSP-basedpyright` format.
- Saves the updated `.sublime-project` file.

## Example

### Before Conversion

```json
{
    "settings": {
        "LSP": {
            "LSP-pyright": {
                "settings": {
                    "python.venvPath": "/path/to/venv",
                    "python.pythonPath": "/path/to/venv/bin/python",
                    "python.analysis.extraPaths": ["src"],
                    "python.analysis.typeCheckingMode": "strict"
                }
            }
        }
    }
}
```

### After Conversion

```json
{
    "settings": {
        "LSP": {
            "LSP-basedpyright": {
                "settings": {
                    "venvStrategies": ["env_var_virtual_env"],
                    "venv": "venv",
                    "venvPath": "/path/to/venv",
                    "python.pythonPath": "/path/to/venv/bin/python",
                    "basedpyright.analysis.extraPaths": ["src"],
                    "basedpyright.analysis.typeCheckingMode": "strict",
                    "basedpyright.analysis.reportOptionalSubscript": "error"
                }
            }
        }
    }
}
```

## Known Limitations

- The script assumes `LSP-pyright` settings are located under `settings.LSP.LSP-pyright`. If your project file structure differs, the script might not work as intended.
- Ensure you back up your project files before running the script in batch mode.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- **Author:** Andrea Alberti
- **GitHub Profile:** [alberti42](https://github.com/alberti42)
- **Donations:** [![Buy Me a Coffee](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-orange)](https://buymeacoffee.com/alberti)

Feel free to contribute to the development of this plugin or report any issues in the [GitHub repository](https://github.com/alberti42/convert_pyright_to_basepyright/issues).
