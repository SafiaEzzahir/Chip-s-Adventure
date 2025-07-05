from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.vertex_instructions import Line
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.vector import Vector
from kivy.graphics.context_instructions import Color
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from kivy.core.audio import SoundLoader
from math import atan2, degrees
from random import randint

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

        self.start_confused = False

        self.size_hint = (None, None)
        self.size = self.sizes
        self.pos = (self.posx, self.posy)

        self.init_sound()
        self.init_moods()

        self.angle = 0
        self.rot = Rotate()

        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.center, angle=self.angle)
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/chip.png", size=self.sizes, pos=self.pos)
            PopMatrix()

    def init_sound(self):
        self.chirp = SoundLoader.load("assets/chipchirp.wav")
        self.sound_randomness = 20
        self.sound_count = 0

    def init_moods(self):
        from chipmoods import Hunger, Confusion, Happiness, Fear, Freedom
        self.hunger = Hunger(0)
        self.confusion = Confusion(0)
        self.happiness = Happiness()
        self.fear = Fear()
        self.freedom = Freedom()

    def event_happens(self, event):
        self.hunger.event_reaction(event)
        self.confusion.event_reaction(event)
        self.happiness.event_reaction(event)
        self.fear.event_reaction(event)
        self.freedom.event_reaction(event)

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

    def move_towards2(self, target_x, target_y):
        dx = target_x - self.pos[0]
        dy = target_y - self.pos[1]
        dist = (dx**2 + dy**2) ** 0.5

        if dist < (self.confusion.speed*3/4):
            self.pos[0] = target_x
            self.pos[1] = target_y
            return

        step_x = dx / dist * (self.confusion.speed/8*5)
        step_y = dy / dist * (self.confusion.speed/8*5)

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
            elif signal.type == "corn":
                self.event_happens("corn")

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

    def make_sound(self):
        self.sound_count += 1
        if self.sound_count == self.sound_randomness:
            self.chirp.play()
            self.sound_count = 0

    def confused_animation(self):
        if not self.start_confused:
            x = dp(randint(50, 100))
            y = dp(randint(-100, 100))
            p1 = (self.pos[0]+self.image.size[0]/2-x, self.pos[1]+self.image.size[1]/2+y)
            p2 = (self.pos[0]+x+self.image.size[0]/2, self.pos[1]-y+self.image.size[1]/2)
            self.p1 = (p1[0]-self.image.size[0], p1[1]-self.image.size[1])
            self.p2 = (p2[0]-self.image.size[0], p2[1]-self.image.size[1])
            self.next_pos = self.p1
            self.start_confused = True
        else:
            if (round(self.image.pos[0]), round(self.image.pos[1])) != (round(self.next_pos[0]), round(self.next_pos[1])):
                self.move_towards2(self.next_pos[0], self.next_pos[1])
            else:
                if self.next_pos == self.p1:
                    self.next_pos = self.p2
                elif self.next_pos == self.p2:
                    self.next_pos = self.p1

    def reset(self):
        self.confusion.reset()
        self.hunger.reset()
        self.happiness.reset()
        self.fear.reset()
        self.freedom.reset()

    def update_state(self, signals):
        if self.confusion.feeling == "very bad":
            self.state = "confused"
            self.confusion.change_speed(5)
        elif self.nearest:
            if self.state in  ["moving", "arrived"]:
                self.move_to(self.nearest, signals, self.nearest.posx, self.nearest.posy)
        elif self.confusion.feeling == "bad":
            self.state = "confused"
            self.confusion.change_speed(1)
            
        if self.state == "following footsteps":
            self.follow_footsteps()
        elif self.state == "confused":
            self.confused_animation()
        else:
            self.nearest = self.find_nearest_signal(signals)

    def update(self, signals):
        self.event_happens("time")
        self.update_state(signals)
        self.rot.angle = self.angle
        self.rot.origin = self.center
        self.image.pos = self.pos
        #self.make_sound()