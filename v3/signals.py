from kivy.uix.image import Image
from kivy.metrics import dp

class Corn():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.sizes = dp(40)
        self.type = "corn"
        self.poss = (self.posx-self.sizes/2, self.posy-self.sizes/2)

    def check_pos(self, bppos):
        if self.poss[0]>=bppos[0] and self.poss[1]<=bppos[1]:
            return None
        else:
            return Image(size_hint=(None, None), pos=(self.poss), source="assets/corn.png", size=(self.sizes, self.sizes))

    def update(self, bppos):
        return self.check_pos(bppos)

class Footprint():
    def __init__(self, position):
        self.type = "footprint"
        self.mode = "footdown"
        self.position = position
        self.sizes = (dp(50), dp(50))

    def footdown(self):
        return Image(size_hint=(None, None), size=(self.sizes), source="assets/footprints.png", pos=self.position)

    def shoesdown(self):
        pass

    def trackdown(self):
        pass

    def trackfinished(self):
        pass

    def update(self):
        if self.mode == "footdown":
            return self.footdown()
        elif self.mode == "shoesdown":
            return self.shoesdown()
        elif self.mode == "trackdown":
            return self.trackdown()
        elif self.mode == "trackfinished":
            return self.trackfinished()