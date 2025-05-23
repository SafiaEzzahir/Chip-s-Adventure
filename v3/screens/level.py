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

        self.signal_types = ["corn", "footprint", "phonebox"]
        self.signals = []
        self.corns = []
        self.footprints_used = False
        self.footprints = None

        self.init_phoneboxes()

        self.backroundcol = get_color_from_hex("#FFC184")
        self.bpwidth = dp(400)
        self.bpheight = dp(120)
        self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
        
        self.allowed_signals = {"corn": 4, "footprints": 1}
        self.current_allowed_signals = {"corn": 4, "footprints": 1}
        self.current_signal = None
        
        self.backpackback = None

    def init_phoneboxes(self):
        from signals import PhoneBox
        box1 = (0, 0)
        box2 = (120, 0)
        box3 = (400, 0)
        self.phoneboxes_positions = [box1, box2, box3]
        self.phoneboxes = []
        for box in self.phoneboxes_positions:
            self.phoneboxes.append(PhoneBox(box))
            print("box")

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
    
    def update_phoneboxes(self):
        for box in self.phoneboxes:
            self.add_widget(box.update())

    def on_touch_up(self, touch):
        from signals import Corn, Footprint
        if int(touch.x) < self.bppos[0] or int(touch.y) > self.bppos[1]+self.backpack.sizes[1]:
            #was the click outside of the backpack? this is if not
            if self.current_signal == "corn":
                if len(self.corns) < self.allowed_signals["corn"]:
                    #are there any corns left to place? if so, add a corn (below)
                    current_corn = Corn(touch.x, touch.y)
                    self.corns.append(current_corn)
                    self.signals.append(current_corn)

            elif self.current_signal == "footprint":
                if self.footprints_used == False:
                    self.footprints = Footprint((touch.x, touch.y))
                    self.footprints_used = True
                    self.current_allowed_signals["footprints"] = 0
                else:
                    if self.footprints.mode == "shoesdown":
                        self.footprints.second_position = (touch.x, touch.y)
                    elif self.footprints.mode == "trackfinished":
                        self.current_signal = None

        else:
            #click was in the backpack, now get which signal was clicked
            if self.current_signal != "footprint":
                self.current_signal = self.backpack.is_touched(touch.x, self.signal_types)

        return super().on_touch_up(touch)

    def update(self):
        self.update_graphics()
        
        if self.footprints != None:
            self.add_widget(self.footprints.update())

        self.update_phoneboxes()
        
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