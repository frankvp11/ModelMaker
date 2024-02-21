import math
from graphicsSVG2.Circle import Circle
from graphicsSVG2.Rectangle import Rectangle
from graphicsSVG2.Triangle import Triangle
from graphicsSVG2.NGon import NGon





# Create shapes
circle = Circle(100, 100, 50, 'red')
triangle = Triangle(50, 50, 150, 50, 100, 150, 'blue')
rectangle = Rectangle(100, 100, 100, 80, 'green')
ngon = NGon(100, 100, 50, 6, color='black')

from nicegui import ui


image = ui.interactive_image(source="testingstuff/shapes.svg")

main_str = [circle.to_svg(), triangle.to_svg(), rectangle.to_svg(), ngon.to_svg()]
# main_str = []


image.content = "".join(main_str)


def update_triangle(e):
    triangle.rotate(-60)
    main_str[1] = triangle.to_svg()
    image.content = "".join(main_str)


def update_rectangle(e):
    rectangle.rotate_shape(60)
    rectangle.set_color("lightblue")
    main_str[2] = rectangle.to_svg()
    image.content = "".join(main_str)


def update_circle(e):
    circle.scale(2)
    main_str[0] = circle.to_svg()
    image.content = "".join(main_str)


ui.button("Click me", on_click=lambda e : update_triangle(e))
ui.button("Click me 2", on_click=lambda e : update_rectangle(e))
ui.button("Click me 3", on_click=lambda e: update_circle(e))
print(math.radians(-60))
ui.run()