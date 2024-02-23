from typing import List



class ShapeCollection:
    def __init__(self, polygons: List= []):
        self.polygons = polygons

    def add_polygon(self, polygon):
        self.polygons.append(polygon)

    def move_all(self, dx, dy):
        for polygon in self.polygons:
            polygon.move(dx, dy)
    
    def scale_all(self, amount):
        for polygon in self.polygons:
            polygon.scale(amount)
            
    def rotate_all(self, angle, x=0, y=0):
        for polygon in self.polygons:
            polygon.rotate(angle, x, y)
    def remove_polygon(self, polygon):
        self.polygons.remove(polygon)


    def to_svg(self):
        return "".join([polygon.to_svg() for polygon in self.polygons])

