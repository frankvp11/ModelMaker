
from .Polygon import Polygon

class Line(Polygon):
    def __init__(self, x1, y1, x2, y2, **kwargs):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        super().__init__(**kwargs)
    
    def emit_events(self, event):
        emit_event = False
        px = event.image_x
        py = event.image_y
        x1 = (self.x1 + self.translate_x) * self.x_scale_factor
        y1 = (self.y1 + self.translate_y - 0.5 * self.stroke_thickness) * self.y_scale_factor
        x2 = (self.x2 + self.translate_x) * self.x_scale_factor
        y2 = (self.y2 + self.translate_y + 0.5 * self.stroke_thickness) * self.y_scale_factor 
        if px >= x1 and px <= x2 and py >= y1 and py <= y2:
            emit_event = True
        if emit_event and self.event_handler:
            self.event_handler(event, self)

    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        svg_code = f'<line  {transforms} {outlines} x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.color}" stroke-width="{self.stroke_thickness}" />'
        return svg_code