import unittest
from Repository import GameOfLifeGrid

class TestGameOfLifeTick(unittest.TestCase):

    def test_under_population(self):
        grid = GameOfLifeGrid()
        grid.add_pattern('blinker', 3, 3)  #Assuming 'blinker' places 3 vertical live cells
        grid.tick()
        self.assertEqual(grid.grid[3][3], ' ')
        self.assertEqual(grid.grid[4][3], ' ')
        self.assertEqual(grid.grid[5][3], ' ')

    def test_stability(self):
        grid = GameOfLifeGrid()
        grid.add_pattern('block', 3, 3)  #Assuming 'block' places a 2x2 square of live cells
        before_tick = [row[:] for row in grid.grid]  # Deep copy of grid before tick
        grid.tick()
        after_tick = grid.grid
        self.assertEqual(before_tick, after_tick)

    def test_over_population(self):
        grid = GameOfLifeGrid()
        #Manually create an overpopulated situation
        grid.add_pattern('block', 2, 2)
        grid.add_pattern('blinker', 3, 2)  #Add extra neighbors to create overpopulation
        grid.tick()
        self.assertEqual(grid.grid[3][3], ' ')

    def test_reproduction(self):
        grid = GameOfLifeGrid()
        #Manually create a reproduction situation
        grid.grid[2][3] = 'X'
        grid.grid[3][2] = 'X'
        grid.grid[3][4] = 'X'
        grid.tick()
        self.assertEqual(grid.grid[3][3], 'X')


