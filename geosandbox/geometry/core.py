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


# ============================================================================
# Выпуклая оболочка (Graham Scan)
# ============================================================================

def convex_hull(points: list[Point]) -> list[Point]:
    """
    Построение выпуклой оболочки методом Грэхема (Graham scan).
    
    Сложность: O(n log n)
    """
    unique = sorted(set(points))
    if len(unique) <= 2:
        return unique

    pivot = min(unique, key=lambda p: (p[1], p[0]))

    def polar_key(point: Point) -> tuple[float, float]:
        angle = math.atan2(point[1] - pivot[1], point[0] - pivot[0])
        dist = (point[0] - pivot[0]) ** 2 + (point[1] - pivot[1]) ** 2
        return (angle, dist)

    ordered = [pivot] + sorted((point for point in unique if point != pivot), key=polar_key)

    hull: list[Point] = []
    for point in ordered:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    return hull


# ============================================================================
# Триангуляция Делоне
# ============================================================================

def circumcircle_contains(a: Point, b: Point, c: Point, p: Point) -> bool:
    """Проверка, лежит ли точка p внутри описанной окружности треугольника abc."""
    ax, ay = a[0] - p[0], a[1] - p[1]
    bx, by = b[0] - p[0], b[1] - p[1]
    cx, cy = c[0] - p[0], c[1] - p[1]

    det = (
            (ax * ax + ay * ay) * (bx * cy - cx * by)
            - (bx * bx + by * by) * (ax * cy - cx * ay)
            + (cx * cx + cy * cy) * (ax * by - bx * ay)
    )

    orientation = cross(a, b, c)
    return det > 1e-9 if orientation > 0 else det < -1e-9


def delaunay(points: list[Point]) -> list[Triangle]:
    """
    Алгоритм триангуляции Делоне (инкрементальный).
    
    Сложность: O(n²) простая реализация, O(n log n) с оптимизациями
    """
    if len(points) < 3:
        return []

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    delta = max(max_x - min_x, max_y - min_y)
    mid_x = (min_x + max_x) * 0.5
    mid_y = (min_y + max_y) * 0.5

    work_points = points[:]
    super_a = (mid_x - 20 * delta, mid_y - delta)
    super_b = (mid_x, mid_y + 20 * delta)
    super_c = (mid_x + 20 * delta, mid_y - delta)
    super_indices = (len(work_points), len(work_points) + 1, len(work_points) + 2)
    work_points.extend([super_a, super_b, super_c])

    triangles: list[Triangle] = [super_indices]

    for new_point_idx in range(len(points)):
        new_point = points[new_point_idx]
        bad_triangles: list[Triangle] = []

        for tri in triangles:
            a_idx, b_idx, c_idx = tri
            a, b, c = work_points[a_idx], work_points[b_idx], work_points[c_idx]
            
            if circumcircle_contains(a, b, c, new_point):
                bad_triangles.append(tri)

        if not bad_triangles:
            continue

        polygon_edges: dict[Edge, int] = {}

        for tri in bad_triangles:
            a_idx, b_idx, c_idx = tri
            for edge in [Edge(a_idx, b_idx), Edge(b_idx, c_idx), Edge(c_idx, a_idx)]:
                normalized = edge.normalized()
                polygon_edges[normalized] = polygon_edges.get(normalized, 0) + 1

        boundary_edges = [edge for edge, count in polygon_edges.items() if count == 1]

        for tri in bad_triangles:
            triangles.remove(tri)

        for edge in boundary_edges:
            triangles.append((edge.a, edge.b, new_point_idx + len(points) - len(points)))

    return [
        tri for tri in triangles
        if all(idx < len(points) for idx in tri)
    ]
