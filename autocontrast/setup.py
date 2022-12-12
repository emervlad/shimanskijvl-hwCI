from setuptools import setup, find_packages
import aucon

setup(
    name="cvutils",
    version=aucon.__version__,
    author="VS",
    packages=find_packages(),
    install_requires=["opencv-python", "numpy"]
)