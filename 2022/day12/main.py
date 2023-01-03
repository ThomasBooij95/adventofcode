from import_text_file import import_text_file
import numpy as np
import logging


def parse_to_grid(input: str):
    grid = []
    for item in input.splitlines():
        grid.append(list(item))
    return np.array(grid, dtype=str)


DIRECTIONS = {
    'up': [-1, 0],
    'right': [0, 1],
    'down': [1, 0],
    'left': [0, -1]
}

# Implement Depth First Search.


def traverse_part_1(grid):
    cur_index_row, cur_index_col = get_starting_index(grid)
    visited = np.array([[False]*len(grid[0])
                       for _ in range(len(grid))], dtype=bool)

    queue = [(cur_index_row, cur_index_col)]
    steps = np.array([[0]*len(grid[0])
                      for _ in range(len(grid))], dtype=int)

    while (len(queue) > 0):
        cur_index_row, cur_index_col = queue.pop(0)
        cur_steps = steps[cur_index_row, cur_index_col]
        if visited[cur_index_row, cur_index_col]:
            continue
        visited[cur_index_row, cur_index_col] = True

        neighbours = get_neighbours_part_1(
            grid, cur_index_row, cur_index_col)
        for row, col in neighbours:
            if visited[row, col] == False:
                queue.append((row, col))
                steps[row, col] = cur_steps+1
    end_row, end_col = get_ending_index(grid)
    return steps[end_row, end_col]


def traverse_part_2(grid):
    cur_index_row, cur_index_col = get_ending_index(grid)
    visited = np.array([[False]*len(grid[0])
                       for _ in range(len(grid))], dtype=bool)

    queue = [(cur_index_row, cur_index_col)]
    steps = np.array([[0]*len(grid[0])
                      for _ in range(len(grid))], dtype=int)

    while (len(queue) > 0):
        cur_index_row, cur_index_col = queue.pop(0)
        cur_steps = steps[cur_index_row, cur_index_col]
        # If we reach the letter 'a' for the first time, we found the shortest path.
        if get_value_of_index(grid, cur_index_row, cur_index_col) == 1:
            return cur_steps

        if visited[cur_index_row, cur_index_col]:
            continue
        visited[cur_index_row, cur_index_col] = True

        neighbours = get_neighbours_part_2(
            grid, cur_index_row, cur_index_col)
        for row, col in neighbours:
            if visited[row, col] == False:
                queue.append((row, col))
                steps[row, col] = cur_steps+1
    end_row, end_col = get_ending_index(grid)


def get_neighbours_part_1(grid, cur_index_row, cur_index_col):
    cur_height = get_value_of_index(grid, cur_index_row, cur_index_col)
    neighbors = []
    width_grid = len(grid[0])
    heigth_grid = len(grid)
    for _, dir in DIRECTIONS.items():
        checking_index = sum_lists([cur_index_row, cur_index_col], dir)
        if checking_index[0] < 0 or checking_index[0] >= heigth_grid or checking_index[1] < 0 or checking_index[1] >= width_grid:
            logging.debug('Out of Bounds!')
            continue
        cur_neighbour_height = get_value_of_index(
            grid, checking_index[0], checking_index[1])
        logging.debug(cur_neighbour_height)
        if cur_neighbour_height <= cur_height+1:
            neighbors.append(tuple(checking_index))
    return neighbors


def get_neighbours_part_2(grid, cur_index_row, cur_index_col):
    cur_height = get_value_of_index(grid, cur_index_row, cur_index_col)
    neighbors = []
    width_grid = len(grid[0])
    heigth_grid = len(grid)
    for _, dir in DIRECTIONS.items():
        checking_index = sum_lists([cur_index_row, cur_index_col], dir)
        if checking_index[0] < 0 or checking_index[0] >= heigth_grid or checking_index[1] < 0 or checking_index[1] >= width_grid:
            logging.debug('Out of Bounds!')
            continue
        cur_neighbour_height = get_value_of_index(
            grid, checking_index[0], checking_index[1])
        logging.debug(cur_neighbour_height)
        if cur_neighbour_height >= cur_height-1:
            neighbors.append(tuple(checking_index))
    return neighbors


def get_value_of_index(grid, cur_index_row, cur_index_col):
    return to_value(grid[cur_index_row, cur_index_col])


def sum_lists(cur_index, dir):
    return [sum(x) for x in zip(cur_index, dir)]


def to_value(input):
    if input == 'S':
        return 1
    if input == 'E':
        return 26
    return ord(input)-96


def get_starting_index(grid):
    start_index = list(list(zip(*np.where(grid == "S")))[0])
    return start_index[0], start_index[1]


def get_ending_index(grid):
    end_index = list(list(zip(*np.where(grid == "E")))[0])
    return end_index[0], end_index[1]


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    parsed_input = import_text_file(isDemoSet=False)
    grid = parse_to_grid(parsed_input)
    answer_part1 = traverse_part_1(grid)
    answer_part2 = traverse_part_2(grid)
    print('Answer to part 1 is:', answer_part1)
    print('Answer to part 2 is:', answer_part2)
