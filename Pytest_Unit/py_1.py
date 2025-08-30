x = "hello"
# to check x is hello or not, left side is condition and right side is exception if not condition become true
assert x == "hello", "x should be 'hello'"
# assert x == "goodbye", "x should be 'hello'"


# to run path: cd C:\Users\user\Desktop\suresh\Python_Lib
# python -m pytest Pytest_Unit\py_1.py
from Pytest_Unit.make_triangle import make_triangle, make_triangle_1
# def test_make_triangle():
#     expected = '@'
#     actual = '\n'.join(make_triangle(1))
#     assert actual == expected

def test_make_triangle():
    expected = '@'
    actual = '\n'.join(make_triangle_1(1))
    assert actual == expected