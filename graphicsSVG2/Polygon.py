
import math

class Polygon:
    def __init__(self, vertices, color='black'):
        self.vertices = vertices
        self.color = color
        self.stroke_outline = color
        self.stroke_thickness = 0

    def move(self, dx, dy):
        for i in range(len(self.vertices)):
            self.vertices[i][0] += dx
            self.vertices[i][1] += dy

    def rotate(self, angle):
        angle_rad = math.radians(angle)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)

        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            self.vertices[i][0] = x * cos_angle - y * sin_angle
            self.vertices[i][1] = x * sin_angle + y * cos_angle
    
    def rotate_shape(self, angle, pivot = None):
        angle_rad = math.radians(angle)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)
        if pivot is None:
            pivot = self.calculate_centroid()
        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            x -= pivot[0]
            y -= pivot[1]
            self.vertices[i][0] = x * cos_angle - y * sin_angle + pivot[0]
            self.vertices[i][1] = x * sin_angle + y * cos_angle + pivot[1]

    def calculate_centroid(self):
        num_vertices = len(self.vertices)
        if num_vertices == 0:
            return (0, 0)
        cx = sum(x for x, _ in self.vertices) / num_vertices
        cy = sum(y for _, y in self.vertices) / num_vertices
        return (cx, cy)



    def scale_x(self, factor, pivot=None):
        if pivot is None:
            pivot = self.calculate_centroid()

        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            self.vertices[i][0] = pivot[0] + (x - pivot[0]) * factor

    def scale_y(self, factor, pivot=None):
        if pivot is None:
            pivot = self.calculate_centroid()

        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            self.vertices[i][1] = pivot[1] + (y - pivot[1]) * factor

    def scale(self, factor, pivot=None):
        if pivot is None:
            pivot = self.calculate_centroid()

        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            self.vertices[i][0] = pivot[0] + (x - pivot[0]) * factor
            self.vertices[i][1] = pivot[1] + (y - pivot[1]) * factor


    def set_color(self, color):
        self.color = color

    def to_svg(self):
        points_str = " ".join([f"{x},{y}" for x, y in self.vertices])
        return f'<polygon points="{points_str}" fill="{self.color}" stroke="{self.stroke_outline}" stroke-width="{self.stroke_thickness}"/>'

    def give_outline(self, color, thickness):
        self.stroke_outline = color
        self.stroke_thickness = thickness
        # Generate lines between consecutive vertices to form the outline
        

