from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.vector import Vector

class Chip(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = "idle"
        self.target = None
        self.speed = 10
        self.signal_responses = {
            "footprint": self.move_to
        }
        self.posx = dp(0)
        self.posy = dp(0)
        self.sizes = (dp(345/5), dp(500/5))
        self.manage_count = 0
        self.nearest = None
        self.signal_to_remove = None

        #self.image = Image(source="assets/chipright.png", size_hint=(None, None), size=self.sizes, pos=(self.posx, self.posy))
        self.source = "assets/chipright.png"
        self.size_hint = (None, None)
        self.size = self.sizes
        self.pos = (self.posx, self.posy)

    def move_to(self, signal, signals, target_posx, target_posy):
        self.posx_center = self.pos[0]+self.sizes[0]
        self.posy_center = self.pos[1]+self.sizes[1]/2
        dx = target_posx - self.posx_center
        dy = target_posy - self.posy_center
        dist = (dx**2 + dy**2) ** 0.5

        if dist < self.speed:
        # Already at the target
            self.pos[0] = target_posx - self.sizes[0]
            self.pos[1] = target_posy - self.sizes[1]/2
            self.state = "arrived"
            if signal in signals:
                self.signal_to_remove = signal
            return
        # Normalize direction and step
        step_x = dx / dist * self.speed
        step_y = dy / dist * self.speed
        # Update position
        self.pos[0] = self.pos[0] + step_x
        self.pos[1] = self.pos[1] + step_y

    def distance_to(self, posx, posy):
        return Vector((self.pos[0], self.pos[1]+self.sizes[1]/2)).distance((posx, posy))

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
        if self.manage_count == 0:
            self.nearest = self.find_nearest_signal(signals)
        if self.nearest:
            self.move_to(self.nearest, signals, self.nearest.posx, self.nearest.posy)
        if self.manage_count == 10:
            self.manage_count = 0
        else:
            self.manage_count += 1

    def update(self, signals):
        self.update_state(signals)