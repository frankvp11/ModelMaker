from .Polygon import Polygon
import math

class Wedge(Polygon):
    def __init__(self, cx, cy, radius, start_angle, end_angle, **kwargs):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle
        super().__init__(**kwargs)
    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        x1 = self.cx + self.radius * math.cos(math.pi * self.start_angle / 180)
        y1 = self.cy + self.radius * math.sin(math.pi * self.start_angle / 180)
        x2 = self.cx + self.radius * math.cos(math.pi * self.end_angle / 180)
        y2 = self.cy + self.radius * math.sin(math.pi * self.end_angle / 180)
        svg_code = f'<path {transforms} {outlines} d="M{self.cx} {self.cy} L{x1} {y1} A{self.radius} {self.radius} 0 0 1 {x2} {y2} z" fill="{self.color}" />'



        return svg_code

        
