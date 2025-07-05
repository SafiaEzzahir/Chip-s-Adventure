class Timer():
    def __init__(self, interval):
        self.value = 0
        self.interval = interval
    
    def update(self):
        if self.value < self.interval:
            self.value += 1
        else: self.value = 0

    def check(self):
        if self.value == self.interval:
            return True

class Mood():
    def __init__(self, difficulty):
        self.value = 0
        self.feeling = "neutral"
        self.difficulty = difficulty
        self.specific_init()

    def specific_init(self):
        pass

    def set_val(self, val):
        self.value = val

    def change_val(self, val):
        self.value += val
    
    def update(self):
        if self.value > 5 + self.difficulty*2:
            self.feeling = "very good"
        elif self.value > self.difficulty:
            self.feeling = "good"
        elif self.value == self.difficulty:
            self.feeling = "neutral"
        elif self.value < self.difficulty:
            self.feeling = "bad"
        if self.value <= -5 - self.difficulty*2:
            self.feeling = "very bad"

    def update_and_print(self):
        self.update()
        if self.timer.check():
            print(f"your score is {self.value} and chip is {self.feeling} {self.name}")

    def reset(self):
        self.value = 0
        self.feeling = "neutral"
        self.specific_init()

class Hunger(Mood):
    def specific_init(self):
        self.name = "hunger"
        self.timer = Timer(160)

    def event_reaction(self, event):
        if event == "time":
            self.timer.update()
            if self.timer.check():
                self.change_val(-1)
        elif event == "corn":
            self.change_val(1)

        self.update_and_print()

class Confusion(Mood):
    def specific_init(self):
        self.name = "confusion"
        self.timer = Timer(250)
        self.speed_timer = Timer(100)
        self.speed = 0

    def event_reaction(self, event):
        if event == "time":
            self.timer.update()
            self.speed_timer.update()
            if self.timer.check():
                self.change_val(-1)
        elif event == "corn":
            self.change_val(1)
        elif event == "no signal":
            if self.timer.check():
                self.change_val(-3)

        self.update_and_print()

    def change_speed(self, val):
        if self.speed_timer.check():
            self.speed += val
            print(self.speed)

class Happiness(Mood):
    def __init__(self):
        pass

    def event_reaction(self, event):
        pass

    def update(self):
        pass

class Fear(Mood):
    def __init__(self):
        pass

    def event_reaction(self, event):
        pass

    def update(self):
        pass

class Freedom(Mood):
    def __init__(self):
        pass

    def event_reaction(self, event):
        pass

    def update(self):
        pass