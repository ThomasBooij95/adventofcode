from import_text_file import import_text_file


class Node:
    x = 0
    y = 0
    history = []
    label = str

    def __init__(self, label) -> None:
        self.label = label

    def move(self, dir: 'list'):
        self.x += dir[0]
        self.y += dir[1]

    def storestate(self):
        self.history.append([self.x, self.y])

    def __repr__(self) -> str:
        return f'Node {self.label} at x:{self.x}, y:{self.y}'


def to_direction(item: str):
    parsed_input = item.split(' ')
    amount = int(parsed_input[1])
    dict_dir = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }
    try:
        direction = dict_dir[parsed_input[0]]
    except:
        raise KeyError(
            f'Key "{parsed_input[0]}" not found in dict. Must be one of {list(dict_dir.keys())}')
    return direction, amount


def generate_tail_move(head_x: int, head_y: int, tail_x: int, tail_y: int, direction: 'list[int]') -> 'list[int]':
    # if overlapping, don't move the tail
    if abs(head_x - tail_x) < 2 and abs(head_y - tail_y) < 2:
        return [0, 0]

    # if moving down, or up, tail moves in same direction
    elif (head_y == tail_y and abs(head_x - tail_x) > 1):
        if head_x - tail_x < 0:
            return [-1, 0]
        else:
            return [1, 0]

    # if moving left or right, tail moves in same direction
    elif (head_x == tail_x and abs(head_y - tail_y) > 1):
        if head_y - tail_y < 0:
            return [0, -1]
        else:
            return [0, 1]

    else:  # Move diagonally in the direction of the head.
        dir_x = head_x-tail_x
        dir_y = head_y-tail_y
        return [int(dir_x/abs(dir_x)), int(dir_y/abs(dir_y))]


def calculate_number_of_visited_cells_of_tail(input: str, head: Node, tail: Node) -> int:
    tail.storestate()
    for item in input.splitlines():
        direction, amount = to_direction(item)
        for _ in range(amount):
            head.move(direction)
            tail.move(generate_tail_move(
                head.x, head.y, tail.x, tail.y, direction))
            tail.storestate()
    unique_data = [list(x) for x in set(tuple(x) for x in tail.history)]
    return (len(unique_data))


def calculate_number_of_visited_cells_of_last_tail(input: str, head: Node, tails: 'list[Node]', flag_print_grid=False):
    history_last_tail = []
    history_last_tail.append([tails[-1].x, tails[-1].y])
    for item in input.splitlines():
        head_direction, amount = to_direction(item)

        for _ in range(amount):
            head.move(head_direction)
            for i in range(len(tails)):
                if i == 0:
                    cur_tail_direction = generate_tail_move(
                        head.x, head.y, tails[i].x, tails[i].y, head_direction)
                    tails[i].move(cur_tail_direction)
                else:
                    cur_tail_direction = generate_tail_move(
                        tails[i-1].x, tails[i-1].y, tails[i].x, tails[i].y, cur_tail_direction)  # type: ignore
                    tails[i].move(cur_tail_direction)
            history_last_tail.append([tails[-1].x, tails[-1].y])
        if (flag_print_grid):
            print(item)
            print('')
            print_grid(head, tails)

    unique_data = [list(x) for x in set(tuple(x) for x in history_last_tail)]
    return (len(unique_data))


def print_grid(head, tails):
    all_nodes = []
    all_nodes.append(head)
    for node in tails:
        all_nodes.append(node)
    print_current_grid(all_nodes)


def print_current_grid(nodes: 'list[Node]'):
    import numpy as np
    height_grid = 21
    row_of_dots = ['. ']*26
    grid = []
    for _ in range(height_grid):
        grid.append(row_of_dots)
    grid = np.array(grid, np.string_)
    nodes.reverse()
    for node in nodes:
        index_x, index_y = convert_to_grid_index_large_example(
            node.x, node.y, height_grid)
        grid[index_y, index_x] = node.label+' '  # type: ignore
    for row in grid:
        print(''.join(row.astype(str)))
    print('')
    print('-'*50)
    print('')


def convert_to_grid_index(xx, yy, height_grid):
    yy = height_grid-1-yy
    return xx, yy


def convert_to_grid_index_large_example(xx, yy, height_grid):
    yy += 5
    xx += 11
    yy = height_grid-1-yy
    return xx, yy


if __name__ == '__main__':
    isDemoSet = True
    input = import_text_file(isDemoSet=isDemoSet)
    head = Node('H')
    tail = Node('T')
    print('Answer to part 1 is:',
          calculate_number_of_visited_cells_of_tail(input, head, tail))
    head = Node('H')
    tails = []
    tail_size = 9
    for i in range(tail_size):
        tails.append(Node(str(i+1)))
    print('Answer to part 2 is:',
          calculate_number_of_visited_cells_of_last_tail(input, head, tails, flag_print_grid=isDemoSet))
