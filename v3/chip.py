from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.vector import Vector
from kivy.uix.floatlayout import FloatLayout

class Chip(FloatLayout):
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
        self.sizes = (dp(345/2), dp(500/2))

    def move_to(self, signal, signals, target_posx, target_posy):
        dx = target_posx - self.posx
        dy = target_posy - self.posy
        dist = (dx**2 + dy**2) ** 0.5

        if dist < 1:
        # Already at the target
            self.posx = target_posx
            self.posy = target_posy
            self.state = "arrived"
            signals.remove(signal)
            return
        # Normalize direction and step
        step_x = dx / dist * self.speed
        step_y = dy / dist * self.speed
        # Update position
        self.posx = self.posx + step_x
        self.posy = self.posy + step_y

    def get_chip_pic(self):
        return Image(source="assets/chipright.png", size_hint=(None, None), size=self.sizes, pos=(self.posx, self.posy))

    def updategraphics(self):
        pass

    def distance_to(self, posx, posy):
        return Vector(*self.pos).distance((posx, posy))

    def find_nearest_signal(self, signals):
        shortest_distance = float("inf")
        nearest_signal = None
        for signal in signals:
            dist = self.distance_to(signal.posx, signal.posy)
            if dist is not None and dist < shortest_distance:
                shortest_distance = dist
                nearest_signal = signal
        return nearest_signal
    
    def update_state(self, signals):
        nearest = self.find_nearest_signal(signals)
        if nearest:
            self.move_to(nearest, signals, nearest.posx, nearest.posy)

    def update(self, signals):
        self.update_state(signals)
        self.updategraphics()