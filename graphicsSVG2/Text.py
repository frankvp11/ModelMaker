class Text:
    def __init__(self, text, x, y, color='black', font_size=12, bold =  False, italics = False, underline= False, strikethrough=False, selectable=False):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size
        self.bold = bold
        self.italics = italics
        self.underline = underline
        self.strikethrough = strikethrough
        self.selectable = selectable
        self.x_scale_factor = 1
        self.y_scale_factor = 1

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, angle):
        # Rotation is not applicable to text
        pass

    def scaleX(self, factor):
        self.x_scale_factor = factor

    def scaleY(self, factor):
        self.y_scale_factor = factor

    def scale(self, factor):
        self.x_scale_factor = factor
        self.y_scale_factor = factor

    def set_bold(self, bold):
        self.bold = bold

    def set_italics(self, italics):
        self.italics = italics

    def set_underline(self, underline):
        self.underline = underline

    def set_strikethrough(self, strikethrough):
        self.strikethrough = strikethrough

    def set_selectable(self, selectable):
        self.selectable = selectable

    def to_svg(self):
        style = ""
        if self.bold:
            style += "font-weight: bold; "
        if self.italics:
            style += "font-style: italic; "
        if self.underline:
            style += "text-decoration: underline; "
        if self.strikethrough:
            style += "text-decoration: line-through; "
        if self.selectable:
            style += "user-select: auto; "
        print(self.x_scale_factor)
        print(self.y_scale_factor)
        svg_text = f'<text transform="scale({self.x_scale_factor}, {self.y_scale_factor})" x="{self.x}" y="{self.y}" fill="{self.color}" font-size="{self.font_size}" style="{style}">{self.text}</text>'
        return svg_text
