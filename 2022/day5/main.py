from import_text_file import import_text_file
import os
import re


def process_input_part_1(input: str):
    stacks = process_stacks_part_1(get_stacks(input), get_instructions(input))
    return get_top_stacks(stacks)


def process_input_part_2(input: str):
    stacks = process_stacks_part_2(get_stacks(input), get_instructions(input))
    return get_top_stacks(stacks)


def get_top_stacks(stacks):
    return ''.join([x.pop() for x in stacks])


def process_stacks_part_1(stacks: 'list[list]', instructions: 'list[dict]'):
    for instruction in instructions:
        index_from_pile = instruction['from_pile'] - 1
        index_to_pile = instruction['to_pile'] - 1
        for _ in range(instruction['amount']):
            crane = stacks[index_from_pile].pop()
            stacks[index_to_pile].append(crane)
    return stacks


def process_stacks_part_2(stacks: 'list[list]', instructions: 'list[dict]'):
    for instruction in instructions:
        index_from_pile = instruction['from_pile'] - 1
        index_to_pile = instruction['to_pile'] - 1
        amount_to_move = instruction['amount']
        crane = []
        for _ in range(instruction['amount']):
            crane.append(stacks[index_from_pile].pop())
        crane = list(reversed(crane))
        stacks[index_to_pile] = stacks[index_to_pile]+crane
    return stacks


def get_instructions(input: str):
    instructions = input.split("\n\n")[1]
    parsed_instructions = []
    for instruction in instructions.splitlines():
        cur_moves = re.findall('\d+', instruction)
        cur_move_dict = {
            'amount': int(cur_moves[0]),
            'from_pile': int(cur_moves[1]),
            'to_pile': int(cur_moves[2])
        }
        parsed_instructions.append(cur_move_dict)
    return parsed_instructions


def get_stacks(input: str):
    num_of_stacks = int((len(input.splitlines()[0])+1)/4)  # number of stacks

    # initialize list of lists stacks
    stacks = [[] for _ in range(num_of_stacks)]
    pattern = re.compile("\d+")  # type: ignore
    for item in input.splitlines():
        if pattern.search(item):  # Break when containers end.
            break
        print(item)
        item_list = list(item)
        cursor = 1
        i = 0
        while (cursor < len(item_list)):
            if item_list[cursor] != ' ':
                stacks[i].append(item_list[cursor])
            i += 1
            cursor += 4
    reversed_stacks = [list(reversed(x)) for x in stacks]
    return reversed_stacks


if __name__ == '__main__':
    os.system('clear')
    text = import_text_file(isDemoSet=False)
    print('part 1 = ', process_input_part_1(text))
    print('part 2 = ', process_input_part_2(text))
