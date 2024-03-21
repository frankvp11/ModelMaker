class Text:
    def __init__(self, text, x, y, **kwargs):
        self.text = text
        self.x = x
        self.y = y
        self.color =    kwargs.get('color', 'black')
        self.font_size = kwargs.get('font_size', 12)
        self.bold = kwargs.get('bold', False)
        self.italics = kwargs.get('italics', False)
        self.underline = kwargs.get('underline', False)
        self.strikethrough = kwargs.get('strikethrough', False)
        self.selectable =  kwargs.get('selectable', False)
        self.x_scale_factor = 1
        self.y_scale_factor = 1
        self.transparency = kwargs.get('transparency', 1)
        self.event_handler = kwargs.get('event_handler', None)

    def update_transparency(self, transparency):
        self.transparency = transparency

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
        
    def set_color(self, color): 
        self.color = color
    

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
        svg_text = f'<text transform="scale({self.x_scale_factor}, {self.y_scale_factor})" x="{self.x}" y="{self.y}" fill="{self.color}" fill-opacity="{self.transparency}" font-size="{self.font_size}" style="{style}">{self.text}</text>'
        return svg_text
