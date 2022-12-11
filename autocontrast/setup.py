from setuptools import setup, find_packages
import src

setup(
    name="autocontrast",
    version=src.__version__,
    author="VS",
    packages=find_packages(),
    install_requires=["opencv-python", "numpy"]
)