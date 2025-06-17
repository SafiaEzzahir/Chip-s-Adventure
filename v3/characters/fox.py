from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.audio import SoundLoader
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from math import atan2, degrees

class Fox(Widget):
    def __init__(self, pos, screen, **kwargs):
        super().__init__(**kwargs)

        self.screen = screen
        self.mode = "idle"
        self.type = "enemy"
        self.pos = pos

        self.p1 = pos
        self.p2 = (pos[0], 0)
        self.nextpos = self.p2
        self.speed = 10
        self.angle = 0
        self.rot = Rotate()
        
        with self.canvas:
            PushMatrix()
            self.rot = Rotate(origin=self.center, angle=self.angle)
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/fox.png", size=(dp(137/2), dp(500/2)), pos=pos)
            PopMatrix()

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
        if self.image.pos != self.nextpos:
            self.move_to(self.nextpos)
        else:
            if self.nextpos == self.p1:
                self.nextpos = self.p2
            elif self.nextpos == self.p2:
                self.nextpos = self.p1

    def move_to(self, target):
        dx = target[0] - self.image.pos[0]
        dy = target[1] - self.image.pos[1]
        #pythagoras theorem to find diagonal
        dist = (dx**2 + dy**2) ** 0.5

        if dist < self.speed:
            newx = target[0]
            newy = target[1]
            self.image.pos = (newx, newy)
            return

        step_x = dx / dist * self.speed
        step_y = dy / dist * self.speed

        newx = self.image.pos[0] + step_x
        newy = self.image.pos[1] + step_y
        self.image.pos = (newx, newy)

        self.angle = degrees(atan2(dy, dx))
        self.rot.angle = 90-self.angle
        self.rot.origin = (self.image.pos[0]+self.image.size[0]/2, self.image.pos[1]+self.image.size[1]/2)

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
        #if self.sound_count == 0:
        #    return True
        #else:
        #    return False
        return False

    def update(self):
        self.posx = self.image.pos[0]
        self.posy = self.image.pos[1]
        if self.mode == "idle":
            #self.make_sound()
            self.idle()
        elif self.mode == "chase":
            self.chase()