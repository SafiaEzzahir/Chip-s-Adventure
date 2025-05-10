from kivy.uix.label import Label

class Text(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inittext(self, text, fnt, col):
        self.fontsize = "50dp"
        self.currentpos = ("500dp", "50dp")
        self.text = text
        self.font = fnt
        self.col = col

    def show(self):
        return Label(text=self.text, font_name=self.font, color=self.col, font_size=self.fontsize, pos=self.currentpos)