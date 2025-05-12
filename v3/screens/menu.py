from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "menu"
        self.backround = None
        self.lbl = dp(80)
        self.backupfont = "assets/fontly.ttf"
        self.fontsize = self.lbl/2
        self.font = "assets/default.ttf"
    
    def onplay(self, instance):
        pass

    def generateplaybutton(self, size, centerx, centery):
        return Button(text="play", size_hint=(None, None), size=size, center_x=centerx, center_y=centery, on_press=self.onplay, font_name=self.font, font_size=self.fontsize)

    def updategraphics(self):
        self.lblx = self.center_x
        self.lbly = self.center_y
        self.playbutton = self.generateplaybutton((self.lbl, self.lbl-dp(20)), self.lblx, self.lbly)
        self.playbutton.background_normal = ""
        self.playbutton.background_down = ""
        self.playbutton.background_color = get_color_from_hex("E6D5C3")
        self.playbutton.color = get_color_from_hex("462521")
        self.backround = Image(source="assets/backgroundgradient.png", allow_stretch=True, keep_ratio=False)
        #self.title = Label(text="hi", color=(0, 0, 0, 1),  pos=(self.playbutton.pos[0], self.playbutton.pos[1]+dp(self.lbly+20)))
        self.title = Label(text="Chip's Adventure", font_name=self.backupfont, color=get_color_from_hex("462521"), size_hint=(None, None), center_x=self.lblx, center_y=self.lbly+dp(self.lbly/5), font_size=dp(60))
        self.add_widget(self.backround)
        self.add_widget(self.playbutton)
        self.add_widget(self.title)

    def update(self):
        self.updategraphics()