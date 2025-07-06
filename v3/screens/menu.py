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
        self.change = "menu"

        self.lblx = self.center_x
        self.lbly = self.center_y

        self.darkestbrown = get_color_from_hex("462521")
        self.cream = get_color_from_hex("E6D5C3")
        
        self.settings_button = self.generatebutton((self.lbl, self.lbl-dp(40)), self.lblx, self.lbly-dp(self.lbly/6), "settings", self.onsettings)
        self.playbutton = self.generatebutton((self.lbl, self.lbl-dp(20)), self.lblx, self.lbly, "play", self.onplay)
        
        self.playbutton.background_color = self.cream
        self.playbutton.color = self.darkestbrown
        self.settings_button.background_color = self.darkestbrown
        self.settings_button.color = self.cream
        self.settings_button.font_size = dp(20)

        self.backround = Image(source="assets/backgroundgradient.png", allow_stretch=True, keep_ratio=False)
        self.title = Label(text="Chip's Adventure", font_name=self.backupfont, color=get_color_from_hex("462521"),
                            size_hint=(None, None), center_x=self.lblx, center_y=self.lbly+dp(self.lbly/5), 
                            font_size=dp(60))
    
        self.add_widget(self.backround)
        
        buttons = [self.playbutton, self.settings_button]
        for button in buttons:
            button.background_normal = ""
            button.background_down = ""
            self.add_widget(button)
        self.add_widget(self.title)

    def onplay(self, instance):
        self.change = "level"

    def onsettings(self, instance):
        self.change = "settings"

    def is_changed(self):
        return self.change

    def generatebutton(self, size, centerx, centery, text, on_press_function):
        return Button(text=text, size_hint=(None, None), size=size, center_x=centerx, center_y=centery, on_press=on_press_function, font_name=self.backupfont, font_size=self.fontsize)

    def updategraphics(self):
        self.lblx = self.center_x
        self.lbly = self.center_y

        self.settings_button.center_x = self.lblx
        self.settings_button.center_y = self.lbly-dp(self.lbly/6)
        self.playbutton.center_x = self.lblx
        self.playbutton.center_y = self.lbly
        
        self.title.center_x = self.lblx
        self.title.center_y = self.lbly+dp(self.lbly/5)

    def update(self):
        self.updategraphics()
        return {}