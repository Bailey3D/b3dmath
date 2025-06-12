import b3dmath

def test_import():
    assert hasattr(b3dmath, "__doc__")


test_import()
print("b3dmath module imported successfully.")