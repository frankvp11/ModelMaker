from .Polygon import Polygon
import math


class RoundedRect(Polygon):

    def __init__(self, x, y, width, height, rx, ry, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rx = rx  # x-radius of the corners
        self.ry = ry  # y-radius of the corners
        self.color = kwargs.get('color', 'black')
        super().__init__(**kwargs)

    def emit_events(self, event):
        emit_event = False
        px = event.image_x
        py = event.image_y
        x = (self.x + self.translate_x) * self.x_scale_factor
        y = (self.y + self.translate_y) * self.y_scale_factor
        scaled_rx = self.rx * self.x_scale_factor
        scaled_ry = self.ry * self.y_scale_factor

        # Check if point is inside the main rectangle excluding the corners
        if (x + scaled_rx <= px <= x + self.width - scaled_rx) and \
           (y + scaled_ry <= py <= y + self.height - scaled_ry):
            emit_event = True
        else:
            # Check if point is inside the rounded corners
            for corner_x, corner_y in [(x + scaled_rx, y + scaled_ry),  # top-left corner
                                       (x + self.width - scaled_rx, y + scaled_ry),  # top-right corner
                                       (x + self.width - scaled_rx, y + self.height - scaled_ry),  # bottom-right corner
                                       (x + scaled_rx, y + self.height - scaled_ry)]:  # bottom-left corner
                dx = px - corner_x
                dy = py - corner_y
                if math.sqrt(dx**2 + dy**2) <= scaled_rx:
                    emit_event = True
                    break

        if emit_event and self.event_handler:
            self.event_handler(event, self)

    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'

        svg_code = f'<rect {transforms} {outlines} x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" rx="{self.rx}" ry="{self.ry}" fill="{self.color}" fill-opacity="{self.transparency}" />'
        return svg_code
