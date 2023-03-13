from setuptools import setup, find_packages

setup(
    name="jarvis",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "logging",
        "flask"
    ]
)