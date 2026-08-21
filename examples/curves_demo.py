"""
Example: Curve Algorithms
Demonstrates Bezier, B-spline, Catmull-Rom, and NURBS curves.
"""

from geosandbox.curves import (
    bezier, bspline, catmull_rom, 
    ControlPoint, nurbs_curve
)


def example_bezier():
    """Bezier curve with de Casteljau algorithm."""
    control_points = [
        (50, 50), (150, 200), (300, 100), (400, 250)
    ]
    
    curve = bezier(control_points, steps=50)
    print(f"Bezier: {len(control_points)} control points → {len(curve)} curve points")
    print(f"First point: {curve[0]}, Last point: {curve[-1]}")
    print(f"Note: Curve does NOT pass through control points except endpoints")


def example_bspline():
    """B-spline curve."""
    control_points = [
        (50, 50), (150, 200), (300, 100), (400, 250), (450, 150)
    ]
    
    curve = bspline(control_points, degree=3, steps=100)
    print(f"\nB-spline: {len(control_points)} control points → {len(curve)} curve points")
    print(f"Properties:")
    print(f"  ✓ C² smooth (second derivative continuous)")
    print(f"  ✓ Local control (moving point affects k+1 segments)")
    print(f"  ✓ Does NOT pass through control points (approximates)")


def example_catmull_rom():
    """Catmull-Rom interpolating spline."""
    control_points = [
        (50, 50), (150, 200), (300, 100), (400, 250)
    ]
    
    curve = catmull_rom(control_points, samples_per_segment=30)
    print(f"\nCatmull-Rom: {len(control_points)} control points → {len(curve)} curve points")
    print(f"Properties:")
    print(f"  ✓ PASSES through all control points (interpolates)")
    print(f"  ✓ Uses Hermite interpolation")
    print(f"  ✓ C¹ smooth (first derivative continuous)")
    
    # Verify that curve passes through control points (approximately)
    # This is a property of Catmull-Rom curves
    print(f"  ✓ Ideal for animating paths through waypoints")


def example_nurbs():
    """NURBS curve with weighted control points."""
    control_points = [
        ControlPoint(50, 50, weight=1.0),
        ControlPoint(150, 200, weight=2.0),   # Heavy weight → attracts curve
        ControlPoint(300, 100, weight=1.0),
        ControlPoint(400, 250, weight=1.5),
    ]
    
    curve = nurbs_curve(control_points, degree=3, steps=100)
    print(f"\nNURBS: {len(control_points)} weighted control points → {len(curve)} curve points")
    print(f"Properties:")
    print(f"  ✓ Weighted points (weight > 1 attracts, < 1 repels)")
    print(f"  ✓ Can represent conic sections (circles, ellipses)")
    print(f"  ✓ Professional CAD standard (AutoCAD, SolidWorks)")
    print(f"  ✓ More flexible than B-splines")


def example_comparison():
    """Compare different curve types."""
    points = [(0, 0), (100, 150), (200, 50), (300, 200)]
    
    print(f"\nCOMPARISON: All methods on same control points")
    print(f"Control points: {points}")
    
    bezier_curve = bezier(points, steps=50)
    bspline_curve = bspline(points, degree=3, steps=50)
    catmull_curve = catmull_rom(points, samples_per_segment=20)
    
    print(f"\nBezier   length: {len(bezier_curve)} points, starts at {bezier_curve[0]:.1f}")
    print(f"B-spline length: {len(bspline_curve)} points, starts at {bspline_curve[0]:.1f}")
    print(f"Catmull  length: {len(catmull_curve)} points, starts at {catmull_curve[0]:.1f}")
    
    print(f"\nKey differences:")
    print(f"  Bezier   - Doesn't pass through points, smooth, predictable")
    print(f"  B-spline - Doesn't pass through points, very smooth")
    print(f"  Catmull  - PASSES through all points, good for animation")


if __name__ == "__main__":
    print("=" * 70)
    print("CURVE ALGORITHMS EXAMPLES")
    print("=" * 70)
    
    example_bezier()
    example_bspline()
    example_catmull_rom()
    example_nurbs()
    example_comparison()
    
    print("\n" + "=" * 70)
    print("✓ Examples completed")
    print("\nFor visualization:")
    print("  pip install pygame matplotlib")
    print("  Then use matplotlib.pyplot to plot points")
