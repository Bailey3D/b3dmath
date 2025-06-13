import numpy as np
from b3dmath.geometry.shapes.cuboid import are_vertices_cuboidal

def test_cuboid_valid():
    # Vertices of a unit cube centered at the origin
    vertices = [
        [-0.5, -0.5, -0.5],
        [-0.5, -0.5,  0.5],
        [-0.5,  0.5, -0.5],
        [-0.5,  0.5,  0.5],
        [ 0.5, -0.5, -0.5],
        [ 0.5, -0.5,  0.5],
        [ 0.5,  0.5, -0.5],
        [ 0.5,  0.5,  0.5],
    ]
    vertices = np.array(vertices)
    assert are_vertices_cuboidal(vertices)

def test_cuboid_broken():
    # One vertex is moved, breaking cuboid property
    vertices = [
        [-0.5, -0.5, -0.5],
        [-0.5, -0.5,  0.5],
        [-0.5,  0.5, -0.5],
        [-0.5,  0.5,  0.5],
        [ 0.5, -0.5, -0.5],
        [ 0.5, -0.5,  0.5],
        [ 0.5,  0.5, -0.5],
        [ 0.5,  1.5,  0.5],  # Broken vertex
    ]
    vertices = np.array(vertices)
    assert not are_vertices_cuboidal(vertices)

def test_cuboid_zeros():
    # All vertices at the origin
    vertices = [[0, 0, 0]] * 8
    vertices = np.array(vertices)
    assert not are_vertices_cuboidal(vertices)

def test_cuboid_random_8():
    # Random vertices that form a cuboid
    vertices = []
    for i in range(8):
        x = np.random.choice([-0.5, 0.5])
        y = np.random.choice([-0.5, 0.5])
        z = np.random.choice([-0.5, 0.5])
        vertices.append([x, y, z])
    vertices = np.array(vertices)


if __name__ == "__main__":
    test_cuboid_valid()
    test_cuboid_broken()
    test_cuboid_zeros()
    print("All tests passed!")  # This line is just for confirmation in a script context