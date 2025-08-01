from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.properties import Clock

class Screener(ScreenManager):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()
        self.new_data = {}
        from screens.menu import MenuScreen
        from screens.level import LevelScreen
        from screens.cutscenes import CutsceneScreen
        from screens.settings import SettingsScreen
        from screens.win import WinScreen
        from screens.lose import LoseScreen
        from screens.map import MapScreen
        self.menu = MenuScreen()
        self.level = LevelScreen()
        self.cutscene = CutsceneScreen()
        self.settings = SettingsScreen()
        self.win = WinScreen()
        self.lose = LoseScreen()
        self.map = MapScreen()
        self.add_widget(self.menu)
        self.add_widget(self.level)
        self.add_widget(self.cutscene)
        self.add_widget(self.settings)
        self.add_widget(self.win)
        self.add_widget(self.lose)
        self.add_widget(self.map)
        self.current = "menu"
        Clock.schedule_interval(self.update, 1.0/20.0)

    def update(self, dt):
        change = self.current_screen.is_changed()
        newcurrent = change
        if newcurrent != self.current:
            self.old_data = self.new_data
            self.new_data = self.current_screen.update()
            self.canvas.clear()
            self.current = newcurrent
            self.current_screen.change = self.current_screen.name
        else:
            self.current_screen.update()

class Version3App(App):
    def build(self):
        return Builder.load_file("version3.kv")
    
if __name__ == '__main__':
    Version3App().run()