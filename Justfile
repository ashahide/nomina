## Set shell
set shell := ["bash", "-cu"]


#--------------------------------------------
# Setup and Installation
#--------------------------------------------

# Install locally with poetry
install-local:
    poetry install

# Update local version with poetry
update-local:
    poetry update

# Build local version with poetry
build-local:
    poetry build

# Install globally with pipx
install-global:
    pipx install . --force



#--------------------------------------------
# Usage and Tests
#--------------------------------------------

# Run locally with poetry
run-local *names:
    poetry run nomina {{names}}

run-global *names:
    nomina {{names}}

# utilities

# Default option without flags. Same as just help
default: help

# Get a list of commands
help:
    @just -l
