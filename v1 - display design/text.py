from kivy.uix.label import Label

class Text(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inittext(self, text, fnt, col, posx, posy):
        self.fontsize = "50dp"
        self.posx = posx
        self.posy = posy
        self.text = text
        self.font = fnt
        self.col = col

    def show(self, mainw, mainh):
        if self.posx == "center":
            self.posxc = (mainw/2-self.width/2)
        else:
            self.posxc = self.posx
        if self.posy == "center":
            self.posyc = (mainh/2-self.height/2)
        else:
            self.posyc = self.posy

        return Label(text=self.text, font_name=self.font, color=self.col, font_size=self.fontsize, pos=(self.posxc, self.posyc))