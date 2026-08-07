"""Image processing and deformation utilities."""

Point = tuple[float, float]
Triangle = tuple[int, int, int]


def bilinear_warp(image, source_quad: list[Point], target_quad: list[Point]):
    """
    Bilinear warping between quadrilaterals.
    
    Complexity: O(width * height)
    """
    import cv2
    import numpy as np
    
    src = np.array(source_quad, dtype=np.float32)
    dst = np.array(target_quad, dtype=np.float32)
    
    matrix = cv2.getPerspectiveTransform(src, dst)
    height, width = image.shape[:2]
    
    return cv2.warpPerspective(image, matrix, (width, height))


def mesh_triangulation(image, points: list[Point]) -> list[Triangle]:
    """
    Compute Delaunay triangulation for mesh-based warping.
    
    Complexity: O(n log n) with proper implementation
    """
    try:
        import cv2
        import numpy as np
        
        height, width = image.shape[:2]
        rect = (0, 0, width, height)
        
        subdiv = cv2.Subdiv2D(rect)
        for pt in points:
            subdiv.insert(tuple(int(x) for x in pt))
        
        triangles = subdiv.getTriangleList()
        return [
            (int(tri[0]), int(tri[1]), int(tri[2]))
            for tri in triangles
        ]
    except Exception:
        return []


def ordered_dithering(image, levels: int = 4):
    """
    Bayer matrix ordered dithering.
    
    Complexity: O(width * height * levels)
    """
    import numpy as np
    
    # Bayer 4x4 matrix
    bayer = np.array([
        [0, 8, 2, 10],
        [12, 4, 14, 6],
        [3, 11, 1, 9],
        [15, 7, 13, 5]
    ], dtype=np.float32) / 16.0
    
    gray = np.mean(image[:, :, :3], axis=2) if len(image.shape) == 3 else image
    h, w = gray.shape
    
    result = np.zeros_like(gray)
    
    for i in range(h):
        for j in range(w):
            threshold = bayer[i % 4, j % 4]
            normalized = gray[i, j] / 255.0
            result[i, j] = 255 if normalized > threshold else 0
    
    return result.astype(np.uint8)


__all__ = [
    "bilinear_warp",
    "mesh_triangulation",
    "ordered_dithering",
]
