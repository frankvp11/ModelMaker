
from .Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, x, y, width, height, color='black'):
        vertices = [
            [x, y],
            [x + width, y],
            [x + width, y + height],
            [x, y + height]
        ]
        super().__init__(vertices, color=color)    
