# Magneto

A powerful and user-friendly command-line tool for batch converting torrent files (.torrent) to magnet links.

## ✨ Features

- 🚀 **Batch Processing** - Support single file or entire folder batch conversion
- 🔍 **Recursive Search** - Recursively search for torrent files in subdirectories
- 🎨 **Beautiful Output** - Colored terminal output with clear progress display
- 📝 **Multiple Formats** - Support full format, links only, and JSON format output
- 🔗 **Tracker Support** - Optionally include tracker information in magnet links
- 📊 **Detailed Statistics** - Display processing progress and success/failure statistics
- 🎯 **Flexible Configuration** - Rich command-line argument options

## 📦 Installation

### Using uv (Recommended)

This project uses `pyproject.toml` for dependency management and is fully compatible with `uv`.

```bash
# Install uv (if not already installed)
# Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Linux/Mac: curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies and install project (development mode)
uv sync

# Run directly (no installation needed, uv manages environment automatically)
uv run magneto file.torrent
uv run magneto folder/ -r -v

# Install to current environment
uv pip install -e .

# Install development dependencies (if configured)
uv sync --extra dev

# View project information
uv tree
```

### Using pip

```bash
# Install from source (pip automatically reads pyproject.toml)
pip install -e .

# Or install dependencies directly
pip install bencode.py colorama
```

## 🚀 Usage

### Basic Usage

```bash
# Convert a single torrent file
magneto file.torrent

# Convert all torrent files in a folder
magneto folder/

# Specify output file
magneto folder/ -o output.txt
```

### Advanced Usage

```bash
# Recursively search subdirectories
magneto folder/ -r

# Output JSON format
magneto folder/ -f json

# Output magnet links only (no other information)
magneto folder/ -f links_only

# Include tracker information in magnet links
magneto folder/ --include-trackers

# Show detailed information
magneto folder/ -v

# Quiet mode (only show errors)
magneto folder/ -q

# Disable colored output
magneto folder/ --no-colors

# Print results to stdout instead of saving to file
magneto folder/ --stdout
magneto folder/ --stdout -f links_only  # Print only magnet links
magneto folder/ --stdout -f json        # Print JSON format
```

### View Help

```bash
magneto --help
magneto -h
```

### View Version

```bash
magneto --version
```

## 📋 Command-Line Arguments

### Positional Arguments

- `input` - Input torrent file or folder path containing torrent files

### Output Options

- `-o, --output FILE` - Specify output file path (default: magnet_links.txt in input directory)
- `-f, --format {full,links_only,json}` - Output format (default: full)
  - `full` - Full format, includes file information, magnet links, Info Hash, etc.
  - `links_only` - Magnet link list only
  - `json` - JSON format output
- `--stdout` - Print results to stdout instead of saving to file

### Search Options

- `-r, --recursive` - Recursively search for torrent files in subdirectories
- `--case-sensitive` - Case-sensitive search for file extensions

### Conversion Options

- `--include-trackers` - Include tracker information in magnet links

### Display Options

- `-v, --verbose` - Show verbose output information
- `-q, --quiet` - Quiet mode, only show error messages
- `--no-colors` - Disable colored output

### Other Options

- `-h, --help` - Show help information and exit
- `--version` - Show version information and exit

## 📁 Output Format Examples

### Full Format

```
================================================================================
Torrent to Magnet Link Conversion Results
================================================================================

File: example.torrent
Magnet Link: magnet:?xt=urn:btih:ABC123...&dn=Example
Info Hash: ABC123...
Name: Example
Trackers: 3 found
--------------------------------------------------------------------------------

================================================================================
Magnet Link List (Links Only)
================================================================================

magnet:?xt=urn:btih:ABC123...&dn=Example
```

### JSON Format

```json
[
  {
    "file": "example.torrent",
    "magnet": "magnet:?xt=urn:btih:ABC123...&dn=Example",
    "info_hash": "ABC123...",
    "name": "Example",
    "trackers": ["http://tracker1.example.com", "http://tracker2.example.com"]
  }
]
```

## 🧪 Testing

The project includes comprehensive unit tests using pytest with mock torrent files.

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=magneto --cov-report=html

# Run specific test file
pytest tests/test_core.py

# Run tests in verbose mode
pytest -v

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration
```

## 🔧 Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality and run tests before committing.

### Setup

```bash
# Install pre-commit hooks (Linux/Mac)
bash scripts/setup-hooks.sh

# Install pre-commit hooks (Windows)
powershell scripts/setup-hooks.ps1

# Or manually
pip install pre-commit
pre-commit install
```

### Usage

Pre-commit hooks will automatically run on `git commit`. You can also run them manually:

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run pytest

# Skip hooks (not recommended)
git commit --no-verify
```

### Hooks Included

- **pytest** - Runs all tests before commit
- **black** - Auto-formats Python code
- **ruff** - Lints and fixes Python code
- **File checks** - Checks for trailing whitespace, large files, etc.

## 🏗️ Project Structure

```
magneto/
├── magneto/           # Main package
│   ├── __init__.py   # Package initialization
│   ├── core.py       # Core conversion logic
│   ├── parser.py     # Command-line argument parsing
│   ├── ui.py         # User interface and output
│   └── utils.py      # Utility functions
├── main.py           # Program entry point
├── tests/            # Test suite
│   ├── __init__.py
│   ├── conftest.py   # Pytest fixtures and configuration
│   ├── test_core.py   # Core module tests
│   ├── test_utils.py # Utility function tests
│   ├── test_parser.py # Parser tests
│   ├── test_ui.py    # UI tests
│   └── test_integration.py # Integration tests
├── pyproject.toml    # Project configuration (for uv/pip)
└── README.md         # Documentation
```

> **Note**: This project uses `pyproject.toml` for dependency and configuration management. `uv` is recommended, but pip also fully supports `pyproject.toml`.

## 🔧 Dependencies

- Python 3.7+
- bencode.py >= 4.0.0
- colorama >= 0.4.0 (optional, for Windows color support)

## 📝 License

MIT License

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📮 Feedback

If you have any questions or suggestions, please provide feedback through Issues.
