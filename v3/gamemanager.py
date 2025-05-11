class GameManager():
    def __init__(self):
        self.count = 0

    def updategm(self):
        if self.count >= 200:
            return "level"
        else:
            print(self.count)
            self.count +=1
            return "menu"