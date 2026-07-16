"""
Example: Delaunay Triangulation
Demonstrates Delaunay triangulation with visualization hints.
"""

import random
from geosandbox.geometry import delaunay, polygon_area, Point


def example_basic():
    """Simple Delaunay triangulation."""
    points: list[Point] = [
        (0, 0), (10, 0), (10, 10), (0, 10),  # Square corners
        (5, 5)  # Center point
    ]
    
    triangles = delaunay(points)
    print("Input points:", points)
    print(f"Triangles ({len(triangles)}):", triangles)


def example_grid():
    """Regular grid triangulation."""
    points: list[Point] = []
    size = 5
    spacing = 20
    
    for i in range(size):
        for j in range(size):
            points.append((i * spacing, j * spacing))
    
    triangles = delaunay(points)
    print(f"\nGrid {size}x{size}: {len(points)} points → {len(triangles)} triangles")


def example_random():
    """Random point cloud triangulation."""
    random.seed(42)
    n = 30
    points = [
        (random.uniform(0, 100), random.uniform(0, 100))
        for _ in range(n)
    ]
    
    triangles = delaunay(points)
    
    # Calculate total area
    total_area = 0
    for tri in triangles:
        i, j, k = tri
        p1, p2, p3 = points[i], points[j], points[k]
        # Triangle area using cross product
        area = 0.5 * abs(
            (p2[0] - p1[0]) * (p3[1] - p1[1]) - 
            (p3[0] - p1[0]) * (p2[1] - p1[1])
        )
        total_area += area
    
    print(f"\nRandom {n} points: {len(triangles)} triangles")
    print(f"Total triangulated area: {total_area:.2f}")


def example_properties():
    """Demonstrate Delaunay properties."""
    points: list[Point] = [
        (0, 0), (100, 0), (100, 100), (0, 100),
        (25, 25), (75, 75), (25, 75), (75, 25)
    ]
    
    triangles = delaunay(points)
    
    print(f"\n{len(points)} points → {len(triangles)} triangles")
    print("\nDelaunay Properties:")
    print("✓ Maximizes minimum angle of triangles")
    print("✓ No point lies inside circumcircle of any triangle")
    print("✓ Empty circumcircle property ensures numerical stability")


if __name__ == "__main__":
    print("=" * 60)
    print("DELAUNAY TRIANGULATION EXAMPLES")
    print("=" * 60)
    
    example_basic()
    example_grid()
    example_random()
    example_properties()
    
    print("\n" + "=" * 60)
    print("✓ Examples completed")
    print("\nNote: For visualization, use pygame or matplotlib")
