from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.properties import Clock

class Screener(ScreenManager):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()
        from screens.menu import MenuScreen
        from screens.level import LevelScreen
        from screens.cutscenes import CutsceneScreen
        from gamemanager import GameManager
        self.gamemanager = GameManager()
        self.menu = MenuScreen()
        self.level = LevelScreen()
        self.cutscene = CutsceneScreen()
        self.add_widget(self.menu)
        self.add_widget(self.level)
        self.add_widget(self.cutscene)
        self.current = "menu"
        Clock.schedule_interval(self.update, 1.0/50.0)

    def update(self, dt):
        change = self.current_screen.is_changed()
        newcurrent = change
        if newcurrent != self.current:
            self.canvas.clear()
            self.current = newcurrent
        self.current_screen.update()

class Version3App(App):
    def build(self):
        return Builder.load_file("version3.kv")
    
if __name__ == '__main__':
    Version3App().run()