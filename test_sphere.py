import numpy as np
from b3dmath.geometry.shapes.sphere import are_vertices_spherical


def test_sphere_valid():
    # Vertices of a unit sphere (octants on the surface)
    r = 1.0
    vertices = [
        [ r,  0,  0],
        [-r,  0,  0],
        [ 0,  r,  0],
        [ 0, -r,  0],
        [ 0,  0,  r],
        [ 0,  0, -r],
        [ r/np.sqrt(2), r/np.sqrt(2), 0],
        [-r/np.sqrt(2), -r/np.sqrt(2), 0],
    ]
    vertices = np.array(vertices)
    assert are_vertices_spherical(vertices, deviation=0.05)


def test_sphere_broken():
    # One vertex is moved off the sphere
    r = 1.0
    vertices = [
        [ r,  0,  0],
        [-r,  0,  0],
        [ 0,  r,  0],
        [ 0, -r,  0],
        [ 0,  0,  r],
        [ 0,  0, -r],
        [ r/np.sqrt(2), r/np.sqrt(2), 0],
        [ 2, 2, 2],  # Broken vertex
    ]
    vertices = np.array(vertices)
    assert not are_vertices_spherical(vertices, deviation=0.05)


def test_sphere_zeros():
    # All vertices at the origin
    vertices = [[0, 0, 0]] * 8
    vertices = np.array(vertices)
    assert not are_vertices_spherical(vertices)

if __name__ == "__main__":
    test_sphere_valid()
    test_sphere_broken()
    test_sphere_zeros()
    print("All sphere tests passed!")
