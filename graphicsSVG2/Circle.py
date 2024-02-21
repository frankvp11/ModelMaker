from .Polygon import Polygon

import math



class Circle(Polygon):
    def __init__(self, cx, cy, r, color='black'):
        self.cx = cx
        self.cy = cy
        self.r = r
        vertices = self._generate_circle_vertices(cx, cy, r)
        super().__init__(vertices, color=color)

    def _generate_circle_vertices(self, cx, cy, r, num_points=30):
        vertices = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            vertices.append([x, y])
        return vertices

