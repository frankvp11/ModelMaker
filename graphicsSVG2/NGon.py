
from .Polygon import Polygon
import math

class NGon(Polygon):
    def __init__(self, cx, cy, r, n, **kwargs):
        vertices = self._generate_ngon_vertices(cx, cy, r, n)
        super().__init__(vertices=vertices, **kwargs)

    def _generate_ngon_vertices(self, cx, cy, r, n):
        vertices = []
        for i in range(n):
            angle = 2 * math.pi * i / n
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            vertices.append([x, y])
        return vertices
    