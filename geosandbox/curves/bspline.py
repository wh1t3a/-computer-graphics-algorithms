"""B-spline curves using Cox-de Boor recursion."""

from __future__ import annotations

Point = tuple[float, float]


def open_uniform_knots(count: int, degree: int) -> list[float]:
    """Create knot vector for uniform B-spline."""
    knot_count = count + degree + 1
    inner = knot_count - 2 * (degree + 1)

    knots = [0.0] * (degree + 1)

    if inner > 0:
        knots.extend(i / (inner + 1) for i in range(1, inner + 1))

    knots.extend([1.0] * (degree + 1))
    return knots


def basis(i: int, degree: int, t: float, knots: list[float]) -> float:
    """Cox-de Boor recursion for B-spline basis functions."""
    if degree == 0:
        if knots[i] <= t < knots[i + 1] or (t == 1.0 and knots[i + 1] == 1.0):
            return 1.0
        return 0.0

    left_den = knots[i + degree] - knots[i]
    right_den = knots[i + degree + 1] - knots[i + 1]

    left = 0.0
    right = 0.0

    if left_den:
        left = (t - knots[i]) / left_den * basis(i, degree - 1, t, knots)

    if right_den:
        right = (knots[i + degree + 1] - t) / right_den * basis(i + 1, degree - 1, t, knots)

    return left + right


def bspline(points: list[Point], degree: int = 3, steps: int = 220) -> list[Point]:
    """
    B-spline curve construction.
    
    Complexity: O(n*k*steps) where k is number of basis functions
    """
    if len(points) < 2:
        return points[:]

    degree = min(degree, len(points) - 1)
    knots = open_uniform_knots(len(points), degree)

    curve: list[Point] = []
    for step in range(steps + 1):
        t = step / steps
        x = 0.0
        y = 0.0

        for i, point in enumerate(points):
            b = basis(i, degree, t, knots)
            x += point[0] * b
            y += point[1] * b

        curve.append((x, y))

    return curve


def catmull_rom(points: list[Point], samples_per_segment: int = 28) -> list[Point]:
    """
    Catmull-Rom interpolating spline.
    
    Complexity: O(n*samples) - passes through all control points
    """
    if len(points) < 2:
        return points[:]

    padded = [points[0], *points, points[-1]]
    curve: list[Point] = []

    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i - 1], padded[i], padded[i + 1], padded[i + 2]

        for s in range(samples_per_segment):
            t = s / samples_per_segment
            t2 = t * t
            t3 = t2 * t

            x = 0.5 * (
                    2 * p1[0]
                    + (-p0[0] + p2[0]) * t
                    + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                    + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3
            )
            y = 0.5 * (
                    2 * p1[1]
                    + (-p0[1] + p2[1]) * t
                    + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                    + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3
            )
            curve.append((x, y))

    curve.append(points[-1])
    return curve
