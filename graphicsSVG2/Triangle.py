
from .Polygon import Polygon

class Triangle(Polygon):
    def __init__(self, x1, y1, x2, y2, x3, y3, color='black'):
        vertices = [[x1, y1], [x2, y2], [x3, y3]]
        super().__init__(vertices, color=color)
