

class Spline:
    def __init__(self, x0, y0, x1, y1, x2, y2, color='black', thickness=1):
        self.color = color
        self.thickness = thickness

        # # Control points of the spline
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        

    def move(self, dx, dy):
        self.x0 += dx
        self.y0 += dy
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def rotate(self, angle):
        # Rotation not applicable for quadratic splines
        pass

    def scaleX(self, factor):
        self.x0 *= factor
        self.x1 *= factor
        self.x2 *= factor

    def scaleY(self, factor):
        self.y0 *= factor
        self.y1 *= factor
        self.y2 *= factor

    def scale(self, factor):
        self.scaleX(factor)
        self.scaleY(factor)

    def set_color(self, color):
        self.color = color

    def emit_events(self, event):
        # TODO: Implement this method
        pass

    def to_svg(self):
        return f'<path d="M {self.x0} {self.y0} Q {self.x1} {self.y1} {self.x2} {self.y2}" stroke="{self.color}" stroke-width="{self.thickness}" fill="none" />'
