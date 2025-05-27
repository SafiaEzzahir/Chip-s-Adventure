from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        from chip import Chip
        from characters.fox import Fox
        super().__init__(**kwargs)
        self.name = "level"
        self.chip = Chip()
        self.backround = None

        self.characters = []
        self.fox = Fox((dp(300), dp(250)), self)
        self.characters.append(self.fox)

        self.signal_types = ["corn", "footprint", "phonebox"]
        self.signals = []
        self.corns = []
        self.footprints_used = False
        self.footprints = None

        self.backroundcol = get_color_from_hex("#FFC184")
        self.bpwidth = dp(400)
        self.bpheight = dp(120)
        self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
        
        self.allowed_signals = {"corn": 4, "footprints": 1}
        self.current_allowed_signals = {"corn": 4, "footprints": 1}
        self.current_signal = None
        
        from backpack import Backpack
        self.backpack = Backpack(self.current_allowed_signals, (self.bpwidth, self.bpheight), self.bppos, self.bpwidth, self.bpheight, self)

        self.init_graphics()
        self.init_phoneboxes()
        for char in self.characters:
            self.add_widget(char)
        self.add_widget(self.chip)
        self.add_widget(self.backpack)

    def init_phoneboxes(self):
        from signals import PhoneBox
        box1 = (0, 0)
        box2 = (120, 0)
        box3 = (400, 0)
        self.phoneboxes_positions = [box1]
        self.phoneboxes = []
        for box in self.phoneboxes_positions:
            pb = PhoneBox(box)
            self.phoneboxes.append(pb)
            self.add_widget(pb)

    def init_graphics(self):
        with self.canvas:
            Color(*self.backroundcol)
            self.backround = Rectangle(size=(self.width, self.height))
            Color(*get_color_from_hex("6E514A"))

    def update_graphics(self):
        self.backround.size = (self.width, self.height)
    
    def update_phoneboxes(self):
        for box in self.phoneboxes:
            b = box.update()
            if b:
                if b.parent == None:
                    self.add_widget(b)

    def on_touch_up(self, touch):
        from signals import Corn, Footprint
        if int(touch.x) < self.bppos[0] or int(touch.y) > self.bppos[1]+self.backpack.size[1]:
            #was the click outside of the backpack? this is if not
            if self.current_signal == "corn":
                if len(self.corns) < self.allowed_signals["corn"] and self.current_allowed_signals["corn"] > 0:
                    #are there any corns left to place? if so, add a corn (below)
                    current_corn = Corn(touch.x, touch.y)
                    self.add_widget(current_corn)
                    self.corns.append(current_corn)
                    self.signals.append(current_corn)
                    self.current_allowed_signals["corn"] -= 1

            elif self.current_signal == "footprint":
                if self.footprints_used == False:
                    self.footprints = Footprint((touch.x, touch.y))
                    self.add_widget(self.footprints)
                    self.footprints_used = True
                    self.current_allowed_signals["footprints"] = 0
                    self.footprints.update()  # <-- make sure first footprint is shown
                else:
                    self.footprints.second_position = (touch.x, touch.y)
                    self.footprints.update()  # <-- triggers second footprint to appear

        else:
            #click was in the backpack, now get which signal was clicked
            if self.current_signal != "footprint":
                self.current_signal = self.backpack.is_touched(touch.x, self.signal_types)
                if self.current_signal == "phonebox":
                    for box in self.phoneboxes:
                        box.ringing = True
                        self.signals.append(box)

        return super().on_touch_up(touch)

    def update(self):
        self.update_graphics()
        if self.footprints != None:
            self.footprints.update()
            if self.footprints.check_if_done() and self.current_signal == "footprint":
                self.current_signal = None

        self.update_phoneboxes()
        for char in self.characters:
            char.update()

        if self.chip.signal_to_remove != None:
            if self.chip.signal_to_remove.type == "corn":
                self.corns.remove(self.chip.signal_to_remove)
                self.remove_widget(self.chip.signal_to_remove)    
            self.signals.remove(self.chip.signal_to_remove)
            self.chip.signal_to_remove = None
            
        self.chip.update(self.signals)
        self.backpack.update(self.current_allowed_signals)
        for corn in self.corns:
            corn.update()

    def is_changed(self):
        return "level"