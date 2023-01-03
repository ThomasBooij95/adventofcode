import logging
from import_text_file import import_text_file
import numpy as np


def process_input(input: str):
    commands = []
    for item in input.splitlines():
        foo = item.split(sep=' -> ')
        res = []
        for item in foo:
            tmp = item.split(sep=',')
            res.append([int(tmp[0]), int(tmp[1])])
        commands.append(res)
    return commands


def get_bounds_from_commands(commands):
    cur_min_x = 5000
    cur_max_x = -1
    cur_min_y = 5000
    cur_max_y = -1
    for command in commands:
        for node in command:
            cur_x = node[0]
            cur_y = node[1]
            if cur_x < cur_min_x:
                cur_min_x = cur_x
            if cur_x > cur_max_x:
                cur_max_x = cur_x
            if cur_y < cur_min_y:
                cur_min_y = cur_y
            if cur_y > cur_max_y:
                cur_max_y = cur_y
    return {'min_x': cur_min_x,
            'max_x': cur_max_x,
            'min_y': cur_min_y,
            'max_y': cur_max_y, }


def create_grid_from_commands(commands, flag_print_grid=False):
    bounds = get_bounds_from_commands(commands)

    lowest_index_x = bounds['min_x']  # TODO: get from commands
    highest_index_x = bounds['max_x']  # TODO: get from commands
    lowest_index_y = 0
    highest_index_y = bounds['max_y']  # TODO: get from commands
    sand_x = 500
    sand_y = 0

    grid = [['.']*(highest_index_x - lowest_index_x+1)
            for _ in range(highest_index_y+1)]
    grid = np.array(grid, dtype=str)
    grid[0, sand_x-lowest_index_x] = '+'

    for command in commands:
        for i in range(len(command)-1):
            x1 = command[i][0]-lowest_index_x
            x2 = command[i+1][0]-lowest_index_x
            y1 = command[i][1]
            y2 = command[i+1][1]
            if x1 == x2:
                if y2 < y1:
                    y1, y2 = y2, y1
                for j in range(y1, y2+1):
                    grid[j, x1] = '#'
            if y1 == y2:
                if x2 < x1:
                    x1, x2 = x2, x1
                for j in range(x1, x2+1):
                    grid[y1, j] = '#'

    if flag_print_grid:
        print_grid(grid)
    return grid


def print_grid(grid):
    print('------------------')
    for id, line in enumerate(grid):
        print(''.join(line))


class Sand_unit:
    def __init__(self, x_offset) -> None:
        self.x = 500-x_offset
        self.y = 0

    def move(self, grid):
        try:
            if grid[self.y+1, self.x] == '.':
                self.y += 1
            elif grid[self.y+1, self.x-1] == '.':
                self.y += 1
                self.x -= 1
            elif grid[self.y+1, self.x+1] == '.':
                self.y += 1
                self.x += 1
            else:
                logging.debug('Sand stays where it is')
                grid[self.y, self.x] = 'o'
                return True, grid
            return False, grid
        except:
            logging.debug('Sand unit fell into abyss')
            return 'Abyss', grid


def fill_grid_with_sand(grid, bounds):
    falling = True
    number_of_sand_units = 0
    while True:
        unit = Sand_unit(bounds['min_x'])
        number_of_sand_units += 1
        moved = False
        while not moved:
            moved, grid = unit.move(grid=grid)
            if grid[0, 500-bounds['min_x']] == 'o':
                break
            if moved == 'Abyss':
                print('Stop Program, sand is falling into the abyss')
                break

            if moved:
                moved = False
                # print_grid(grid)
                break

        if moved == 'Abyss':
            number_of_sand_units -= 1
            break
        if grid[0, 500-bounds['min_x']] == 'o':
            # number_of_sand_units -= 1
            break
    return grid, number_of_sand_units


if __name__ == '__main__':
    # Part 1
    input = import_text_file(isDemoSet=False)
    commands = process_input(input)
    grid = create_grid_from_commands(commands, flag_print_grid=False)
    bounds = get_bounds_from_commands(commands)
    grid_with_sand, number_of_sand_units = fill_grid_with_sand(grid, bounds)
    print_grid(grid_with_sand)
    print('Answer to part 1 is:', number_of_sand_units)

    # Part 2
    max_y = bounds['max_y']
    new_input = f'{input}\n330,{max_y+2} -> 666,{max_y+2}'
    new_commands = process_input(new_input)
    grid = create_grid_from_commands(new_commands, flag_print_grid=False)

    bounds = get_bounds_from_commands(new_commands)
    grid_with_sand, number_of_sand_units = fill_grid_with_sand(grid, bounds)
    print_grid(grid_with_sand)  # Warning, Takes a few minutes to compute
    print('Answer to part 1 is:', number_of_sand_units)
