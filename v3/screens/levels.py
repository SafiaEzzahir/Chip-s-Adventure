from kivy.metrics import dp

class LevelManager():
    def __init__(self, levelnum):
        levels = [self.level1, self.level2, self.level3]
        levels[levelnum-1]()

    def level1(self):
        self.phoneboxes = []
        self.chars = {}
        self.allowed_signals = {"corn": 5, "footprints": 1}
        self.backgroundcol = "135879"

    def level2(self):
        self.phoneboxes = []
        self.chars = {}
        self.allowed_signals = {"corn": 2, "footprints": 1}
        self.backgroundcol = "F4F678"

    def level3(self):
        pass