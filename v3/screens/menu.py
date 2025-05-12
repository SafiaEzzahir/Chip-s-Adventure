from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "menu"
        self.backround = None
        self.mb_colr = 1
        self.mb_colg = 0.7922
        self.mb_colb = 0.686275
        self.lbl = dp(80)
        self.font = "assets/fontly.ttf"
        self.fontsize = self.lbl/2
    
    def onplay(self, instance):
        pass

    def update(self):
        self.lblx = self.center_x-self.lbl/2
        self.lbly = self.center_y-self.lbl/2
        with self.canvas:
            Color(self.mb_colr, self.mb_colg, self.mb_colb)
            self.backround = Rectangle(size=self.size)
        self.playbutton = Button(text="play", size_hint=(None, None), size=(self.lbl, self.lbl-dp(20)), pos=(self.lblx, self.lbly), on_press=self.onplay, font_name=self.font, font_size=self.fontsize)
        self.add_widget(self.playbutton)