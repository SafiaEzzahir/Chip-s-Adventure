from kivy.uix.image import Image
from kivy.metrics import dp

class Corn():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.sizes = dp(40)

    def update(self):
        return Image(size_hint=(None, None), pos=(self.posx-self.sizes/2, self.posy-self.sizes/2), source="assets/corn.png", size=(self.sizes, self.sizes))