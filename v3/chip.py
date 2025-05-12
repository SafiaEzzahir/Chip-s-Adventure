from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image

class Chip(Widget):
    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)
        self.state = "idle"
        self.target = None
        self.speed = 2
        self.screen = screen
        self.signal_responses = {
            "footprint": self.move_to
        }

    def move_to(self):
        pass

    def get_chip_pic(self):
        return Image(source="assets/chipleft.png")

    def updategraphics(self):
        pass

    def update(self):
        self.updategraphics()