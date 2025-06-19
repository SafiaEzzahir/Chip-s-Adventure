from kivy.uix.screenmanager import Screen

class MapScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "map"
        self.current = "map"

    def update(self):
        pass

    def is_changed(self):
        return self.current