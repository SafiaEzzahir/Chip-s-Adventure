from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "level"

    def update(self, screen):
        with screen.canvas:
            Color(0, 0, 1)
            Rectangle(size=(500, 500), pos=(50, 50))