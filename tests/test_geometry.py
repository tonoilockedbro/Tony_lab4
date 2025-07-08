import pytest
from geometry.utils import area_stats
from geometry.shapes import Square, Circle
def test_square_area_zero_and_positive():
    square = Square(0)
    assert square.area() == 0
    square = Square(5)
    assert square.area() == 25
def test_stats_keys_and_values():
    square = Square(4)
    circle = Circle(3)
    shapes = [square, circle]
    stats = area_stats(shapes)
    assert set(stats.keys()) == {'n', 'total', 'mean', 'min', 'max'}
    assert stats['n'] == 2
    assert stats['total'] == 44.27431
    assert stats['mean'] == 22.137155
    assert stats['min'] == 16
    assert stats['max'] == 28.27431
def test_stats_raises_without_shapes():
    with pytest.raises(TypeError):
        area_stats(None)
    