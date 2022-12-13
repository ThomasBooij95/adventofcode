from import_text_file import import_text_file


def calculate_score_pt2(input: str):
    vert = 0
    horz = 0
    aim = 0
    for item in input.splitlines():
        amount = int(item.split(' ')[1])
        if item[0] == 'f':
            horz += amount
            vert += amount*aim
        elif item[0] == 'd':
            aim += amount
        elif item[0] == 'u':
            aim -= amount
        else:
            raise RuntimeError('unknown command')

    return vert*horz


def calculate_score_pt1(input: str):
    vert = 0
    horz = 0
    aim = 0
    for item in input.splitlines():
        amount = int(item.split(' ')[1])
        if item[0] == 'f':
            horz += amount
        elif item[0] == 'd':
            vert += amount
        elif item[0] == 'u':
            vert -= amount
        else:
            raise RuntimeError('unknown command')

    return vert*horz


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    print('Answer to part 1: ', calculate_score_pt1(input))
    print('Answer to part 2: ', calculate_score_pt2(input))
