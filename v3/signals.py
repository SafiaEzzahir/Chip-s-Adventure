from kivy.uix.image import Image
from kivy.metrics import dp

class Corn():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def update(self):
        return Image(size_hint=(None, None), pos=(self.posx, self.posy), source="assets/corn.png", size=(dp(40), dp(40)))