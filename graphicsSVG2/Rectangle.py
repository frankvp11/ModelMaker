
from .Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, x, y, width, height, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        super().__init__(**kwargs)

    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'

        svg_str = f'<rect {transforms} {outlines} x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="{self.color}" fill-opacity="{self.transparency}" stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}" />'
        return svg_str
    
