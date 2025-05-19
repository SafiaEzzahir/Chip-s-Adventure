from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class Backpack():
    def __init__(self, allowed_dict, sizes):
        self.allowed_dict = allowed_dict
        self.sizes = sizes
        self.corn_img = Image(source="assets/corn.png")

    def update_graphics(self, bppos):
        if self.corn_img.parent:
            self.corn_img.parent.remove_widget(self.corn_img)
        self.disp = GridLayout(pos=(bppos), size_hint=(None, None), size=self.sizes, cols=3)
        self.disp.add_widget(self.corn_img)