from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class Fox(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas:
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/fox.png", size=(dp(137/2), dp(500/2)), pos=pos)

    def update(self):
        pass