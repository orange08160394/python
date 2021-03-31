class Geometic():
    def __init__(self):
        self.color=""
        self.shape=""
    def getcolor(self):
        if self.shape=="circle":
            self.color="Green"
        if self.shape=="Square":
            self.color="Red"
        return self.color