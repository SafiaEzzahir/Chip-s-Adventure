from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.audio import SoundLoader
import random

class Fox(Widget):
    def __init__(self, pos, screen, **kwargs):
        super().__init__(**kwargs)

        self.screen = screen
        self.mode = "idle"
        self.type = "enemy"
        
        with self.canvas:
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/fox.png", size=(dp(137/2), dp(500/2)), pos=pos)

        self.posx = pos[0]
        self.posy = pos[1]

        self.init_sound()
        
    def init_sound(self):
        self.growl = SoundLoader.load("assets/foxgrowl.mp3")
        self.sound_count = 0
        self.sound_randomness = 80
        self.return_to_default_image = 15

    def where_is_chip(self):
        chip = self.screen.chip
        return False
        #if chip.is_it_fox_signal:
        #    self.mode = "chase"

    def idle_animation(self):
        pass

    def idle(self):
        self.idle_animation()
        if self.where_is_chip():
            self.mode = "chase"

    def chase(self):
        pass

    def make_sound(self):
        self.sound_count += 1
        if self.sound_count == self.sound_randomness:
            self.image.source = "assets/foxgrowl.png"
            self.growl.play()
            self.sound_count = 0
        elif self.sound_count == self.return_to_default_image:
            self.image.source = "assets/fox.png"

    def is_making_sound(self):
        if self.sound_count == 0:
            return True
        else:
            return False

    def update(self):
        self.make_sound()
        if self.mode == "idle":
            self.idle()
        elif self.mode == "chase":
            self.chase()