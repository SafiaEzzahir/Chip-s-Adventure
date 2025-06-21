from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp

class Map(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "assets/map1.png"
        self.allow_stretch = True
        
    def update(self, screen):
        self.size = screen.size

class Home(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(on_press=self.pressed)
        self.background_color = (1, 1, 1, 1)
        self.background_normal = "assets/homeicon.png"
        self.background_down = "assets/homeicon.png"
        self.size_hint = (None, None)
        self.size = (dp(50), dp(50))

        self.homescreen = False

    def pressed(self, instance):
        self.homescreen = True

    def default(self):
        self.homescreen = False

    def update(self, screen):
        self.pos = (dp(5), screen.height-self.height-dp(5))

class MapScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "map"
        self.current = "map"
        with self.canvas:
            Color(1, 1, 1)
            self.background = Rectangle(size=(self.width,self.height))

        self.img = Map()
        self.homebutton = Home()
        self.screenitems = [self.img, self.homebutton]
        for item in self.screenitems:
            self.add_widget(item)

    def update(self):
        self.current = "map"
        self.background.size = (self.width, self.height)
        for item in self.screenitems:
            item.update(self)
        self.checkmap()
        
    def checkmap(self):
        if self.homebutton.homescreen:
            self.current = "level"
            self.homebutton.default()

    def is_changed(self):
        return self.current