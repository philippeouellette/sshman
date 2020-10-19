try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

config = {
    "keywords": "ssh sessions manager",
    "author": "Philippe Ouellette & Olivier Granger-Hotte",
    "description": "A simple ssh sessions manager",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "http://192.168.100.23:3000/ouellp/sshman",
    "download_url": "http://192.168.100.23:3000/ouellp/sshman",
    "author_email": "philippeouellette@protonmail.com",
    "version": "2.0.5",
    "install_requires": ["bullet"],
    "packages": ["sshman"],
    "entry_points": {
        "console_scripts": ['sshman = sshman:main']
    },
    "name": "sshman",
    "classifiers": [
        "Programming Language :: Python :: 3.8",
    ],
}

setup(**config)