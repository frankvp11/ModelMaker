
from .Polygon import Polygon

class Line(Polygon):
    def __init__(self, x1, y1, x2, y2, thickness=1):
        super().__init__([(x1, y1), (x2, y2), (x1 + (x2-x1), y2), (x1+(x2-x1), y2) ], stroke_thickness=thickness, color='black')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

