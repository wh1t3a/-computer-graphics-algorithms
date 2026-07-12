"""Computational Geometry Module"""

from .core import (
    Point,
    Triangle,
    Edge,
    cross,
    polygon_area,
    point_in_polygon,
    segments_intersect,
    convex_hull,
)

__all__ = [
    "Point",
    "Triangle",
    "Edge",
    "cross",
    "polygon_area",
    "point_in_polygon",
    "segments_intersect",
    "convex_hull",
]
