from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import Clock
from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image

class MainWidget(Widget):

    baaground = None
    mb_colr, mb_colg, mb_colb = 1, 0.7922, 0.686275

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from chip import Chip
        from text import Text
        self.chip = Chip(self.width, self.height)
        self.intro = Text()
        self.intro.inittext("this is chip:", "assets/fontly.ttf", (0, 0, 0))
        self.init_background()
        Clock.schedule_interval(self.update, 1.0/30.0)

    def init_background(self):
        with self.canvas:
            Color(self.mb_colr, self.mb_colg, self.mb_colb)
            self.baaground = Rectangle(size=self.size)

    def update_background(self):
        with self.canvas:
            Color(self.mb_colr, self.mb_colg, self.mb_colb)
            self.baaground = Rectangle(size=self.size)

    def update(self, dt):
        self.update_background()
        with self.canvas:
            Color(None)
            self.chip.current_pos = (self.width/2 - self.chip.currentsizex/2, self.height/2 - self.chip.currentsizey/2)
            self.chip.show()
        self.add_widget(self.intro.show())

class Version1app(App):
    def build(self):
        return MainWidget()

Version1app().run()