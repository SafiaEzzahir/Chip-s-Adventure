from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class Fox(Widget):
    def __init__(self, pos, screen, **kwargs):
        super().__init__(**kwargs)

        self.screen = screen
        self.mode = "idle"
        
        with self.canvas:
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/fox.png", size=(dp(137/2), dp(500/2)), pos=pos)

    def where_is_chip(self):
        chip = self.screen.chip
        #if chip.is_it_fox_signal:
        #    self.mode = "chase"

    def update(self):
        self.where_is_chip()
        #print(self.mode)