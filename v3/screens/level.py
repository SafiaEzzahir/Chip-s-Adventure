from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from kivy.uix.button import Button

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        from chip import Chip
        super().__init__(**kwargs)
        self.name = "level"
        self.chip = Chip(self)
        self.backround = None
        self.backpack = None
        self.backroundcol = get_color_from_hex("#FFC184")
        self.corns = []
        self.bpwidth = dp(400)
        self.bpheight = dp(120)
        self.bppos = (self.width-self.bpwidth-dp(5), dp(5))

    def update_backpack(self):
        with self.canvas:
            Color(*get_color_from_hex("6E514A"))
            self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
            self.backpack = Rectangle(size=(self.bpwidth, self.bpheight), pos=(self.width-self.bpwidth-dp(5), dp(5)))

    def update_graphics(self):
        with self.canvas:
            Color(*self.backroundcol)
            self.backround = Rectangle(size=(self.width, self.height))
            Color(*get_color_from_hex("6E514A"))
    
    def on_touch_up(self, touch):
        from signals import Corn
        self.corns.append(Corn(touch.x, touch.y))
        return super().on_touch_up(touch)

    def update(self):
        self.update_graphics()
        for corn in self.corns:
            c = corn.update((self.bppos[0], self.bppos[1]+self.bpheight))
            if c != None:
                self.add_widget(c)
            else:
                self.corns.remove(corn)
            
        self.chip.update(self.corns)
        self.add_widget(self.chip.get_chip_pic())
        self.update_backpack()
        #print(self.corns)

    def is_changed(self):
        return "level"