from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class Backpack():
    def __init__(self, allowed_dict, sizes):
        self.allowed_dict = allowed_dict
        self.sizes = sizes

        self.corn_img = Image(source="assets/corn.png")
        self.corn_layout = BoxLayout()
        self.corn_layout.add_widget(self.corn_img)
        self.corn_layout.add_widget(Label(text=str(allowed_dict["corn"]), size_hint=(.1, 1)))

        self.footprint_img = Image(source="assets/footprints.png")
        self.footprint_layout = BoxLayout()
        self.footprint_layout.add_widget(self.footprint_img)
        self.footprint_layout.add_widget(Label(text=str(allowed_dict["footprints"]), size_hint=(.1, 1)))

    def update_graphics(self, bppos):
        if self.corn_layout.parent:
            self.corn_layout.parent.remove_widget(self.corn_layout)
        if self.footprint_layout.parent:
            self.footprint_layout.parent.remove_widget(self.footprint_layout)
        self.disp = GridLayout(pos=(bppos), size_hint=(None, None), size=self.sizes, cols=3)
        self.disp.add_widget(self.corn_layout)
        self.disp.add_widget(self.footprint_layout)