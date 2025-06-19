from kivy.uix.button import Button
from kivy.metrics import dp

class Map(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(on_press=self.pressed)
        self.background_color = (1, 1, 1, 1)
        self.background_normal = "assets/mapicon.png"
        self.background_down = "assets/mapicon2.png"
        self.size_hint = (None, None)
        self.size = (dp(50), dp(50))

        self.mapscreen = False

    def pressed(self, instance):
        self.mapscreen = True

    def update(self, screen):
        self.pos = (dp(5), screen.height-self.height-dp(5))