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
        
    def polar_to_cartesian(self, center_x, center_y, radius, angle_in_degrees):
        angle_in_radians = math.radians(angle_in_degrees)
        x = center_x + (radius * math.cos(angle_in_radians))
        y = center_y + (radius * math.sin(angle_in_radians))
        return x, y
    
    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        start_x, start_y = self.polar_to_cartesian(self.cx, self.cy, self.radius, self.start_angle)
        end_x, end_y = self.polar_to_cartesian(self.cx, self.cy, self.radius, self.end_angle)
        arc_sweep = "0" if self.end_angle - self.start_angle <= 180 else "1"
        svg_code = f'<path {transforms} {outlines} d="M {self.cx} {self.cy} L {start_x} {start_y} A {self.radius} {self.radius} 0 {arc_sweep} 1 {end_x} {end_y} z" fill="{self.color}" />'       

        return svg_code

        
