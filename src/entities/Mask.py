
class Mask():

    def __init__(self, neighbourhood):
        self.neighbourhood = neighbourhood
        self.center_cell = neighbourhood[1][1]
        
    def center_cell_is_alive(self):
        return self.center_cell.is_alive()

    # R1: Celula viva con menos de 2, muere
    def apply_rule_one(self, alive_count):
        if self.center_cell_is_alive() and alive_count < 2:
            self.center_cell.kill()

    # R2: Viva con 2 o 3 viva, sigue viva
    def apply_rule_two(self, alive_count):
        if self.center_cell_is_alive() and (alive_count == 2 or alive_count == 3):
            pass
