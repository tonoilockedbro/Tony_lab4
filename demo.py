from geometry.utils import area_stats
from geometry.shapes import Square, Circle
import pytest
s, c = Square(3), Circle(1.5)
list_of_shapes = [s, c]
print(area_stats(list_of_shapes))