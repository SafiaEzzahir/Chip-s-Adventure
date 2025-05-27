from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class Corn(Image):
    def __init__(self, posx, posy, **kwargs):
        super().__init__(**kwargs)
        self.posx = posx
        self.posy = posy
        self.sizes = dp(40)
        self.type = "corn"
        self.poss = (self.posx-self.sizes/2, self.posy-self.sizes/2)

        self.size_hint = (None, None)
        self.pos = self.poss
        self.source = "assets/corn.png"
        self.size = (self.sizes, self.sizes)

    def update(self):
        self.pos = self.poss

class Footprint(FloatLayout):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.type = "footprint"
        self.mode = "footdown"
        self.position = position
        self.second_position = None
        self.sizes = (dp(50), dp(50))

        self.has_first_foot = False
        self.has_second_foot = False

        self.lastx = 0
        self.lasty = 0

    def check_if_done(self):
        if self.mode == "trackfinished":
            # if the track is finished, return True
            return True

    def footdown(self):
        # check if the first footprint is already down
        if not self.has_first_foot:
            self.add_widget(Image(size_hint=(None, None), size=self.sizes, source="assets/footprints.png", pos=self.position))
            self.has_first_foot = True
            self.mode = "shoesdown"

    def shoesdown(self):
        if self.second_position and not self.has_second_foot: # if second_position exists and second footprint is not down
            self.add_widget(Image(size_hint=(None, None), size=self.sizes, source="assets/footprints.png", pos=self.second_position))
            self.has_second_foot = True
            self.mode = "trackdown"

    def trackdown(self):
        # Calculate center points for start and end
        x1, y1 = self.position[0] + self.sizes[0] / 2, self.position[1] + self.sizes[1] / 2
        x2, y2 = self.second_position[0] + self.sizes[0] / 2, self.second_position[1] + self.sizes[1] / 2
        dx = x2 - x1
        dy = y2 - y1
        distance = (dx**2 + dy**2) ** 0.5
        step_size = self.sizes[0]  # use width, or make this a parameter
        steps = max(1, int(distance // step_size))
        for i in range(1, steps + 1):
            t = i / (steps + 1)
            x = x1 + dx * t
            y = y1 + dy * t
            self.add_widget(Image(size_hint=(None, None), size=self.sizes, source="assets/footprints.png", pos=(x - self.sizes[0] / 2, y - self.sizes[1] / 2)))
        self.mode = "trackfinished"

    def update(self):
        if self.mode == "footdown":
            self.footdown()
            return 
        elif self.mode == "shoesdown":
            self.shoesdown()
        elif self.mode == "trackdown":
            self.trackdown()
        
class PhoneBox(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.pos = (350, 200)
        self.ring = SoundLoader.load("assets/phonering.wav")
        self.ringing = False
        self.ringing_count = 0
        self.type = "phonebox"

        self.posx = self.pos[0]
        self.posy = self.pos[1]

        with self.canvas:
            Color(1, 1, 1, 1)
            self.image = Rectangle(source="assets/phoneboxtop.png", pos=self.pos, size=(dp(500/5), dp(500/5)))
        with self.canvas.before:
            PushMatrix()
            self.rotator = Rotate(angle=0, origin=self.center)
        with self.canvas.after:
            PopMatrix()

    def ringing_image(self):
        self.size = self.image.size
        self.rotator.origin = self.center
        anim = Animation(angle=0, duration=0.1)
        for i in range(0, 4):
            anim += Animation(angle=5, duration=0.05) + Animation(angle=10, duration=0.01) + Animation(angle=0, duration=0.025) + Animation(angle=-5, duration=0.05) + Animation(angle=-10, duration=0.01) + Animation(angle=0, duration=0.025)
        anim.start(self.rotator)
        return self

    def update(self):
        if self.ringing == True:
            self.ring.play()
            self.ringing = False
            return self.ringing_image()
        return self

