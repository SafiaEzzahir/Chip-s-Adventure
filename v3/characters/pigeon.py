from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class Pigeon(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_making_sound(self):
        return False

    def update(self):
        pass