from .Polygon import Polygon

class CustomPolygon(Polygon):
    def __init__(self, vertices, color='black'):
        super().__init__(vertices, color=color)
