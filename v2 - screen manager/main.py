from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class CutsceneScreen(Screen):
    pass

class Version2App(App):
    def build(self):
        return Builder.load_file("version2.kv")

Version2App().run()