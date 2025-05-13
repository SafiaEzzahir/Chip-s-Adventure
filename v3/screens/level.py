from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        from chip import Chip
        super().__init__(**kwargs)
        self.name = "level"
        self.chip = Chip(self)
        self.backround = None
        self.backroundcol = get_color_from_hex("#FFC184")
        self.corns = []

    def update_graphics(self):
        with self.canvas:
            Color(*self.backroundcol)
            self.backround = Rectangle(size=(self.width, self.height))
        self.add_widget(self.chip.get_chip_pic())
    
    def on_touch_up(self, touch):
        from signals import Corn
        print(str(touch.x) + " " + str(touch.y))
        self.corns.append(Corn(touch.x, touch.y))
        return super().on_touch_up(touch)

    def update(self):
        self.update_graphics()
        for corn in self.corns:
            self.add_widget(corn.update())

    def is_changed(self):
        return "level"