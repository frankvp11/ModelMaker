from .Polygon import Polygon

class CustomPolygon(Polygon):
    def __init__(self, vertices, **kwargs):
        super().__init__(vertices=vertices, **kwargs)
