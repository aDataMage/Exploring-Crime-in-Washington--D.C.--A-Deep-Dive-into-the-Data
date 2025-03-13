import subprocess
import sys

# List of required packages
required_packages = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "folium",
    "geopandas",
    "datetime",
    "openpyxl",
]


# Function to install missing packages
def install_missing_packages(packages):
    for package in packages:
        try:
            __import__(package)  # Try to import the package
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Run package installation
install_missing_packages(required_packages)


print("All packages are installed and imported successfully!")
