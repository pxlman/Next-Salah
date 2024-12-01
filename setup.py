from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="next-salah",
    version="0.2.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "next-salah=src.cli:main",
        ],
    },
    description="A python program to print out the next salah comming and the remaining time to it.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pxlman/next-salah",
    python_requires=">=3.6",
) 