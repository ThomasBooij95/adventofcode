from import_text_file import import_text_file
import re


def parse_intervals(input: str):
    parsed_intervals = []
    for item in input.splitlines():
        numbers = re.findall('\d+', item)  # type: ignore
        numbers = [int(x) for x in numbers]
        cur_interval = [range(numbers[0], numbers[1]+1),
                        range(numbers[2], numbers[3]+1)]
        # print(cur_interval)
        parsed_intervals.append(cur_interval)
    return parsed_intervals


def get_number_of_fully_contains(input: 'list'):
    total_containing = 0
    for item in input:
        set1 = set(item[0])
        set2 = set(item[1])
        intersection = list(set1 & set2)
        if intersection == list(set1) or intersection == list(set2):
            total_containing += 1
    return total_containing


def get_number_of_overlapping(input: 'list'):
    total_overlapping = 0
    for item in input:
        set1 = set(item[0])
        set2 = set(item[1])
        intersection = list(set1 & set2)
        if intersection:
            total_overlapping += 1
    return total_overlapping


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    parsed_intervals = parse_intervals(input)
    print('part 1: ', get_number_of_fully_contains(
        parsed_intervals))
    print('part 2: ', get_number_of_overlapping(
        parsed_intervals))
