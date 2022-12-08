from import_text_file import import_text_file
# import array as ar
import numpy as np
from collections import defaultdict


def parse_grid_from(input: str):
    def _str_to_list_of_int(row):
        rv = []
        for char in row:
            rv.append(int(char))
        return rv

    row_index = 0
    grid = []
    for row in input.splitlines():
        row_int_list = _str_to_list_of_int(row)
        grid.insert(row_index, row_int_list)
        row_index += 1

    return np.array(grid, np.int32)


def calculate_visibility_bool_grid_from(grid):
    # initialize grid to all zeros(everything is invisible)
    vis_grid = np.zeros((len(grid), len(grid[0])))
    width = vis_grid.shape[0]
    length = vis_grid.shape[1]

    # 4 loops: from left, from top, from right, from bottom(maybe only 2 loops needed)
    # Loop horizontally
    loopconditions = \
        [[range(0, length), range(0, width)],  # loop from left
         [range(0, length), range(width-1, -1, -1)],  # loop from right
         ]
    for range_condition in loopconditions:
        for i in range_condition[0]:
            cur_max = -1
            for j in range_condition[1]:
                if grid[i, j] > cur_max:
                    cur_max = grid[i, j]
                    vis_grid[i, j] = 1

    # Loop from top to bottom
    loopconditions = \
        [[range(0, width), range(0, length)],  # top to bottom
         [range(0, width), range(length-1, -1, -1)],  # bottom to top
         ]
    for range_condition in loopconditions:
        for j in range_condition[0]:
            cur_max = -1
            for i in range_condition[1]:
                if grid[i, j] > cur_max:
                    cur_max = grid[i, j]
                    vis_grid[i, j] = 1
    return vis_grid


def calculate_scenic_score_grid_from(grid):
    def calculate_scenic_score_right(grid, i, j):
        # print('calculating score')
        width = grid.shape[0]
        length = grid.shape[1]
        reference_height = grid[i, j]
        scenic_score = defaultdict(int)
        for cursor in range(j+1, width):
            cur_treeheight = grid[i, cursor]
            scenic_score['right'] += 1
            if cur_treeheight >= reference_height:
                break
        return scenic_score['right']

    def calculate_scenic_score_down(grid, i, j):
        width = grid.shape[0]
        length = grid.shape[1]
        reference_height = grid[i, j]
        scenic_score = 0
        for cursor in range(i+1, length):
            cur_treeheight = grid[cursor, j]
            scenic_score += 1
            if cur_treeheight >= reference_height:
                break
        return scenic_score

    def calculate_scenic_score_left(grid, i, j):
        width = grid.shape[0]
        length = grid.shape[1]
        reference_height = grid[i, j]
        scenic_score = 0
        for cursor in range(j-1, -1, -1):
            cur_treeheight = grid[i, cursor]
            scenic_score += 1
            if cur_treeheight >= reference_height:
                break
        return scenic_score

    def calculate_scenic_score_top(grid, i, j):
        width = grid.shape[0]
        length = grid.shape[1]
        reference_height = grid[i, j]
        scenic_score = 0
        for cursor in range(i-1, -1, -1):
            cur_treeheight = grid[cursor, j]
            scenic_score += 1
            if cur_treeheight >= reference_height:
                break
        return scenic_score

    # initialize grid to all zeros(everything is invisible)
    score_grid = np.zeros((len(grid), len(grid[0])))
    width = score_grid.shape[0]
    length = score_grid.shape[1]
    for i in range(0, length):
        for j in range(0, width):
            score = calculate_scenic_score_right(grid, i, j)
            score *= calculate_scenic_score_down(grid, i, j)
            score *= calculate_scenic_score_left(grid, i, j)
            score *= calculate_scenic_score_top(grid, i, j)
            score_grid[i, j] = score
    return score_grid


if __name__ == '__main__':
    txt = import_text_file(isDemoSet=False)
    grid = parse_grid_from(txt)
    vis_grid = calculate_visibility_bool_grid_from(grid)
    print('Answer to part 1: ', round(sum(sum(vis_grid))))  # type: ignore

    score_grid = calculate_scenic_score_grid_from(grid)
    print('Answer to part 2: ', round(score_grid.max()))
