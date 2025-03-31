"""
Resources:
    https://natureofcode.com/cellular-automata/#the-game-of-life
"""
import os
import time
from copy import deepcopy
from random import randint
from itertools import count


class GameOfLife:

    def print(self, grid, update_freq=0.75):
        for i in count():
            os.system('clear')
            print(f'Gen{i}')
            print(self._get_grid_as_str_to_display(grid))
            grid = self._get_next_generation_grid(grid)
            time.sleep(update_freq)

    def _get_next_generation_grid(self, grid):
        new_grid = deepcopy(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                new_grid[x][y] = self._check_alive(grid, x, y)
        return new_grid

    def _get_grid_as_str_to_display(self, grid):
        return '\n'.join(
            ''.join('a' if cell else '_' for cell in row)
            for row in grid
        )

    def _check_alive(self, grid, x, y):
        current = grid[x][y]
        alive_neighbours = sum((
            self._get_cell_or_zero(grid, x-1, y-1), self._get_cell_or_zero(grid, x-1, y), self._get_cell_or_zero(grid, x-1, y+1),
            self._get_cell_or_zero(grid, x, y-1), self._get_cell_or_zero(grid, x, y+1),
            self._get_cell_or_zero(grid, x+1, y-1), self._get_cell_or_zero(grid, x+1, y), self._get_cell_or_zero(grid, x+1, y+1),
        ))

        if current and (alive_neighbours >= 4 or alive_neighbours <= 1):
            return False

        if not current and alive_neighbours == 3:
            return True

        return current

    def _get_cell_or_zero(self, grid, x, y):
        if x < 0 or x >= len(grid):
            return 0
        if y < 0 or y >= len(grid[0]):
            return 0
        return grid[x][y]

if __name__ == '__main__':
    # blinker (goes back and forth between two states)
    # GameOfLife().print([
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    # ])

    initial_board = [
        [randint(0, 1) for _ in range(30)]
        for _ in range(30)
    ]
    GameOfLife().print(initial_board, update_freq=0.1)
