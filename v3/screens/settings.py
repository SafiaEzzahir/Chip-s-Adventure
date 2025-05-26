from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider

class SettingsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "settings"
        self.change = "settings"

        self.darkestbrown = get_color_from_hex("462521")
        self.mediumbrown = get_color_from_hex("6E514A")
        self.mediumcream = get_color_from_hex("BEA99B")
        self.cream = get_color_from_hex("E6D5C3")

        self.home_button_sizes = (dp(413/8), dp(500/8))
        self.home_button_padding = dp(10)

        with self.canvas:
            Color(*self.mediumbrown)
            self.backround = Rectangle(size=self.size)

        self.volume_slider = Slider(min=0, max=100, value=100, pos=(0, 0), size_hint=(None, None), size=(self.width/3, dp(10)), background_horizontal="assets/brownslider.png", background_width=dp(5), cursor_image="assets/browncursor.png")
        self.add_widget(self.volume_slider)
        self.widgets = [self.volume_slider]

        self.labels = [self.init_label("volume", (0,0), self.mediumcream), self.init_label("darkmode", (0,0), self.mediumcream), self.init_label("life", (0,0), self.mediumcream)]

        self.labels_height = 0
        for l in self.labels:
            self.labels_height += l.size[1]

        self.title = self.init_label("Settings", (0, 0), self.cream)
        
        self.init_home()

    def init_home(self):
        self.sparkle = SoundLoader.load("v3/assets/sparkle.wav")
        self.chirp = SoundLoader.load("v3/assets/chipchirp.wav")
        self.home_button = Button(background_normal="v3/assets/homeicon.png", 
                                  background_down="v3/assets/homeicondown.png", 
                                  size_hint=(None, None), 
                                  size=self.home_button_sizes, 
                                  pos=(self.home_button_padding, self.height-self.home_button_sizes[1]-self.home_button_padding), 
                                  on_press=self.onhome
                                  )
        self.add_widget(self.home_button)

    def update_label_pos(self, label, num):
        interval = (self.title.pos[1]-self.labels_height)/len(self.labels)
        y = self.title.pos[1]-interval*num
        x = self.width/6-label.size[0]/2
        label.pos = (x, y)

    def update_widget_pos(self, widget, num):
        y = self.labels[num].pos[1]+widget.size[1]
        x = self.width/6*3-widget.size[0]/2
        widget.width = self.width/3
        widget.pos = (x, y)
        
    def init_label(self, text, pos, col):
        label = Label(text=text, pos=pos, color=col, font_size=dp(30), font_name="v3/assets/fontly.ttf", size_hint=(None, None), size=(dp(200), dp(40)))
        self.add_widget(label)
        return label

    def update(self):
        self.backround.size = self.size
        self.home_button.pos = (self.home_button_padding, self.height-self.home_button_sizes[1]-self.home_button_padding)

        for labelnum in range(len(self.labels)):
            label = self.labels[labelnum]
            self.update_label_pos(label, labelnum+1)

        for widgetnum in range(len(self.widgets)):
            widget = self.widgets[widgetnum]
            self.update_widget_pos(widget, widgetnum)

        self.title.center_x = self.center_x
        self.title.center_y = self.height - dp(50)

    def onhome(self, instance):
        self.sparkle.play()
        self.chirp.play()
        self.change = "menu"

    def is_changed(self):
        return self.change