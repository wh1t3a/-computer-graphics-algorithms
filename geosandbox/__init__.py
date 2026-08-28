"""
Computational Geometry Sandbox - Interactive Algorithms Library

A comprehensive Python library for computational geometry algorithms,
including convex hulls, Delaunay triangulation, and curve rendering.
"""

__version__ = "1.0.2"
__author__ = "Computer Graphics Course"
__license__ = "MIT"

from . import geometry
from . import curves
from . import physics
from . import image

__all__ = [
    "geometry",
    "curves",
    "physics",
    "image",
]
