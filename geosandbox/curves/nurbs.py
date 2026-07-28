"""NURBS curves (Non-Uniform Rational B-Spline)."""

from __future__ import annotations

from .bezier import ControlPoint
from .bspline import open_uniform_knots, basis

Point = tuple[float, float]


def nurbs_curve(points: list[ControlPoint], degree: int = 3, steps: int = 240) -> list[Point]:
    """
    NURBS curve construction with weighted control points.
    
    Formula: C(t) = (Σ wᵢ * Pᵢ * Nᵢ(t)) / (Σ wᵢ * Nᵢ(t))
    
    Complexity: O(n*k*steps) with basis function caching
    """
    if len(points) < 2:
        return [p.pos for p in points]

    degree = min(degree, len(points) - 1)
    knots = open_uniform_knots(len(points), degree)

    curve: list[Point] = []
    for step in range(steps + 1):
        t = step / steps
        x = 0.0
        y = 0.0
        denom = 0.0

        for i, point in enumerate(points):
            b = basis(i, degree, t, knots) * point.weight
            x += point.x * b
            y += point.y * b
            denom += b

        if denom:
            curve.append((x / denom, y / denom))

    return curve
