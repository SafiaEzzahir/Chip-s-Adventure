from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from kivy.animation import Animation
from kivy.uix.widget import Widget

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

    def check_pos(self, bppos):
        if self.poss[0]>=bppos[0] and self.poss[1]<=bppos[1]:
            return None
        else:
            return self

    def update(self, bppos):
        return self.check_pos(bppos)

class Footprint():
    def __init__(self, position):
        self.type = "footprint"
        self.mode = "footdown"
        self.position = position
        self.sizes = (dp(50), dp(50))
        self.second_position = position

    def footdown(self):
        self.mode = "shoesdown"
        return Image(size_hint=(None, None), size=(self.sizes), source="assets/footprints.png", pos=self.position)

    def shoesdown(self):
        layout = FloatLayout()
        layout.add_widget(self.footdown())
        layout.add_widget(Image(size_hint=(None, None), size=(self.sizes), source="assets/footprints.png", pos=self.second_position))
        return layout

    def trackdown(self):
        pass

    def trackfinished(self):
        pass

    def update(self):
        if self.mode == "footdown":
            return self.footdown()
        elif self.mode == "shoesdown":
            return self.shoesdown()
        elif self.mode == "trackdown":
            return self.trackdown()
        elif self.mode == "trackfinished":
            return self.trackfinished()
        
class PhoneBox(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.pos = pos
        self.image = Image(source="assets/phonebox.png", pos=self.pos, size=(dp(194), dp(500)), size_hint=(None, None))
        self.ring = SoundLoader.load("assets/phonering.wav")
        self.ringing = False
        self.add_widget(self.image)
        self.ringing_count = 0

        with self.image.canvas.before:
            PushMatrix()
            self.rotator = Rotate(angle=0, origin=self.image.center)
        with self.image.canvas.after:
            PopMatrix()

    def ringing_image(self):
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

