from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.label import Label

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "menu"
        self.backround = None
        self.mb_colr = 1
        self.mb_colg = 0.7922
        self.mb_colb = 0.686275
        self.lbl = 40
        self.font = "assets/fontly.ttf"

    def update(self):
        self.play = Label(text="play", size_hint=(None, None), size=("80dp", "80dp"), pos=(self.center_x-self.lbl, self.center_y-self.lbl), font_name=self.font)
        with self.canvas:
            Color(self.mb_colr, self.mb_colg, self.mb_colb)
            self.backround = Rectangle(size=self.size)
        self.add_widget(self.play)