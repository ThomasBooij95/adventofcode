from typing import List
from helpers.import_text_file import import_text_file
import os
from pathlib import Path


def import_text_file(cwd) -> str:
    if os.environ['DEMO_SET'] == True:
        file = str(cwd)+'/demo-input.txt'
    else:
        file = str(cwd)+'/test-input.txt'
    p = Path(__file__).with_name(file)
    with p.open('r') as f:
        return f.read()


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


if __name__ == '__main__':
    input = import_text_file(os.getcwd()+'/2022/day1')
    list_of_sums = calculate_list_of_sums(input)
    list_of_sums.sort(reverse=True)
    print('answer to part 1: ', list_of_sums[0])
    print('Answer to part 2: ', sum(list_of_sums[0:3]))
