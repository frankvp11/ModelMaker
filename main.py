import math

from nicegui import ui, app


from graphicsSVG2.Circle import Circle
from graphicsSVG2.Rectangle import Rectangle
from graphicsSVG2.Triangle import Triangle
from graphicsSVG2.NGon import NGon
from graphicsSVG2.CustomPolygon import CustomPolygon
from graphicsSVG2.roundedRect import RoundedRect
from graphicsSVG2.Oval import Oval
from graphicsSVG2.Wedge import Wedge
from graphicsSVG2.ShapeCollection import ShapeCollection
from graphicsSVG2.Text import Text
from graphicsSVG2.Line import Line
# Create shapes


custom_vertices = [
    [50, 50],
    [100, 50],
    [100, 100],
    [50, 100],
]

circle = Circle(100, 100, 50, 'green') # Good
triangle = Triangle(50, 50, 150, 50, 100, 150, color='green') #good
rectangle = Rectangle(100, 100, 100, 80, color='green') # Good
ngon = NGon(100, 100, 50, 6, color='green') # Good
custom_polygon = CustomPolygon(custom_vertices, color="green") # Good
oval =  Oval(100, 100, 100, 50, color='green') # Good
wedge = Wedge(100, 100, 100, 0, 359, color='green') # Bad
roundedrect = RoundedRect(100, 100, 100, 80, 20, 10, color='green') #good
text = Text("hello frank!", 100, 100, color="green", bold=True)  # good
line = Line(0, 0, 100, 100, color='green') # good

transformation_options = ['rotate', "move", "scaleX", "scaleY", "set_color", "skewX", "skewY", "give_outline", 'transparency']
option_selections = ['circle', 'triangle', 'rectangle', 'ngon', 'custom_polygon', 'oval', 'wedge', 'roundedrect', 'text', 'line' ]
app.add_static_file(local_file="shapes.svg", url_path="shapes.svg")




class SVGContent():
    def __init__(self) -> None:
        self.content = ""
        self.shape = circle
        self.transformation = "move"
        with ui.row():
            with ui.column():
                shape_selector = ui.select(option_selections, value='circle', on_change=lambda e : self.update_shape(e))
            with ui.column():
                transformation_selection = ui.select(transformation_options, value="move", on_change=lambda e : self.update_transformation(e))
            with ui.column():
                apply_transformation_button = ui.button("Apply transformation", on_click=self.apply_transformation)

    def update_transformation(self, e):
        self.transformation = e.value
    

    def apply_transformation(self, e):
        if self.transformation == "move":
            print("Trying to move!")
            self.shape.move(10, 0)
        elif self.transformation == "rotate":
            self.shape.rotate(15, 0, 0)
        elif self.transformation == "scaleX":
            self.shape.scale_x(1.5)
        elif self.transformation == "scaleY":
            self.shape.scale_y(1.5)
        elif self.transformation == "set_color":
            self.shape.set_color("red")
        elif self.transformation == "skewX":
            self.shape.skewX(2)
        elif self.transformation == "skewY":
            self.shape.skewY(2)
        elif self.transformation == "give_outline":
            self.shape.give_outline("black", 5)
        elif self.transformation == "transparency":
            self.shape.update_transparency(0.5)


        self.content = self.shape.to_svg()

    def update_shape(self, e):
        if e.value == "circle":
            self.content = circle.to_svg()
            self.shape = circle
        elif e.value == "triangle":
            self.content = triangle.to_svg()
            self.shape = triangle
        elif e.value == "rectangle":
            self.content = rectangle.to_svg()
            self.shape = rectangle
        elif e.value == "ngon":  
            self.content = ngon.to_svg()     
            self.shape = ngon
        elif e.value == "custom_polygon":  
            self.content = custom_polygon.to_svg()     
            self.shape = custom_polygon
        elif e.value == "oval":  
            self.content = oval.to_svg()     
            self.shape = oval
        elif e.value == "wedge":  
            self.content = wedge.to_svg()     
            self.shape = wedge
        elif e.value == "roundedrect":  
            self.content = roundedrect.to_svg()     
            self.shape = roundedrect
        elif e.value == "text":  
            self.content = text.to_svg()     
            self.shape = text
        elif e.value == "line":
            self.content = line.to_svg()
            self.shape = line


main_str = circle.to_svg()
svgcontent = SVGContent()
svgcontent.content = main_str

image = ui.interactive_image(source="shapes.svg")
image.bind_content_from(svgcontent, 'content')














ui.run()