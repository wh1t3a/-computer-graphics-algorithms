#!/usr/bin/env python3
"""Setup configuration for geosandbox package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geosandbox",
    version="1.0.0",
    author="Computer Graphics Course",
    description="Interactive sandbox for computational geometry algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wh1t3a/-computer-graphics-algorithms",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pygame>=2.1.0",
        "numpy>=1.21.0",
        "opencv-python>=4.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "pylint>=2.8",
        ],
    },
)
