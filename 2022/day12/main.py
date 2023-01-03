from import_text_file import import_text_file
import numpy as np


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
    print(cur_height)
    # print(DIRECTIONS)
    for _, dir in DIRECTIONS.items():
        checking_index = sum_lists(cur_index, dir)
        if checking_index[0] < 0 or checking_index[0] > heigth_grid or checking_index[1] < 0 or checking_index[1] > width_grid:
            print('Out of Bounds!')
            continue

        print(checking_index)


def sum_lists(cur_index, dir):
    return [sum(x) for x in zip(cur_index, dir)]
    # print(grid[start_index[0], start_index[1]])
    # print(to_value(grid[0, 0]))


def to_value(input):
    if input == 'S':
        return 0
    if input == 'E':
        return 27
    return ord(input)-96


def get_starting_index(grid) -> list[int]:
    start_index = list(list(zip(*np.where(grid == "S")))[0])
    return start_index


if __name__ == '__main__':
    parsed_input = import_text_file(isDemoSet=True)
    grid = parse_to_grid(parsed_input)
    print(grid)
    traverse(grid)
