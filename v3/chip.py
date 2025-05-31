from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.vector import Vector
from kivy.graphics.context_instructions import Color
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from math import atan2, degrees

class Chip(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = "idle"
        self.target = None
        self.speed = 10
        self.posx = dp(0)
        self.posy = dp(0)
        self.sizes = (dp(100), dp(100))
        self.manage_count = 0
        self.nearest = None
        self.signal_to_remove = None

        self.size_hint = (None, None)
        self.size = self.sizes
        self.pos = (self.posx, self.posy)

        self.angle = 0
        self.rot = Rotate()

        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.center, angle=self.angle)
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/chip.png", size=self.sizes, pos=self.pos)
            PopMatrix()

    def move_towards(self, target_x, target_y):
        center_x = self.pos[0] + self.sizes[0]
        center_y = self.pos[1] + self.sizes[1] / 2

        dx = target_x - center_x
        dy = target_y - center_y
        dist = (dx**2 + dy**2) ** 0.5

        if dist < self.speed:
            self.pos[0] = target_x - self.sizes[0]
            self.pos[1] = target_y - self.sizes[1] / 2
            self.state = "arrived"
            return

        step_x = dx / dist * self.speed
        step_y = dy / dist * self.speed

        self.pos[0] += step_x
        self.pos[1] += step_y
        self.image.pos = self.pos

        self.angle = degrees(atan2(dy, dx))
        self.rot.angle = self.angle
        self.rot.origin = self.center

    def move_to(self, signal, signals, target_posx, target_posy):
        self.move_towards(target_posx, target_posy)
        if self.state == "arrived" and signal in signals:
            self.signal_to_remove = signal
            if signal.type == "footprint":
                self.state = "following footsteps"

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
                self.state = "moving"
        return nearest_signal
    
    def follow_footsteps(self):
        self.move_towards(self.nearest.second_posx, self.nearest.second_posy)
    
    def update_state(self, signals):
        if self.nearest:
            if self.state in  ["moving", "arrived"]:
                self.move_to(self.nearest, signals, self.nearest.posx, self.nearest.posy)
            
        if self.state == "following footsteps":
            self.follow_footsteps()
        else:
            self.nearest = self.find_nearest_signal(signals)

    def update(self, signals):
        self.update_state(signals)
        self.rot.angle = self.angle
        self.rot.origin = self.center
        self.image.pos = self.pos