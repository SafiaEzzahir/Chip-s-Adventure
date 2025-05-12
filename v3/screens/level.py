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
        #self.background_color = get_color_from_hex("FFC184")

    def update_graphics(self):
        self.add_widget(self.chip.get_chip_pic())

    def update(self):
        self.update_graphics()

    def is_changed(self):
        return "level"