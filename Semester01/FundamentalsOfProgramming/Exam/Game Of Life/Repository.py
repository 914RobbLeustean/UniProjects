class GameOfLifeGrid:
    def __init__(self, size=8, patterns_file='patterns.txt'):
        self.size = size
        self.grid = self.create_empty_grid()
        self.patterns = self.load_patterns(patterns_file)

    def create_empty_grid(self):
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def load_patterns(self, filename):
        patterns = {}
        current_pattern = []
        pattern_name = ""
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    if current_pattern:
                        patterns[pattern_name] = current_pattern
                        current_pattern = []
                    pattern_name = line.strip().split(':')[0]
                elif line.strip():
                    current_pattern.append(list(line.strip()))
                else:
                    if current_pattern:
                        patterns[pattern_name] = current_pattern
                        current_pattern = []
        if current_pattern:  # Add the last pattern if file doesn't end with a blank line
            patterns[pattern_name] = current_pattern
        return patterns

    def add_pattern(self, pattern_name, x, y):
        pattern = self.patterns.get(pattern_name, [])
        # Validate pattern placement
        if not self.is_placement_valid(pattern, x, y):
            print(f"Cannot place {pattern_name} at ({x},{y}). Pattern would be out of bounds or overlap with live cells.")
            return False
        for dx, row in enumerate(pattern):
            for dy, cell in enumerate(row):
                if cell == 'X':
                    self.grid[x + dx][y + dy] = 'X'
        return True

    def is_placement_valid(self, pattern, x, y):
        for dx, row in enumerate(pattern):
            for dy, cell in enumerate(row):
                if cell == 'X':
                    if not (0 <= x + dx < self.size and 0 <= y + dy < self.size):  # Boundary check
                        return False
                    if self.grid[x + dx][y + dy] == 'X':  # Overlap check
                        return False

    def count_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == 'X':
                count += 1
        return count

    def tick(self):
        """
        The tick method in the GameOfLifeGrid class is responsible for advancing the game state by one generation according to the following rules:
        Under-population: A live cell with fewer than two live neighbors dies.
        Stability: A live cell with two or three live neighbors lives on to the next generation.
        Over-population: A live cell with more than three live neighbors dies.
        Reproduction: A dead cell with exactly three live neighbors becomes a live cell.
        A "neighbor" includes the eight cells surrounding a given cell. The tick method applies these rules simultaneously to every cell in the grid, creating the next generation. 
        """
        
        new_grid = self.create_empty_grid()
        for x in range(self.size):
            for y in range(self.size):
                neighbors = self.count_neighbors(x, y)
                if self.grid[x][y] == ' ' and neighbors == 3:
                    new_grid[x][y] = 'X'
                elif self.grid[x][y] == 'X' and neighbors in [2, 3]:
                    new_grid[x][y] = 'X'
        self.grid = new_grid

    def display(self):
        print('_' * (self.size * 2 + 1))  # Top border
        for row in self.grid:
            row_str = '|' + '|'.join(row) + '|'
            print(row_str.replace(' ', ' _').replace('X', ' X'))  # Replace empty cells with visually distinct placeholders
        print('_' * (self.size * 2 + 1))  # Bottom border
