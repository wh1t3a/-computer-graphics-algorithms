# Directory Structure

```
computational-geometry-sandbox/
│
├── 📄 README.md                          # Main documentation
├── 📄 QUICKSTART.md                      # Quick start guide
├── 📄 CONTRIBUTING.md                    # Contribution guidelines
├── 📄 LICENSE                            # MIT License
├── 📄 setup.py                           # Package setup
├── 📄 requirements.txt                   # Dependencies
├── 📄 .gitignore                         # Git ignore rules
│
├── 🎨 geosandbox/                        # Main package
│   ├── __init__.py                       # Package initialization
│   │
│   ├── 📐 geometry/                      # Computational geometry
│   │   ├── __init__.py
│   │   └── core.py                       # Core algorithms
│   │       ├── Point, Triangle, Edge types
│   │       ├── cross()                   # 2D cross product
│   │       ├── polygon_area()            # Shoelace formula
│   │       ├── point_in_polygon()        # Ray casting
│   │       ├── segments_intersect()      # Line intersection
│   │       ├── convex_hull()             # Graham Scan O(n log n)
│   │       ├── delaunay()                # Delaunay triangulation O(n²)
│   │       └── circumcircle_contains()   # Delaunay criterion
│   │
│   ├── 🎯 curves/                        # Curve algorithms
│   │   ├── __init__.py
│   │   ├── bezier.py                     # Bezier curves (de Casteljau)
│   │   ├── bspline.py                    # B-splines (Cox-de Boor)
│   │   └── nurbs.py                      # NURBS with weights
│   │
│   ├── 🎬 physics/                       # Particle systems & physics
│   │   └── __init__.py
│   │       ├── Vec3                      # 3D vector math
│   │       ├── Particle                  # Individual particle
│   │       └── ParticleSystem            # Particle manager
│   │
│   └── 🖼️ image/                         # Image processing
│       └── __init__.py
│           ├── bilinear_warp()           # Mesh warping
│           ├── mesh_triangulation()      # Delaunay for mesh
│           └── ordered_dithering()       # Bayer dithering
│
├── 📚 examples/                          # Example scripts
│   ├── graham_scan_demo.py               # Convex hull examples
│   ├── delaunay_mesh.py                  # Triangulation examples
│   ├── curves_demo.py                    # Curve algorithm examples
│   └── particle_effects.py               # Particle system examples
│
├── 🧪 tests/                             # Unit tests
│   ├── test_geometry.py                  # Geometry algorithm tests
│   ├── test_curves.py                    # Curve algorithm tests
│   └── test_physics.py                   # Physics simulation tests
│
├── 📖 docs/                              # Documentation
│   ├── ALGORITHMS.md                     # Detailed algorithm descriptions
│   ├── COMPLEXITY.md                     # Time/space complexity analysis
│   └── MATHEMATICS.md                    # Mathematical foundations
│
└── .github/
    └── workflows/
        └── python-tests.yml              # GitHub Actions CI/CD
```

## Module Organization

### `geosandbox.geometry`
Core computational geometry algorithms

| Function | Time Complexity | Use Case |
|----------|---|---|
| `convex_hull()` | O(n log n) | Find minimal convex polygon |
| `delaunay()` | O(n²) / O(n log n) | Mesh generation, triangulation |
| `point_in_polygon()` | O(n) | Point classification |
| `segments_intersect()` | O(1) | Collision detection |

### `geosandbox.curves`
Curve rendering and interpolation

| Function | Type | Properties |
|----------|------|-----------|
| `bezier()` | Bezier | Doesn't interpolate, smooth, predictable |
| `bspline()` | B-spline | Doesn't interpolate, very smooth, local control |
| `catmull_rom()` | Catmull-Rom | **Interpolates all points**, animation-friendly |
| `nurbs_curve()` | NURBS | Weighted control, can represent conics |

### `geosandbox.physics`
Particle systems and physics

| Class | Purpose |
|-------|---------|
| `Vec3` | 3D vector for position/velocity/acceleration |
| `Particle` | Individual particle with physics and visual properties |
| `ParticleSystem` | Manager for multiple particles |

### `geosandbox.image`
Image processing and deformation

| Function | Purpose |
|----------|---------|
| `bilinear_warp()` | Warp image between quadrilaterals |
| `mesh_triangulation()` | Delaunay triangulation for mesh |
| `ordered_dithering()` | Bayer matrix dithering |

## File Size Overview

```
geosandbox/geometry/core.py      ~300 lines  (Core algorithms)
geosandbox/curves/bezier.py      ~80 lines   (Bezier curves)
geosandbox/curves/bspline.py     ~100 lines  (B-splines)
geosandbox/curves/nurbs.py       ~50 lines   (NURBS)
geosandbox/physics/__init__.py   ~150 lines  (Particle system)
geosandbox/image/__init__.py     ~80 lines   (Image processing)

examples/                         ~400 lines  (4 demo scripts)
docs/                             ~600 lines  (3 documentation files)
tests/                            ~200 lines  (Test suite)
```

**Total**: ~2000+ lines of code, documentation, and examples

## Dependencies

```
pygame          >= 2.1.0      # Visualization (optional for core)
numpy           >= 1.21.0     # Numerical computation
opencv-python   >= 4.5.0      # Image processing (optional)
```

## Adding New Algorithms

To add a new algorithm:

1. **Create file** in appropriate module: `geosandbox/geometry/new_algo.py`
2. **Implement algorithm** with docstring
3. **Add type hints** for all parameters
4. **Update `__init__.py`** to export public API
5. **Write tests** in `tests/test_*.py`
6. **Create example** in `examples/`
7. **Document** in README.md or docs/

---

**Project Stats**:
- 15+ core algorithms
- 4 curve types
- Full particle system
- Comprehensive documentation
- Examples for every major feature
