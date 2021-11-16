
class Cell:

    def __init__(self, alive):
        self.alive = alive

    def is_alive(self):
        return self.alive

    def resurrect(self):
        self.alive = True

    def kill(self):
        self.alive = False

