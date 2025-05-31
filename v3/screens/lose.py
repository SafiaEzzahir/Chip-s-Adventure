from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label

class LoseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "lose"

    def update(self):
        self.add_widget(Label(text="you lose"))

    def is_changed(self):
        return "lose"