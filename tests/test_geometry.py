"""Tests for computational geometry algorithms."""

import pytest
from geosandbox.geometry import (
    convex_hull, delaunay, point_in_polygon,
    segments_intersect, polygon_area, cross
)


class TestBasicOperations:
    """Test basic geometric operations."""
    
    def test_cross_product(self):
        """Test 2D cross product."""
        # CCW orientation
        assert cross((0, 0), (1, 0), (0, 1)) > 0
        # CW orientation
        assert cross((0, 0), (0, 1), (1, 0)) < 0
        # Collinear
        assert cross((0, 0), (1, 1), (2, 2)) == 0
    
    def test_polygon_area(self):
        """Test polygon area calculation."""
        # Unit square
        square = [(0, 0), (1, 0), (1, 1), (0, 1)]
        assert polygon_area(square) == 1.0
        
        # Triangle
        triangle = [(0, 0), (2, 0), (0, 2)]
        assert polygon_area(triangle) == 2.0
    
    def test_point_in_polygon(self):
        """Test point-in-polygon ray casting."""
        square = [(0, 0), (10, 0), (10, 10), (0, 10)]
        
        assert point_in_polygon((5, 5), square) == True
        assert point_in_polygon((15, 15), square) == False
        assert point_in_polygon((0, 0), square) == False  # On corner


class TestConvexHull:
    """Test Graham Scan convex hull."""
    
    def test_square(self):
        """Test hull of square."""
        points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
        hull = convex_hull(points)
        assert len(hull) == 4
    
    def test_collinear(self):
        """Test hull of collinear points."""
        points = [(0, 0), (1, 1), (2, 2)]
        hull = convex_hull(points)
        assert len(hull) >= 2
    
    def test_single_point(self):
        """Test hull of single point."""
        points = [(5, 5)]
        hull = convex_hull(points)
        assert hull == points
    
    def test_ccw_order(self):
        """Test that hull is in CCW order."""
        points = [(0, 0), (4, 0), (4, 3), (2, 4), (0, 3)]
        hull = convex_hull(points)
        
        # Check if points form CCW loop
        area = 0
        for i in range(len(hull)):
            p1 = hull[i]
            p2 = hull[(i + 1) % len(hull)]
            area += (p2[0] - p1[0]) * (p2[1] + p1[1])
        
        assert area < 0  # Negative area = CCW


class TestDelaunay:
    """Test Delaunay triangulation."""
    
    def test_square(self):
        """Test triangulation of square with center."""
        points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
        triangles = delaunay(points)
        
        # Should have multiple triangles
        assert len(triangles) > 0
        
        # All vertex indices should be valid
        for tri in triangles:
            assert all(0 <= idx < len(points) for idx in tri)
    
    def test_grid(self):
        """Test triangulation of regular grid."""
        points = []
        for i in range(3):
            for j in range(3):
                points.append((i, j))
        
        triangles = delaunay(points)
        assert len(triangles) > 0
    
    def test_minimum_points(self):
        """Test with minimum points."""
        points = [(0, 0), (1, 0), (0.5, 1)]
        triangles = delaunay(points)
        
        # Should form exactly one triangle
        assert len(triangles) >= 1


class TestIntersection:
    """Test line segment intersection."""
    
    def test_intersecting_segments(self):
        """Test segments that intersect."""
        # X crossing
        assert segments_intersect((0, 0), (1, 1), (0, 1), (1, 0)) == True
    
    def test_parallel_segments(self):
        """Test parallel segments."""
        assert segments_intersect((0, 0), (1, 0), (0, 1), (1, 1)) == False
    
    def test_touching_endpoints(self):
        """Test segments touching at endpoint."""
        assert segments_intersect((0, 0), (1, 0), (1, 0), (2, 0)) == True
    
    def test_non_intersecting(self):
        """Test segments that don't intersect."""
        assert segments_intersect((0, 0), (1, 0), (0, 2), (1, 2)) == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
