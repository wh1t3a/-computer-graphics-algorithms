# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-08-28

### Fixed

- Install the package in editable mode before running tests so `geosandbox` is importable in CI
- Correct point-in-polygon boundary expectation: points on the corner count as inside
- Add `pytest.ini` with `pythonpath` fore reliable imports in CI

## [1.0.1] - 2026-08-25

### Fixed

- Use the official codecov-action for coverage upload in CI pipeline

## [1.0.0] - 2026-08-21

### Added

- Core geometric primitives: 2D cross product, orientation test, polygon area (shoelace), point-in-polygon (ray casting), segment intersection
- Convex hull via Graham scan (O(n log n))
- Incremental Delaunay triangulation with empty circumcircle criterion
- Curve algorithms: Bezier (de Casteljau), B-spline (Cox-de Boor), Catmull-Rom and NURBS with weights
- Particle system with Euler integration, color/size interpolation and depth sorting
- Image processing: bilinear warping, mesh triangulation, Bayer ordered dithering
- GitHub Actions CI pipeline and pytest test suite
- Full documentation: README, quickstart, structure overview, complexity analysis
