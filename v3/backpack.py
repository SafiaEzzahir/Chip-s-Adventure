from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex
from kivy.graphics import Rectangle

class Backpack(GridLayout):
    def __init__(self, allowed_dict, sizes, bppos, bpwidth, bpheight, screen, **kwargs):
        super().__init__(**kwargs)
        self.bppos = bppos
        self.pos = bppos
        self.size_hint = (None, None)
        self.size = sizes
        self.cols = 3
        self.padding = (dp(20), dp(20))
        
        self.screen = screen
        self.bpwidth = bpwidth
        self.bpheight = bpheight

        with self.canvas.before:
            Color(*get_color_from_hex("6E514A"))
            self.bppos = (screen.width-self.bpwidth-dp(5), dp(5))
            self.backpackback = Rectangle(size=(self.bpwidth, self.bpheight), pos=(self.bppos))

        self.allowed_dict = allowed_dict
        self.signal_number = 3

        self.corn_img = Image(source="assets/corn.png")
        self.corn_label = Label(text=str(allowed_dict["corn"]), size_hint=(.1, 1))
        self.corn_layout = BoxLayout()
        self.corn_layout.add_widget(self.corn_img)
        self.corn_layout.add_widget(self.corn_label)

        self.footprint_img = Image(source="assets/footprints.png")
        self.footprint_label = Label(text=str(allowed_dict["footprints"]), size_hint=(.1, 1))
        self.footprint_layout = BoxLayout()
        self.footprint_layout.add_widget(self.footprint_img)
        self.footprint_layout.add_widget(self.footprint_label)

        self.phone_img = Image(source="assets/phoneicon.png")
        self.phone_layout = BoxLayout()
        self.phone_layout.add_widget(self.phone_img)

        self.add_widget(self.corn_layout)
        self.add_widget(self.footprint_layout)
        self.add_widget(self.phone_layout)

    def is_touched(self, touchx, types):
        signal_width = self.size[0]/self.signal_number
        #works out how wide a signal is
        for num in range(0, self.signal_number):
            if touchx >= self.bppos[0] + signal_width*num and touchx < self.bppos[0] + signal_width*(num+1):
                return types[num]
            
    def update(self, allowed_dict):
        self.bppos = (self.screen.width-self.bpwidth-dp(5), dp(5))
        self.pos = self.bppos  # <-- keep widget and rectangle in sync
        self.backpackback.pos = self.bppos
        self.corn_label.text = str(allowed_dict["corn"])
        self.footprint_label.text = str(allowed_dict["footprints"])