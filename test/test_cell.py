import unittest

from src.entities.Cell import Cell


class TestCell(unittest.TestCase):
    def test_when_is_alive_method_is_called_with_a_alive_cell_then_return_true(self):
        expected_is_alive_result = True
        cell = Cell(True)

        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)


    def test_when_is_alive_method_is_called_with_a_death_cell_then_return_false(self):
        expected_is_alive_result = False
        cell = Cell(False)

        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)


    def test_when_resurrect_method_is_called_with_a_death_cell_then_the_cell_is_resurrected(self):
        expected_is_alive_result = True
        cell = Cell(False)

        cell.resurrect()
        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)


    def test_when_resurrect_method_is_called_with_a_alive_cell_then_the_cell_still_alive(self):
        expected_is_alive_result = True
        cell = Cell(True)

        cell.resurrect()
        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)


    def test_when_kill_method_is_called_with_a_alive_cell_then_the_cell_is_killed(self):
        expected_is_alive_result = False
        cell = Cell(True)

        cell.kill()
        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)


    def test_when_kill_method_is_called_with_a_death_cell_then_the_cell_still_death(self):
        expected_is_alive_result = False
        cell = Cell(False)

        cell.kill()
        is_alive = cell.is_alive()

        self.assertEqual(expected_is_alive_result, is_alive)

if __name__ == '__main__':
    unittest.main()
