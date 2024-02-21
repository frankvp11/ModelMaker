from .Polygon import Polygon
import math


class RoundedRect(Polygon):
    def __init__(self, x, y, width, height, corner_radius, color='black'):
        vertices = self._generate_rounded_rect_vertices(x, y, width, height, corner_radius)
        super().__init__(vertices, color=color)

    def _generate_rounded_rect_vertices(self, x, y, width, height, corner_radius):
        vertices = []
        x1 = x - width / 2
        y1 = y - height / 2
        x2 = x + width / 2
        y2 = y + height / 2

        # Calculate the vertices for the rounded rectangle
        num_segments = 10  # Number of segments for each corner arc
        arc_radius = corner_radius

        # Top left corner
        vertices.extend(self._generate_arc_vertices(x1 + corner_radius, y1 + corner_radius, arc_radius, 0, 3 * math.pi / 2, num_segments))

        # Top right corner
        vertices.extend(self._generate_arc_vertices(x2 - corner_radius, y1 + corner_radius, arc_radius, 3 * math.pi / 2, 2 * math.pi, num_segments))

        # Bottom right corner
        vertices.extend(self._generate_arc_vertices(x2 - corner_radius, y2 - corner_radius, arc_radius, 0, math.pi / 2, num_segments))

        # Bottom left corner
        vertices.extend(self._generate_arc_vertices(x1 + corner_radius, y2 - corner_radius, arc_radius, math.pi / 2, math.pi, num_segments))

        # Close the path
        vertices.append([x1, y1 + corner_radius])  # Adjusted the bottom left corner
        return vertices

    def _generate_arc_vertices(self, cx, cy, r, start_angle, end_angle, num_segments=10):
        vertices = []
        angle_step = (end_angle - start_angle) / num_segments
        for i in range(num_segments + 1):
            angle = start_angle + i * angle_step
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            vertices.append([x, y])
        return vertices