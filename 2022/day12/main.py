from import_text_file import import_text_file
import numpy as np
import logging


def parse_to_grid(input: str):
    grid = []
    for item in input.splitlines():
        print(item)
        grid.append(list(item))
    return np.array(grid, dtype=str)


DIRECTIONS = {
    'up': [-1, 0],
    'right': [0, 1],
    'down': [1, 0],
    'left': [0, -1]
}


def traverse(grid):
    cur_index = get_starting_index(grid)
    cur_height = to_value(grid[cur_index[0], cur_index[1]])
    width_grid = len(grid[0])
    heigth_grid = len(grid)
    last_index = get_starting_index(grid)
    steps = 0
    while (get_value_of_index(grid, cur_index) < 27):
        cur_index, last_index = get_next_index(
            grid, cur_index, width_grid, heigth_grid, last_index)
        steps += 1

    print(get_value_of_index(grid, cur_index))
    print('new node = ', cur_index)
    print('nr of steps = ', steps)
    return steps


def get_next_index(grid, cur_index, width_grid, heigth_grid, last_index):
    cur_height = get_value_of_index(grid, cur_index)
    for _, dir in DIRECTIONS.items():
        checking_index = sum_lists(cur_index, dir)
        if checking_index[0] < 0 or checking_index[0] >= heigth_grid or checking_index[1] < 0 or checking_index[1] >= width_grid:
            logging.debug('Out of Bounds!')
            continue
        if checking_index == last_index:
            logging.debug('Back is not the way!')
            continue
        cur_neighbour_height = get_value_of_index(grid, checking_index)
        logging.debug(cur_neighbour_height)
        if cur_neighbour_height <= cur_height+1:
            last_index = cur_index
            cur_index = checking_index
            break
    return cur_index, last_index


def get_value_of_index(grid, checking_index):
    return to_value(grid[checking_index[0], checking_index[1]])


def sum_lists(cur_index, dir):
    return [sum(x) for x in zip(cur_index, dir)]


def to_value(input):
    if input == 'S':
        return 0
    if input == 'E':
        return 27
    return ord(input)-96


def get_starting_index(grid) -> 'list[int]':
    start_index = list(list(zip(*np.where(grid == "S")))[0])
    return start_index


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    parsed_input = import_text_file(isDemoSet=False)
    grid = parse_to_grid(parsed_input)
    print(grid)
    answer_part1 = traverse(grid)
    print('Answer to part 1 is:', answer_part1)
    # print('Answer to part 2 is:')
