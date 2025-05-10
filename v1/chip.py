from kivy.uix.image import Image
from kivy.uix.widget import Widget

class Chip(Widget):
    current_img = "chipleft.png"
    def __init__(self, mainw, mainh):
        self.actsizex = 345/100
        self.actsizey = 500/100
        self.currentsizex = self.actsizex*mainw
        self.currentsizey = self.actsizey*mainh
        self.current_pos = (mainw/2-self.currentsizex/2, mainh/2-self.currentsizey/2)

    def show(self):
        return Image(source=self.current_img, pos=(self.current_pos))