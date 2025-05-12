from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "menu"
        self.backround = None
        self.lbl = dp(80)
        self.font = "assets/fontly.ttf"
        self.fontsize = self.lbl/2
    
    def onplay(self, instance):
        pass

    def generateplaybutton(self, size, pos):
        return Button(text="play", size_hint=(None, None), size=size, pos=pos, on_press=self.onplay, font_name=self.font, font_size=self.fontsize)

    def update(self):
        self.lblx = self.center_x-self.lbl/2
        self.lbly = self.center_y-self.lbl/2
        self.playbutton = self.generateplaybutton((self.lbl, self.lbl-dp(20)), (self.lblx, self.lbly))
        self.playbutton.background_normal = ""
        self.playbutton.background_down = ""
        self.add_widget(self.playbutton)