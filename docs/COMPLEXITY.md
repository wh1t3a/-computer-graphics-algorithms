# Algorithm Complexity Analysis

Detailed analysis of time and space complexity for all algorithms.

## Computational Geometry

### Graham Scan - Convex Hull

**Time Complexity**: 
- Best case: $O(n \log n)$ — dominated by sorting
- Average case: $O(n \log n)$
- Worst case: $O(n \log n)$

**Space Complexity**: $O(n)$ — for output hull

**Algorithm**:
```
1. Find pivot (min Y, min X)              → O(n)
2. Sort by polar angle                   → O(n log n)
3. Build hull with stack                 → O(n)
```

**Key Insight**: CCW orientation test ensures optimal hull construction

---

### Delaunay Triangulation - Incremental

**Time Complexity**:
- Best case: $O(n \log n)$ — random point insertion order
- Average case: $O(n)$ — optimal for uniform distributions
- Worst case: $O(n^2)$ — degenerate point sets

**Space Complexity**: $O(n)$ — output size is always $O(n)$

**Algorithm**:
```
1. Build super triangle               → O(1)
2. For each point p:
   a) Find bad triangles             → O(n)
   b) Remove bad triangles           → O(n)
   c) Connect boundary to p          → O(n)
3. Remove super triangle             → O(n)
```

**Properties**:
- Delaunay criterion: Empty circumcircle property
- Maximizes minimum angle (numerical stability)
- Unique (unless 4+ cocircular points)

---

### Ray Casting - Point-in-Polygon

**Time Complexity**: $O(n)$ where $n$ = polygon vertices

**Space Complexity**: $O(1)$ — constant space

**Algorithm**:
```
Cast ray from point in +X direction
Count intersections with polygon edges
- Odd count → inside
- Even count → outside
```

**Edge cases handled**:
- Ray through vertex
- Horizontal edges
- Degenerate triangles

---

### Segment Intersection

**Time Complexity**: $O(1)$ — constant time per pair

**Space Complexity**: $O(1)$

**Algorithm**:
```
Compute cross products:
- c1 = cross(A,B,C)
- c2 = cross(A,B,D)
- c3 = cross(C,D,A)
- c4 = cross(C,D,B)

Intersect if c1*c2 < 0 AND c3*c4 < 0
(or special case: point on segment)
```

---

## Curves

### Bézier Curve - de Casteljau

**Time Complexity**: $O(n^2 \cdot m)$ where $n$ = control points, $m$ = output steps

**Space Complexity**: $O(n)$ — temporary arrays for interpolation

**Algorithm**:
```
For each parameter t ∈ [0,1]:
  Layer 0: P₀, P₁, ..., Pₙ
  Layer i: Lerp(Layer_{i-1}[j], Layer_{i-1}[j+1], t)
  ...repeat until 1 point
```

**Properties**:
- Affine invariant
- Convex hull property (curve stays within convex hull of control points)
- Velocity vector: $B'(t) = n \sum (P_{i+1} - P_i) B_i(t)$

---

### B-spline - Cox-de Boor

**Time Complexity**: $O(k \cdot m)$ where $k$ ≤ degree, $m$ = output steps

**Space Complexity**: $O(n + k)$ — knot vector + evaluation

**Basis Function** (recursive):
$$N_{i,0}(t) = \begin{cases} 1, & \text{if } t_i \leq t < t_{i+1} \\ 0, & \text{otherwise} \end{cases}$$

$$N_{i,k}(t) = \frac{t - t_i}{t_{i+k} - t_i} N_{i,k-1}(t) + \frac{t_{i+k+1} - t}{t_{i+k+1} - t_{i+1}} N_{i+1,k-1}(t)$$

**Curve Formula**:
$$C(t) = \sum_{i=0}^{n} P_i N_{i,k}(t)$$

**Properties**:
- Local control: moving $P_i$ affects $k+1$ segments
- $C^{k-1}$ smoothness
- Does NOT pass through control points (approximates)
- Partition of unity: $\sum N_{i,k}(t) = 1$

---

### Catmull-Rom - Hermite Interpolation

**Time Complexity**: $O(n \cdot m)$ where $m$ = samples per segment

**Space Complexity**: $O(n + m)$

