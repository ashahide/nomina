## Set shell
set shell := ["bash", "-cu"]


#--------------------------------------------
# Setup and Installation
#--------------------------------------------

# Install locally with poetry
install-local:
    poetry install

# Install globally with pipx
install-global:
    pipx install . --force

# Run total installation
install: install-local update-local

# Update local version with poetry
update-local:
    poetry update

# Build local version with poetry
build:
    poetry build

# Clean and uninstall global environment
clean-global:
    pipx uninstall nomina

# Clean local environment
clean-local:
    uv pip uninstall nomina
    rm -f .venv/bin/nomina

# Total clean (local and global)
clean: clean-local clean-global


#--------------------------------------------
# Usage and Tests
#--------------------------------------------

# Run locally with poetry
run-local *names:
    poetry run nomina {{names}}

# Run globaly if it's installed
run-global *names:
    nomina {{names}}

tests:
    pytest > logs/just.log

# utilities

# Default option without flags. Same as just help
default: help

# Get a list of commands
help:
    @just -l
