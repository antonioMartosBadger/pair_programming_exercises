import unittest

from src.entities.Cell import Cell
from src.entities.Mask import Mask


class TestMask(unittest.TestCase):
    def test_when_rule_1_is_called_and_there_is_a_cell_alive_with_less_than_2_neighbours_alive_then_is_killed(self):
        neighbourhood = [[Cell(True), Cell(False), Cell(False)],
                         [Cell(False), Cell(True), Cell(False)],
                         [Cell(False), Cell(False), Cell(False)]]
        expected_result = False
        ALIVE_CELLS_COUNT = 1

        mask = Mask(neighbourhood)
        mask.apply_rule_one(ALIVE_CELLS_COUNT)
        is_alive = mask.center_cell_is_alive()

        self.assertEqual(expected_result, is_alive)

    def test_when_rule_2_is_called_and_there_is_a_cell_alive_with_2_neighbours_alive_then_still_alive(self):
        neighbourhood = [[Cell(True), Cell(True), Cell(False)],
                         [Cell(False), Cell(True), Cell(False)],
                         [Cell(False), Cell(False), Cell(False)]]
        expected_result = True
        ALIVE_CELLS_COUNT = 2

        mask = Mask(neighbourhood)
        mask.apply_rule_two(ALIVE_CELLS_COUNT)
        is_alive = mask.center_cell_is_alive()

        self.assertEqual(expected_result, is_alive)

    def test_when_rule_2_is_called_and_there_is_a_cell_alive_with_3_neighbours_alive_then_still_alive(self):
        neighbourhood = [[Cell(True), Cell(True), Cell(True)],
                         [Cell(False), Cell(True), Cell(False)],
                         [Cell(False), Cell(False), Cell(False)]]
        expected_result = True
        ALIVE_CELLS_COUNT = 3

        mask = Mask(neighbourhood)
        mask.apply_rule_two(ALIVE_CELLS_COUNT)
        is_alive = mask.center_cell_is_alive()

        self.assertEqual(expected_result, is_alive)

    def test_when_rule_3_is_called_and_there_is_a_cell_alive_with_more_than_3_neighbours_alive_then_the_cell_died(self):
        neighbourhood = [[Cell(True), Cell(True), Cell(True)],
                         [Cell(True), Cell(True), Cell(False)],
                         [Cell(False), Cell(False), Cell(False)]]
        expected_result = True
        ALIVE_CELLS_COUNT = 4
        
        mask = Mask(neighbourhood)
        mask.apply_rule_three(ALIVE_CELLS_COUNT)
        is_alive = mask.center_cell_is_alive()

        self.assertEqual(expected_result, is_alive)



# R1: Celula viva con menos de 2, muere
# R2: Viva con 2 o 3 viva, sigue viva
# R3: Celula viva con mas de 3, muere
# R4: Celula muerta con exactamente 3 vivas, renace


if __name__ == '__main__':
    unittest.main()
