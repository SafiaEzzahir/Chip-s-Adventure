from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

class NextButton(Button):
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

class WinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.name = "win"

        self.label = Label(text="you win")
        self.button = NextButton()

        self.add_widget(self.label)
        self.add_widget(self.button)

    def update(self):
        pass

    def is_changed(self):
        if self.button.nextlevel:
            self.button.nextlevel = False
            return "level"
        else:
            return "win"