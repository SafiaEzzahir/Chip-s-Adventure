from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    count = 0
    canCount = BooleanProperty(False)
    #slider_value_txt = StringProperty("50")
    text_input_str = StringProperty("foo")

    def on_button_click(self):
        if self.canCount:
            self.count += 1
            self.my_text = "clicked " + str(self.count) + " times"

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.canCount = False
        else:
            widget.text = "ON"
            self.canCount = True
    
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
    
    #def on_slider_value(self, widget):
    #    pass
        #self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

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

TheLabApp().run()