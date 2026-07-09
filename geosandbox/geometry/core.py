"""
Библиотека геометрических алгоритмов для 2D и 3D данных.
Содержит базовые алгоритмы вычислительной геометрии:
- Проверка принадлежности точки полигону (ray casting)
- Пересечение отрезков
- Площадь полигона
- Выпуклая оболочка (Graham scan)
- Триангуляция Делоне
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# Типы данных для удобства
Point = tuple[float, float]  # Точка на плоскости (x, y)
Triangle = tuple[int, int, int]  # Треугольник как три индекса точек


@dataclass(frozen=True)
class Edge:
    """Ребро графа (неориентированное). Используется в триангуляции."""
    a: int  # Индекс первой вершины
    b: int  # Индекс второй вершины

    def normalized(self) -> "Edge":
        """Нормализует ребро - гарантирует, что a < b."""
        return Edge(self.a, self.b) if self.a < self.b else Edge(self.b, self.a)


# ============================================================================
# Базовые геометрические операции
# ============================================================================

def cross(a: Point, b: Point, c: Point) -> float:
    """
    Векторное произведение (2D cross product).

    Возвращает ориентацию точки C относительно вектора AB:
    > 0 - C слева (CCW)
    < 0 - C справа (CW)
    = 0 - коллинеарны
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def polygon_area(points: list[Point]) -> float:
    """Площадь полигона по формуле шнурка (Shoelace)."""
    area = 0.0
    for i, p in enumerate(points):
        q = points[(i + 1) % len(points)]
        area += p[0] * q[1] - q[0] * p[1]
    return abs(area) * 0.5


def point_in_polygon(point: Point, polygon: list[Point]) -> bool:
    """Проверка принадлежности точки полигону (Ray Casting)."""
    x, y = point
    inside = False
    j = len(polygon) - 1

    for i, pi in enumerate(polygon):
        pj = polygon[j]
        crosses_ray = (pi[1] > y) != (pj[1] > y)

        if crosses_ray:
            x_intersection = (pj[0] - pi[0]) * (y - pi[1]) / (pj[1] - pi[1]) + pi[0]
            if x < x_intersection:
                inside = not inside
        j = i

    return inside


def on_segment(a: Point, b: Point, p: Point) -> bool:
    """Проверка, лежит ли точка p на отрезке ab."""
    return (
            min(a[0], b[0]) - 1e-9 <= p[0] <= max(a[0], b[0]) + 1e-9
            and min(a[1], b[1]) - 1e-9 <= p[1] <= max(a[1], b[1]) + 1e-9
            and abs(cross(a, b, p)) < 1e-9
    )


def segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    """Проверка пересечения двух отрезков AB и CD."""
    c1 = cross(a, b, c)
    c2 = cross(a, b, d)
    c3 = cross(c, d, a)
    c4 = cross(c, d, b)

    if c1 * c2 < 0 and c3 * c4 < 0:
        return True

    return on_segment(a, b, c) or on_segment(a, b, d) or on_segment(c, d, a) or on_segment(c, d, b)
