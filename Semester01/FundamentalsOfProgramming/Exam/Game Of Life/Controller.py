class GameOfLifeController:
    def __init__(self, grid):
        self.grid = grid

    def place_pattern(self, pattern, position):
        x, y = map(int, position.split(','))
        self.grid.add_pattern(pattern, x, y)

    def advance_generations(self, n=1):
        for _ in range(n):
            self.grid.tick()