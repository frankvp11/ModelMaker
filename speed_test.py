
from graphicsSVG2.Rectangle import Rectangle
from nicegui import ui

import time

start = time.time()

elements = []
for i in range(1000):
    elements.append(Rectangle(i, 0, 1, 1, color="green").to_svg())

stop1 = time.time()
image = ui.interactive_image(source="shapes.svg")
image.content = "".join(elements)


stop2 = time.time()

print("Time taken to create all 1000 elements: ", str(stop1-start))
print("Time taken to render all 1000 elements: ", str(stop2-stop1))

ui.run()