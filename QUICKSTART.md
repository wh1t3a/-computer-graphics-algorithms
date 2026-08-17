# Quick Start Guide

## Installation

### From PyPI (coming soon)
```bash
pip install geosandbox
```

### From Source
```bash
git clone https://github.com/wh1t3a/-computer-graphics-algorithms.git
cd computational-geometry-sandbox
pip install -e .
```

## Running Examples

```bash
# All examples are in the examples/ directory
cd examples

python graham_scan_demo.py
python delaunay_mesh.py
python curves_demo.py
python particle_effects.py
```

## Simple Script

```python
from geosandbox.geometry import convex_hull, delaunay, Point

# Generate some points
points: list[Point] = [
    (0, 0), (10, 0), (10, 10), (0, 10), (5, 5)
]

# Compute convex hull
hull = convex_hull(points)
print("Hull:", hull)

# Compute Delaunay triangulation
triangles = delaunay(points)
print("Triangles:", triangles)
```

## Common Tasks

### Task: Find Convex Hull
```python
from geosandbox.geometry import convex_hull

points = [(x, y) for x, y in your_points]
hull = convex_hull(points)
# Result: list of points in CCW order
```

### Task: Triangulate Mesh
```python
from geosandbox.geometry import delaunay

points = [(x, y) for x, y in your_points]
triangles = delaunay(points)
# Result: list of (i, j, k) vertex indices
```

### Task: Draw Smooth Curve
```python
from geosandbox.curves import bezier, bspline, catmull_rom

control_points = [(x, y) for x, y in your_points]

# Choose one:
curve = bezier(control_points)         # Doesn't pass through points
curve = bspline(control_points)        # Smooth approximation
curve = catmull_rom(control_points)    # Passes through all points
```

### Task: Animate with Particles
```python
from geosandbox.physics import ParticleSystem, Particle, Vec3

system = ParticleSystem()

for i in range(num_particles):
    p = Particle(
        pos=Vec3(x, y, z),
        vel=Vec3(vx, vy, vz),
        acc=Vec3(0, gravity, 0),
        life=2.0,
        age=0,
        start_color=(r, g, b, a),
        end_color=(r, g, b, 0),
        start_size=10,
        end_size=2,
    )
    system.add(p)

# In your game loop:
system.update(dt)
```

## Troubleshooting

### ImportError: No module named 'geosandbox'
```bash
# Make sure you're in the right directory
cd /path/to/computational-geometry-sandbox

# Install in development mode
pip install -e .
```

### OpenCV not found (for image processing)
```bash
pip install opencv-python
```

### Pygame not found (for visualization)
```bash
pip install pygame
```

## Next Steps

1. **Read the documentation**: Check [README.md](../README.md)
2. **Explore examples**: Look at [examples/](../examples/)
3. **Study algorithms**: Read [docs/COMPLEXITY.md](../docs/COMPLEXITY.md)
4. **Contribute**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

## FAQ

**Q: Can I use this in production?**  
A: Yes! The library is stable and tested. Production use requires additional testing specific to your application.

**Q: Is it fast?**  
A: Performance is good for educational purposes and typical use cases. For high-performance requirements (millions of points), consider GPU acceleration or C++ libraries like CGAL.

**Q: Can I modify for my needs?**  
A: Yes! It's MIT licensed. You're free to fork, modify, and use it in your projects.

**Q: How do I visualize results?**  
A: Use matplotlib, pygame, or plotly. See examples for visualization patterns.

---

**Happy geometry! 🎨**
