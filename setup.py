from setuptools import setup

__version__ = "v1.1.0"

with open("requirements.txt", "r") as f:
    req_list = f.read().split("\n")[:-1]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name                          = "PyClash",
    version                       = __version__,
    description                   = "API Wrapper for Clash of Clans",
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/1Doomdie1/PyClash",
    author                        = "Todoran Horia",
    license                       = "GPL-3.0",
    classifiers                   = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires              = req_list,
    extras_require                = {
        "dev": ["pytest", "twine"],
    },
    python_requires               = ">=3.10"
)