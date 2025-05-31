from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label

class WinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "win"

    def update(self):
        self.add_widget(Label(text="you win"))

    def is_changed(self):
        return "win"