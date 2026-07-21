"""Bezier curves using de Casteljau algorithm."""

from __future__ import annotations

import math
from dataclasses import dataclass

Point = tuple[float, float]


@dataclass
class ControlPoint:
    """Control point with coordinates and weight coefficient."""
    x: float
    y: float
    weight: float = 1.0

    @property
    def pos(self) -> Point:
        """Returns coordinates as a tuple (x, y)."""
        return self.x, self.y


def lerp_point(a: Point, b: Point, t: float) -> Point:
    """Linear interpolation between two points."""
    return a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t


def distance(a: Point, b: Point) -> float:
    """Euclidean distance between two points."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def bezier(points: list[Point], steps: int = 180) -> list[Point]:
    """
    Bezier curve construction using de Casteljau algorithm.
    
    Complexity: O(n*steps) where n is number of control points
    """
    if len(points) < 2:
        return points[:]

    curve: list[Point] = []
    for i in range(steps + 1):
        t = i / steps
        layer = points[:]

        while len(layer) > 1:
            layer = [lerp_point(layer[j], layer[j + 1], t) for j in range(len(layer) - 1)]

        curve.append(layer[0])

    return curve
