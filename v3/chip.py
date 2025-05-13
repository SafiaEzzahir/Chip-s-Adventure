from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.metrics import dp

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
        self.posx = dp(50)
        self.posy = dp(200)
        self.sizes = (dp(345), dp(500))

    def move_to(self):
        pass

    def get_chip_pic(self):
        return Image(source="assets/chipleft.png", size_hint=(None, None), size=self.sizes,  pos=(self.posx, self.posy))

    def updategraphics(self):
        pass

    def update(self):
        self.updategraphics()