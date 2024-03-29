from .Polygon import Polygon
import math


class Oval(Polygon):
    def __init__(self, cx, cy, rx, ry, **kwargs):
        self.cx = cx
        self.cy = cy
        self.rx = rx  # x-radius
        self.ry = ry  # y-radius
        self.color = kwargs.get('color', 'black')
        super().__init__(**kwargs)

    def emit_events(self, event):
        emit_event = False
        px = event.image_x
        py = event.image_y
        x = (self.cx + self.translate_x) * self.x_scale_factor
        y = (self.cy + self.translate_y) * self.y_scale_factor
        if (px - x) ** 2 / self.rx ** 2 + (py - y) ** 2 / self.ry ** 2 <= 1:
            emit_event = True
        if emit_event and self.event_handler:
            self.event_handler(event, self)


    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        svg_code = f'<ellipse {transforms} {outlines} cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" fill-opacity="{self.transparency}" fill="{self.color}" />'
        return svg_code
    