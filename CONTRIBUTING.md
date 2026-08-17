# Contributing to Computational Geometry Sandbox

Thanks for your interest in contributing! 🎉

## How to Contribute

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/my-feature`)
3. **Make your changes** and add tests
4. **Commit** with clear messages
5. **Push** to your fork
6. **Create a Pull Request**

## Development Setup

```bash
git clone https://github.com/YOUR-USERNAME/computational-geometry-sandbox.git
cd computational-geometry-sandbox

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

## Code Style

- Use **Black** for formatting: `black geosandbox/`
- Use **Pylint** for linting: `pylint geosandbox/`
- Write **docstrings** for all functions (Google style)
- Add **type hints** where possible

```python
def convex_hull(points: list[Point]) -> list[Point]:
    """Build convex hull using Graham Scan.
    
    Args:
        points: List of 2D points
        
    Returns:
        Vertices of convex hull in CCW order
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_geometry.py -v

# Run with coverage
pytest --cov=geosandbox tests/
```

## Documentation

- Update **README.md** for user-facing changes
- Add **docstrings** in module docstrings
- Create detailed comments for complex algorithms
- Include algorithm descriptions and complexity analysis

## Areas for Contribution

### High Priority
- [ ] O(n log n) Delaunay implementation
- [ ] Voronoi diagram computation
- [ ] Additional curve types (Hermite, basis functions)
- [ ] Comprehensive test suite

### Medium Priority
- [ ] GPU-accelerated algorithms (CuPy)
- [ ] Web visualization interface
- [ ] Performance benchmarking suite
- [ ] Additional examples

### Nice to Have
- [ ] 3D geometry algorithms
- [ ] Mesh optimization algorithms
- [ ] Exact arithmetic predicates
- [ ] Integration with geometry libraries (CGAL)

## Questions?

Open an **Issue** for questions or discussions about the project.

---

**Thank you for making computational geometry more accessible!** 🙏
