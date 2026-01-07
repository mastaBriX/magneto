#!/bin/bash
#
# Setup script to install pre-commit hooks
#

set -e

echo "Setting up pre-commit hooks..."

# Check if pre-commit is installed
if command -v pre-commit >/dev/null 2>&1; then
    echo "Installing pre-commit hooks..."
    pre-commit install
    echo "Pre-commit hooks installed successfully!"
    echo ""
    echo "You can test the hooks with: pre-commit run --all-files"
else
    echo "pre-commit framework not found. Installing..."
    
    # Try to install with pip
    if command -v pip >/dev/null 2>&1; then
        pip install pre-commit
        pre-commit install
        echo "Pre-commit hooks installed successfully!"
    elif command -v uv >/dev/null 2>&1; then
        uv pip install pre-commit
        pre-commit install
        echo "Pre-commit hooks installed successfully!"
    else
        echo "Error: Could not find pip or uv to install pre-commit"
        echo "Please install pre-commit manually: pip install pre-commit"
        exit 1
    fi
fi

echo ""
echo "Setup complete! Pre-commit hooks will now run automatically on git commit."

