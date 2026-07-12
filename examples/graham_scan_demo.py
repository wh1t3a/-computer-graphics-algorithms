"""
Example: Graham Scan Convex Hull
Demonstrates the Graham Scan algorithm for computing convex hulls.
"""

import random
from geosandbox.geometry import convex_hull, Point


def example_basic():
    """Simple example with predefined points."""
    points: list[Point] = [
        (0, 0), (1, 1), (2, 0), (1, 2), (1.5, 0.5)
    ]
    
    hull = convex_hull(points)
    print("Input points:", points)
    print("Convex hull (CCW):", hull)
    print(f"Hull size: {len(hull)} vertices")


def example_random():
    """Example with random points."""
    random.seed(42)
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(20)]
    
    hull = convex_hull(points)
    print(f"\nGenerated {len(points)} random points")
    print(f"Convex hull has {len(hull)} vertices")
    
    # Calculate hull perimeter
    perimeter = 0
    for i in range(len(hull)):
        p1 = hull[i]
        p2 = hull[(i + 1) % len(hull)]
        dist = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
        perimeter += dist
    
    print(f"Hull perimeter: {perimeter:.2f}")


def example_timing():
    """Compare timing for different input sizes."""
    import time
    
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        points = [
            (random.uniform(0, 1000), random.uniform(0, 1000))
            for _ in range(size)
        ]
        
        start = time.time()
        hull = convex_hull(points)
        elapsed = time.time() - start
        
        print(f"\nn={size}: {elapsed*1000:.2f} ms → {len(hull)} hull vertices")


if __name__ == "__main__":
    print("=" * 60)
    print("GRAHAM SCAN CONVEX HULL EXAMPLES")
    print("=" * 60)
    
    example_basic()
    example_random()
    example_timing()
    
    print("\n" + "=" * 60)
    print("✓ Examples completed")