**Cubic Hermite**:
$$Q(t) = 0.5 \begin{pmatrix} 1 & t & t^2 & t^3 \end{pmatrix} 
\begin{pmatrix} 0 & 2 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 2 & -5 & 4 & -1 \\ -1 & 3 & -3 & 1 \end{pmatrix}
\begin{pmatrix} P_0 \\ P_1 \\ P_2 \\ P_3 \end{pmatrix}$$

**Properties**:
- **PASSES through all control points** (interpolating)
- $C^1$ continuity (smooth velocity)
- Tangent determined by neighboring points
- Perfect for animation paths

---

### NURBS - Rational B-spline

**Time Complexity**: $O(k \cdot m)$ where $k$ = basis functions, $m$ = steps

**Space Complexity**: $O(n \cdot k)$ — weights + basis values

**Curve Formula**:
$$C(t) = \frac{\sum_{i=0}^{n} w_i P_i N_{i,k}(t)}{\sum_{i=0}^{n} w_i N_{i,k}(t)}$$

**Weight Effects**:
- $w_i > 1$: curve attracted to $P_i$ (pulls toward point)
- $w_i = 1$: equivalent to B-spline
- $w_i < 1$: curve repelled from $P_i$
- $w_i \to 0$: point has no effect

**Advantages**:
- Represents **conic sections exactly** (circles, ellipses, parabolas, hyperbolas)
- Industry standard (AutoCAD, SolidWorks, Maya, Blender)
- More flexible than B-splines

---

## Particle Systems

### Update Loop

**Time Complexity**: $O(n)$ per frame where $n$ = active particles

**Space Complexity**: $O(n)$

**Per Particle** (Euler Integration):
```
v(t+dt) = v(t) + a * dt
p(t+dt) = p(t) + v * dt
age += dt
```

**Color Interpolation** (LERP):
```
t = age / life ∈ [0,1]
color = (1-t) * start_color + t * end_color
```

**Sorting for Transparency** (optional):
- Sort by depth: $O(n \log n)$
- Render front-to-back for correct alpha blending

---

## Space Complexity Summary

| Algorithm | Data Structure | Memory |
|-----------|---|---|
| Graham Scan | Array + Hull | $O(n)$ |
| Delaunay | Triangle list | $O(n)$ |
| Ray Casting | - | $O(1)$ |
| Bezier | Control points | $O(n)$ |
| B-spline | Knot vector | $O(n)$ |
| Catmull-Rom | Points + temp | $O(n)$ |
| NURBS | Weights | $O(n)$ |

---

## Optimization Strategies

### For Geometry Algorithms

1. **Delaunay to O(n log n)**:
   - Use divide-and-conquer (merge sorted triangulations)
   - Use randomized incremental with walk structure
   - Use Sweepline algorithm

2. **Graham Scan tuning**:
   - Pre-sort by X to avoid edge cases
   - Use only 3 points test (skip collinear)
   - Vectorize cross product

3. **Ray Casting optimization**:
   - For multiple point queries: build acceleration structure (BSP tree)
   - Or use precomputed edge equations

### For Curve Algorithms

1. **Basis function caching**:
   - Pre-compute basis values at common parameters
   - Memoize recursive Cox-de Boor values

2. **Parallel evaluation**:
   - Compute curve points in parallel (embarrassingly parallel)
   - Use SIMD for multiple curves

3. **Adaptive subdivision**:
   - Use fewer steps for flat segments
   - Increase precision near high-curvature regions

---

## Numerical Stability

### Floating Point Issues

1. **Cross product**: Use epsilon for collinearity check
   ```python
   if abs(cross(a,b,c)) < 1e-9:
       # Treat as collinear
   ```

2. **Circumcircle test**: Reorder operands to minimize cancellation error

3. **Knot vectors**: Normalize to [0,1] range for stability

---

## References

- **Graham Scan**: R. Graham, "An Efficient Algorithm for Determining the Convex Hull of a Finite Planar Set"
- **Delaunay**: Guibas & Stolfi, "Primitives for the Manipulation of General Subdivisions and the Computation of Voronoi"
- **B-splines**: Cox (1972), de Boor (1972)
- **NURBS**: Piegl & Tiller, "The NURBS Book" (second edition)

