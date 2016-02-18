import sys
from setuptools import setup, find_packages

wargs = {}
requires = ['apache-libcloud>=1.0.0-pre1']

# python 2.7 hackery
if sys.version_info <= (3, 0):
    requires.extend(
        ["future"]
    )

setup(
    author="Jeff Dunham",
    author_email="",
    description="Base description, say what your package does here",
    url="https://www.dimensiondata.com/",
    name="DDDisasterRecovery.py",
    version="0.1.0",
    packages=find_packages(exclude=["contrib", "docs", "tests*", "tasks", "venv"]),
    install_requires=requires,
    setup_requires=[],
)
