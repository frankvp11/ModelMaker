
from .Polygon import Polygon

class Triangle(Polygon):
    def __init__(self, x1, y1, x2, y2, x3, y3, **kwargs):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        super().__init__(**kwargs)

    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'

        svg_code = f'<polygon {transforms} {outlines} points="{self.x1},{self.y1} {self.x2},{self.y2} {self.x3},{self.y3}" fill="{self.color}" />'
        return svg_code
