from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "level"

    def update(self):
        self.add_widget(Button(text="hey", background_color=get_color_from_hex("BEA99B")))

    def is_changed(self):
        return "level"