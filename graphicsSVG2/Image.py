from nicegui import ui

from .Polygon import Polygon
from .ShapeCollection import ShapeCollection


class Image:
    def __init__(self, image_url, shapes):
        self.image_url = image_url
        self.shapes = ShapeCollection(shapes)
        self.content = self.shapes.to_svg()
        self.image = ui.interactive_image(image_url, on_mouse=self.emit_events)
        self.image.bind_content_from(self, 'content')
    

    def add_shape(self, shape):
        self.shapes.append(shape)
    def remove_shape(self, shape):
        self.shapes.remove(shape)


    def emit_events(self, event):
        for shape in self.shapes.polygons:
            shape.emit_events(event)
