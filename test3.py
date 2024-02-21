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
# Create shapes
# circle = Circle(100, 100, 50, 'red')
# triangle = Triangle(50, 50, 150, 50, 100, 150, 'blue')
# rectangle = Rectangle(100, 100, 100, 80, 'green')
# ngon = NGon(100, 100, 50, 6, color='black')

# custom_vertices = [
#     [50, 50],
#     [100, 50],
#     [100, 100],
#     [75, 125],
# ]
# custom_polygon = CustomPolygon(custom_vertices, "red")

# custom_polygon2 =  Oval(0, 0, 100, 50, color='blue')
# custom_polygon2.move(0, 30)


app.add_static_file(local_file="testingstuff/shapes.svg", url_path="testingstuff/shapes.svg")


# custom_polygon = Wedge(0, 0, 100, math.pi / 4, 8 * math.pi / 4, color='green')
# custom_polygon =  Text("Hello, World!", 5, 20)
custom_polygon = Rectangle(0,0, 100, 80, 'green')
custom_polygon.move(100, 100)
custom_polygon.scale(0.5)
# custom_polygon.rotate(45, 100, 100)
# custom_polygon.skewX()
# custom_polygon.move(100, 100   )
custom_polygon.give_outline("black", 5)


class SVGContent():
    def __init__(self) -> None:
        self.content = ""


image = ui.interactive_image(source="testingstuff/shapes.svg")

# main_str = [circle.to_svg(), triangle.to_svg(), rectangle.to_svg(), ngon.to_svg()]
main_str = [custom_polygon.to_svg()]
svgcontent = SVGContent()
svgcontent.content = "".join(main_str)

# group_object = ShapeCollection([custom_polygon, custom_polygon2])
# group_object.scale_all(0.5)
# group_object.move_all(50, 10)


image.bind_content_from(svgcontent, 'content')
# image.content = main_str    

def update_triangle(e):
    custom_polygon.rotate(45, 100, 100)
    svgcontent.content = custom_polygon.to_svg()

ui.button("Click me", on_click=lambda e : update_triangle(e))





ui.run()