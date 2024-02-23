

import math
from .Polygon import Polygon
from .ShapeCollection import ShapeCollection

class Arrow(ShapeCollection):
    def __init__(self, x1, y1, x2, y2, color='black', thickness=1, head_length=10, head_width=5):
        self.thickness = thickness
        self.head_length = head_length
        self.head_width = head_width

        # Calculate angle and length of the arrow
        dx = x2 - x1
        dy = y2 - y1
        self.angle = math.atan2(dy, dx)
        self.length = math.sqrt(dx**2 + dy**2)

        # Calculate coordinates for arrow head
        self.head_top_x = x2 - self.head_length * math.cos(self.angle)
        self.head_top_y = y2 - self.head_length * math.sin(self.angle)
        self.head_left_x = self.head_top_x - self.head_width * math.cos(self.angle + math.pi/6)
        self.head_left_y = self.head_top_y - self.head_width * math.sin(self.angle + math.pi/6)
        self.head_right_x = self.head_top_x - self.head_width * math.cos(self.angle - math.pi/6)
        self.head_right_y = self.head_top_y - self.head_width * math.sin(self.angle - math.pi/6)
        line_1 = Polygon([[x1, y1], [x2, y2]], color=color, stroke_thickness=thickness)
        triangle_1 = Polygon([[x2, y2], [self.head_left_x, self.head_left_y], [self.head_right_x, self.head_right_y]], color=color, stroke_thickness=thickness)
        # ShapeCollection([line_1, triangle_1])
        super().__init__([line_1, triangle_1])
