find . -name __pycache__ -type d -exec rm -rf {} \;
rm -rf .pytest_cache
rm -rf .venv

# George's clean up pycache script