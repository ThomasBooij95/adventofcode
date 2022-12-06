from import_text_file import import_text_file
import string


def get_duplicates_in_halves(input: str):
    duplicates = []
    for item in input.splitlines():
        half_num_of_items = int(len(item)/2)
        firsthalf = item[0:half_num_of_items]
        secondhalf = item[half_num_of_items:]
        result = ''
        for item_first in firsthalf:
            if item_first in secondhalf:
                result = item_first
                break
        duplicates.append(result)
    return duplicates


def get_total_priority_score(duplicates: 'list[str]'):
    total_priority = 0
    for item in duplicates:
        cur_priority = calculate_priority(item)
        total_priority += cur_priority
    return total_priority


def calculate_priority(item):
    cur_priority = 0
    if item.isupper():
        cur_priority += 26
    lowercaseitem = item.lower()
    index = string.ascii_lowercase.index(lowercaseitem)+1
    cur_priority += index
    return cur_priority


def get_badges(input: str):
    badges = []
    gnomes = input.splitlines()
    num_of_gnomes = len(gnomes)
    for i in range(int(num_of_gnomes/3)):
        current_index = i*3
        cur_gnome = gnomes[current_index]
        for char in cur_gnome:
            if char in gnomes[current_index+1] and char in gnomes[current_index+2]:
                badges.append(char)
                break

    return badges


if __name__ == '__main__':
    print('')
    input = import_text_file(isDemoSet=False)

    print('part 1: ', get_total_priority_score(
        get_duplicates_in_halves(input)))
    print('part 2: ', get_total_priority_score(get_badges(input)))
