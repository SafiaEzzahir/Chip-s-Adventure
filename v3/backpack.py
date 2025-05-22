from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp

class Backpack():
    def __init__(self, allowed_dict, sizes):
        self.allowed_dict = allowed_dict
        self.sizes = sizes
        self.signal_number = 2

        self.corn_img = Image(source="assets/corn.png")
        self.corn_layout = BoxLayout()
        self.corn_layout.add_widget(self.corn_img)
        self.corn_layout.add_widget(Label(text=str(allowed_dict["corn"]), size_hint=(.1, 1)))

        self.footprint_img = Image(source="assets/footprints.png")
        self.footprint_layout = BoxLayout()
        self.footprint_layout.add_widget(self.footprint_img)
        self.footprint_layout.add_widget(Label(text=str(allowed_dict["footprints"]), size_hint=(.1, 1)))

    def is_touched(self, touchx, types):
        signal_width = self.sizes[0]/self.signal_number
        #works out how wide a signal is
        for num in range(0, self.signal_number):
            if touchx >= self.bppos[0] + signal_width*num and touchx < self.bppos[0] + signal_width*(num+1):
                return types[num]

    def update_graphics(self, bppos):
        self.bppos = bppos
        if self.corn_layout.parent:
            self.corn_layout.parent.remove_widget(self.corn_layout)
        if self.footprint_layout.parent:
            self.footprint_layout.parent.remove_widget(self.footprint_layout)
        self.disp = GridLayout(pos=(bppos), size_hint=(None, None), size=self.sizes, cols=3, padding=(dp(10), dp(10)))
        self.disp.add_widget(self.corn_layout)
        self.disp.add_widget(self.footprint_layout)