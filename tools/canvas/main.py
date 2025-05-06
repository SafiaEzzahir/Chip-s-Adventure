from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.app import App

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        size = dp(100)
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass 
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="a")
        b2 = Button(text="b")
        b3 = Button(text="c")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            Rectangle(pos=(700, 200), size=(150, 100))

TheLabApp().run()