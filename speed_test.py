from graphicsSVG2.Arrow import Arrow
from graphicsSVG2.CustomPolygon import CustomPolygon
from graphicsSVG2.Image import Image
from graphicsSVG2.Rectangle import Rectangle
from graphicsSVG2.Circle import Circle
from graphicsSVG2.Triangle import Triangle
from graphicsSVG2.Line import Line
from graphicsSVG2.NGon import NGon
from graphicsSVG2.Oval import Oval
from graphicsSVG2.roundedRect import RoundedRect
from graphicsSVG2.Text import Text
from graphicsSVG2.Wedge import Wedge


from nicegui import ui

import time


def handle(event, shape):
    print("Hi there")
    print(event)
    print("Clicked on shape: ", shape)




circle = Wedge(100, 100, 50, 0, 180, color="red", event_handler=handle)
circle.scale(0.5)
circle.move(50, 50)








shapes = [circle]



image = Image("shapes.svg", shapes)





ui.run()