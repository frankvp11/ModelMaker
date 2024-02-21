from .Polygon import Polygon
import math

class Wedge(Polygon):
    def __init__(self, cx, cy, radius, start_angle, end_angle, num_segments=30, color='black'):
        vertices = self._generate_wedge_vertices(cx, cy, radius, start_angle, end_angle, num_segments)
        super().__init__(vertices, color=color)

    def _generate_wedge_vertices(self, cx, cy, radius, start_angle, end_angle, num_segments):
        vertices = []
        angle_step = (end_angle - start_angle) / num_segments
        for i in range(num_segments + 1):
            angle = start_angle + i * angle_step
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            vertices.append([x, y])
        # Include the center of the wedge as a vertex
        vertices.append([cx, cy])
        return vertices
