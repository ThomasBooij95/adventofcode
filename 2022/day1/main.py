from typing import List
from import_text_file import import_text_file


def calculate_list_of_sums(input: str) -> List[int]:
    cur_list = []
    sum_list = []
    for item in input.splitlines():
        if item:
            cur_list.append(int(item))
        else:
            sum_list.append(sum(cur_list))
            cur_list = []
    sum_list.append(sum(cur_list))
    return sum_list


def find_highest_value(list_of_sums):
    list_of_sums.sort(reverse=True)
    return list_of_sums[0]


def find_sum_of_highest_x_values(list_of_sums, x) -> int:
    list_of_sums.sort(reverse=True)
    return sum(list_of_sums[0:x])


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    list_of_sums = calculate_list_of_sums(input)

    print('Answer to part 1: ', find_highest_value(list_of_sums))
    print('Answer to part 2: ', find_sum_of_highest_x_values(list_of_sums, 3))
