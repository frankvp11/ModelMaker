
import math

class Polygon:
    def __init__(self, color='black', **kwargs):
        self.vertices = kwargs.get('vertices', [])
        self.color = color
        self.stroke_outline = color
        self.stroke_thickness = kwargs.get('stroke_thickness', 1)
        self.x_scale_factor = kwargs.get('x_scale_factor', 1)
        self.y_scale_factor = kwargs.get('y_scale_factor', 1)
        self.transparency = kwargs.get('transparency', 1)
        self.translate_x = 0
        self.translate_y = 0
        self.rotate_x = 0
        self.rotate_y = 0 
        self.rotate_angle = 0
        self.x_skew_factor = 1
        self.y_skew_factor = 1
        self.event_handler = kwargs.get('event_handler', None)
    
    def is_point_inside_polygon(self, point):
        x, y = point
        inside = False
        for i in range(len(self.vertices)):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % len(self.vertices)]
            x1, y1 = ((x1 + self.translate_x) * self.x_scale_factor, (y1 + self.translate_y) * self.y_scale_factor)
            x2, y2 = ((x2 + self.translate_x) * self.x_scale_factor, (y2 + self.translate_y) * self.y_scale_factor)

            if ((y1 <= y < y2) or (y2 <= y < y1)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                inside = not inside
        return inside

    def emit_events(self, event):
        emit_event = self.is_point_inside_polygon((event.image_x, event.image_y))
        if emit_event and self.event_handler:
            self.event_handler(event, self)
        


    def move(self, dx, dy):
        self.translate_x += dx
        self.translate_y += dy

    def rotate(self, angle, x=0, y=0):
        self.rotate_angle += angle
        self.rotate_x += x
        self.rotate_y += y


    def update_transparency(self, transparency):
        self.transparency = transparency


    def scale_x(self, factor):
        self.x_scale_factor *= factor

    def scale_y(self, factor):
        self.y_scale_factor *= factor

    def scale(self, factor):
        self.x_scale_factor *= factor
        self.y_scale_factor *= factor

    def set_color(self, color):
        self.color = color

    def skewX(self, factor):
        self.x_skew_factor *= factor

    def skewY(self, factor):
        self.y_skew_factor *= factor

    def to_svg(self): # 

        points_str = " ".join([f"{x},{y}" for x, y in self.vertices])
        transforms = f'transform="scale({self.x_scale_factor}, {self.y_scale_factor}) rotate({self.rotate_angle},{self.rotate_x},{self.rotate_y}) translate({self.translate_x}, {self.translate_y}) skewX({self.x_skew_factor}) skewY({self.y_skew_factor})"'
        outlines = f'stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"'
        poly_str = f'<polygon {transforms} {outlines} points="{points_str}" fill="{self.color}" fill-opacity="{self.transparency}" stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"/>'
        return poly_str
    
    def give_outline(self, color, thickness):
        self.stroke_outline = color
        self.stroke_thickness = thickness


