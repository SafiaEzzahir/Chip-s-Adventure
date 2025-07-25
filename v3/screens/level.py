from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        from chip import Chip
        from characters.fox import Fox
        from level_objects.signals import Footprint
        from screens.levels import LevelManager
        super().__init__(**kwargs)
        self.name = "level"
        self.current_level = "level"
        self.level_number = 1
        self.old_level = 1
        self.levelmanager = LevelManager(self.level_number)
        self.chip = Chip()

        self.loss = "none"

        self.characters = []
        for key in self.levelmanager.chars:
            if key == "fox":
                self.characters.append(Fox(self.levelmanager.chars[key], self))
            else:
                print("error")

        self.signal_types = ["corn", "footprint", "phonebox"]
        self.signals = []
        self.corns = []
        self.footprints_used = False
        self.footprints = Footprint()

        self.allowed_signals = self.levelmanager.allowed_signals
        self.current_allowed_signals = self.allowed_signals
        self.current_signal = None

        self.bpwidth = dp(400)
        self.bpheight = dp(120)
        self.bppos = (self.width-self.bpwidth-dp(5), dp(5))
        
        from level_objects.backpack import Backpack
        self.backpack = Backpack(self.current_allowed_signals, (self.bpwidth, self.bpheight), self.bppos, self.bpwidth, self.bpheight, self)

        self.init_graphics()
        self.init_target()
        self.add_widget(self.footprints)
        self.init_phoneboxes()
        for char in self.characters:
            self.add_widget(char)
        self.add_widget(self.chip)
        self.add_widget(self.backpack)
        self.init_map()

    def init_map(self):
        from level_objects.mapobj import Map
        self.map = Map()
        self.add_widget(self.map)

    def init_target(self):
        with self.canvas:
            Color(0, 1, 0, 1)
            self.target = Rectangle(pos=(self.width-dp(60), self.height-dp(60)), size=(dp(50), dp(50)))

    def init_phoneboxes(self):
        from level_objects.signals import PhoneBox
        self.phoneboxes_positions = self.levelmanager.phoneboxes
        self.phoneboxes = []
        for box in self.phoneboxes_positions:
            pb = PhoneBox(box)
            self.phoneboxes.append(pb)
            self.add_widget(pb)

    def init_graphics(self):
        with self.canvas:
            Color(*get_color_from_hex(self.levelmanager.backgroundcol))
            self.backround = Rectangle(size=(self.width, self.height))
            Color(*get_color_from_hex("6E514A"))

    def update_map(self):
        self.map.update(self)
        if self.map.mapscreen:
            self.current_level = "map"
            self.map.default()

    def update_graphics(self):
        self.backround.size = (self.width, self.height)
    
    def update_phoneboxes(self):
        for box in self.phoneboxes:
            b = box.update()
            if b:
                if b.parent == None:
                    self.add_widget(b)

    def on_touch_up(self, touch):
        from level_objects.signals import Corn
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
                    self.footprints.init((touch.x, touch.y))
                    self.footprints_used = True
                    self.current_allowed_signals["footprints"] -= 1
                    self.footprints.update()  # <-- make sure first footprint is shown
                else:
                    self.footprints.second_position = (touch.x, touch.y)
                    self.footprints.update()  # <-- triggers second footprint to appear
                    self.signals.append(self.footprints)

        else:
            #click was in the backpack, now get which signal was clicked
            if self.current_signal != "footprint":
                self.current_signal = self.backpack.is_touched(touch.x, self.signal_types)
                if self.current_signal == "phonebox":
                    for box in self.phoneboxes:
                        box.ringing = True
                        self.signals.append(box)

        return super().on_touch_up(touch)
    
    def winning_pos(self):
        x = self.chip.x + self.chip.width
        y = self.chip.y + self.chip.height
        if y >= self.target.pos[1] and x >= self.target.pos[0]:
            return True
        else:
            return False

    def did_you_win(self):
        count = 0
        for key in self.current_allowed_signals:
            if self.current_allowed_signals[key] == 0:
                count+=1
        if count == len(self.current_allowed_signals) and self.signals==[]:
            if self.winning_pos():
                self.current_level = "win"
                self.level_number +=1
            #else:
            #    self.current_level = "lose"
            #    self.reset()
            else:
                self.chip.event_happens("no signal")

        if self.chip.confusion.value <= -12:
            self.current_level = "lose"
            self.loss = "confusion"
            self.reset()

    def new_level(self):
        if self.old_level != self.level_number:
            self.reset()

    def reset(self):
        self.clear_widgets()

        self.old_level += 1

        from characters.fox import Fox
        from screens.levels import LevelManager
        from level_objects.signals import Footprint

        self.levelmanager = LevelManager(self.level_number)

        self.chip.reset()

        self.characters = []
        for key in self.levelmanager.chars:
            if key == "fox":
                self.characters.append(Fox(self.levelmanager.chars[key], self))
            else:
                print("error")

        self.signal_types = ["corn", "footprint", "phonebox"]
        self.signals = []
        self.corns = []
        self.footprints_used = False
        self.footprints = Footprint()

        self.allowed_signals = self.levelmanager.allowed_signals
        self.current_allowed_signals = self.allowed_signals
        self.current_signal = None
        
        from level_objects.backpack import Backpack
        self.backpack = Backpack(self.current_allowed_signals, (self.bpwidth, self.bpheight), self.bppos, self.bpwidth, self.bpheight, self)

        self.init_graphics()
        self.init_target()
        self.add_widget(self.footprints)
        self.init_phoneboxes()
        for char in self.characters:
            self.add_widget(char)
        self.add_widget(self.chip)
        self.add_widget(self.backpack)
        self.init_map()

    def update(self):
        self.current_level = "level"
        self.new_level()
        self.update_graphics()
        self.target.pos = (self.width-dp(60), self.height-dp(60))

        if self.footprints != None:
            self.footprints.update()
            if self.footprints.check_if_done() and self.current_signal == "footprint":
                self.current_signal = None

        self.update_phoneboxes()

        for char in self.characters:
            char.update()
            if char.is_making_sound() and char not in self.signals:
                self.signals.append(char)

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

        self.update_map()

        self.did_you_win()

        return {"loss": self.loss}

    def is_changed(self):
        return self.current_level