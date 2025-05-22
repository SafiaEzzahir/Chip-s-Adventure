from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from kivy.uix.button import Button

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        from chip import Chip
        from backpack import Backpack
        super().__init__(**kwargs)
        self.name = "level"
        self.chip = Chip(self)
        self.backround = None

        self.signal_types = ["corn", "footprint"]
        
        self.backroundcol = get_color_from_hex("#FFC184")
        self.signals = []
        self.corns = []
        self.bpwidth = dp(400)
        self.bpheight = dp(120)
        self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
        
        self.allowed_signals = {"corn": 4, "footprints": 1}
        self.current_allowed_signals = {"corn": 4, "footprints": 1}
        #self.backpack = Backpack(self.allowed_signals, (self.bpwidth, self.bpheight))
        self.current_signal = None
        self.backpackback = None

    def update_backpack(self):
        with self.canvas:
            from backpack import Backpack
            self.backpack = Backpack(self.current_allowed_signals, (self.bpwidth, self.bpheight))
            Color(*get_color_from_hex("6E514A"))
            self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
            self.backpackback = Rectangle(size=(self.bpwidth, self.bpheight), pos=(self.bppos))
            self.backpack.update_graphics(self.bppos)

    def update_graphics(self):
        with self.canvas:
            Color(*self.backroundcol)
            self.backround = Rectangle(size=(self.width, self.height))
            Color(*get_color_from_hex("6E514A"))
    
    def on_touch_up(self, touch):
        from signals import Corn
        if int(touch.x) < self.bppos[0] or int(touch.y) > self.bppos[1]+self.backpack.sizes[1]:
            #was the click outside of the backpack? this is if not
            if self.current_signal == "corn":
                if len(self.corns) < self.allowed_signals["corn"]:
                    #are there any corns left to place? if so, add a corn (below)
                    current_corn = Corn(touch.x, touch.y)
                    self.corns.append(current_corn)
                    self.signals.append(current_corn)

            elif self.current_signal == "footprint":
                pass
        else:
            #click was in the backpack, now get which signal was clicked
            self.current_signal = self.backpack.is_touched(touch.x, self.signal_types)

        return super().on_touch_up(touch)

    def update(self):
        self.update_graphics()
        for corn in self.corns:
            c = corn.update((self.bppos[0], self.bppos[1]+self.bpheight))
            if c != None:
                self.add_widget(c)
            else:
                self.corns.remove(corn)
                self.signals.remove(corn)

        if self.chip.signal_to_remove != None:
            self.corns.remove(self.chip.signal_to_remove)
            self.signals.remove(self.chip.signal_to_remove)
            self.chip.signal_to_remove = None
            #print(self.corns)
        
        self.current_allowed_signals["corn"] = 4-len(self.corns)
            
        self.chip.update(self.signals)
        #print(self.corns)
        self.add_widget(self.chip.get_chip_pic())
        self.update_backpack()

    def is_changed(self):
        return "level"