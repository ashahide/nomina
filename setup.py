from setuptools import setup, find_packages

setup(
    name="nomina",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    entry_points={
        'console_scripts': [
            'nomina=src.main:main',  # Replace with your module and function
        ],
    },
)