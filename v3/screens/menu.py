from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "menu"
        self.button = Button()

    def update(self, screen):
        with screen.canvas:
            Color(1, 0, 0)
            Rectangle(size=(500, 500), pos=(50, 50))
            Color(1, 1, 1)
        self.button