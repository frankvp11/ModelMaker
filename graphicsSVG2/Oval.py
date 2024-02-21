from .Polygon import Polygon
import math


class Oval(Polygon):
    def __init__(self, cx, cy, rx, ry, num_segments=30, color='black'):
        vertices = self._generate_oval_vertices(cx, cy, rx, ry, num_segments)
        super().__init__(vertices, color=color)

    def _generate_oval_vertices(self, cx, cy, rx, ry, num_segments):
        vertices = []
        angle_step = 2 * math.pi / num_segments
        for i in range(num_segments):
            angle = i * angle_step
            x = cx + rx * math.cos(angle)
            y = cy + ry * math.sin(angle)
            vertices.append([x, y])
        return vertices
    