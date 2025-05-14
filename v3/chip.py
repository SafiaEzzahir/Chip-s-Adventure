from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.vector import Vector

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
        self.nearest_signal = None

    def move_to(self):
        pass

    def get_chip_pic(self):
        return Image(source="assets/chipright.png", size_hint=(None, None), size=self.sizes,  pos=(self.posx, self.posy))

    def updategraphics(self):
        pass

    def distance_to(self, posx, posy):
        return Vector(*self.pos).distance((posx, posy))

    def find_nearest_signal(self, signals):
        shortest_distance = float("inf")
        for signal in signals:
            dist = self.distance_to(signal.posx, signal.posy)
            if dist is not None and dist < shortest_distance:
                shortest_distance = dist
                self.nearest_signal = signal
        return self.nearest_signal

    def update(self, signals):
        self.find_nearest_signal(signals)
        self.updategraphics()