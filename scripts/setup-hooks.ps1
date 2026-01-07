# PowerShell script to setup pre-commit hooks
# For Windows users

Write-Host "Setting up pre-commit hooks..." -ForegroundColor Yellow

# Check if pre-commit is installed
if (Get-Command pre-commit -ErrorAction SilentlyContinue) {
    Write-Host "Installing pre-commit hooks..." -ForegroundColor Green
    pre-commit install
    Write-Host "Pre-commit hooks installed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can test the hooks with: pre-commit run --all-files" -ForegroundColor Cyan
} else {
    Write-Host "pre-commit framework not found. Installing..." -ForegroundColor Yellow
    
    # Try to install with pip
    if (Get-Command pip -ErrorAction SilentlyContinue) {
        pip install pre-commit
        pre-commit install
        Write-Host "Pre-commit hooks installed successfully!" -ForegroundColor Green
    } elseif (Get-Command uv -ErrorAction SilentlyContinue) {
        uv pip install pre-commit
        pre-commit install
        Write-Host "Pre-commit hooks installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "Error: Could not find pip or uv to install pre-commit" -ForegroundColor Red
        Write-Host "Please install pre-commit manually: pip install pre-commit" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host ""
Write-Host "Setup complete! Pre-commit hooks will now run automatically on git commit." -ForegroundColor Green

