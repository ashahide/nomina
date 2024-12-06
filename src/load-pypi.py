from pypi_simple import PyPISimple
import json



pypi = PyPISimple()

# Get all packages
packages = pypi.list_packages()

# Save package names to a json
with open('pypi-packages.json', 'w') as f:
    json.dump(packages, f)