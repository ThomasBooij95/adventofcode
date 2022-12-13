from import_text_file import import_text_file


def calculate_num_of_increases(input: str) -> int:
    prev_val = 0
    first = True
    num_of_increase = 0
    for cur_val in input.splitlines():
        if first:
            prev_val = int(cur_val)
            first = False
            continue
        if int(cur_val) > int(prev_val):
            num_of_increase += 1

        prev_val = cur_val
    return num_of_increase


def make_windows_from(txt: str) -> 'list[int]':
    array = [int(x) for x in txt.splitlines()]
    sliding_windows = []
    for i in range(len(array)-2):
        sliding_windows.append(sum(array[i:i+3]))
    return sliding_windows


if __name__ == '__main__':
    txt = import_text_file(isDemoSet=False)
    windows = make_windows_from(txt)
    # convert back to string to use first func
    str_list = '\n'.join([str(x) for x in windows])
    ans_part1 = calculate_num_of_increases(txt)
    ans_part2 = calculate_num_of_increases(str_list)
    print('Answer to part 1: ', ans_part1)
    print('Answer to part 2: ', ans_part2)
