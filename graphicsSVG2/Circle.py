from .Polygon import Polygon

import math



class Circle(Polygon):
    def __init__(self, cx, cy, r, color='black', **kwargs):
        self.cx = cx
        self.cy = cy
        self.r = r
        super().__init__(color=color, **kwargs)

    def emit_events(self, event):
        emit_event = False
        px = event.image_x
        py = event.image_y
        
        center = ((self.cx + self.translate_x) * self.x_scale_factor, (self.cy + self.translate_y) * self.y_scale_factor)
        radius = self.r * self.x_scale_factor
        distance = math.sqrt((px - center[0])**2 + (py - center[1])**2)

        if distance <= radius:
            emit_event = True
        if emit_event and self.event_handler:
            self.event_handler(event, self)


    def to_svg(self):
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        svg_code = f'<circle  {transforms}  cx="{self.cx}" cy="{self.cy}" r="{self.r}" fill="{self.color}" fill-opacity="{self.transparency}" stroke="{self.stroke_outline}" {outlines} />'
        return svg_code


