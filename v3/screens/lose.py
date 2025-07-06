from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

class TryAgainButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.pressed)
        self.background_color = (1, 1, 1, 1)
        self.background_normal = "assets/homeicon.png"
        self.background_down = "assets/homeicon.png"
        self.size_hint = (None, None)
        self.size = (dp(50), dp(50))

        self.nextlevel = False

    def pressed(self, instance):
        self.nextlevel = True

    def default(self):
        self.nextlevel = False

class LoseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "lose"

        with self.canvas:
            Color(1, 1, 1, 1)
            self.background_rect = Rectangle(pos=(0, 0), size=(self.width, self.height))

        self.label = Label(text="you lose")
        self.button = TryAgainButton()

        self.add_widget(self.label)
        self.add_widget(self.button)

    def fox(self):
        pass

    def confusion(self):
        print("here")
        with self.canvas:
            Color(1, 0, 1, 1)
            self.background_rect = Rectangle(pos=(0, 0), size=(self.width, self.height))

    def update(self):
        self.background_rect.size = (self.width, self.height)

        self.label.pos = self.label.pos
        self.button.pos = self.button.pos
        
        if "loss" in self.parent.new_data:
            if self.parent.new_data["loss"] == "confusion":
                self.confusion()

        return self.parent.new_data

    def is_changed(self):
        if self.button.nextlevel:
            self.button.nextlevel = False
            return "level"
        else:
            return "lose"