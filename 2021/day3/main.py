from import_text_file import import_text_file


def calculate_gamma_and_epsilon_binary_from(input: str):
    bytelen, full_string, bytearray = get_bytearray(input)
    gamma = []
    epsilon = []
    for item in bytearray:
        total = sum(item)
        if total > len(full_string)/bytelen/2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    return gamma, epsilon


def calculate_oxygen_and_co2_binary_from(input: str, gamma: 'list', epsilon: 'list'):
    bytelen, full_string, bytearray = get_bytearray(input)
    cur_item = bytearray[0]
    while len(cur_item) > 1:
        total = sum(cur_item)
        if total >= len(full_string)/bytelen/2:
            new_array_indeces = [i for i in range(
                len(cur_item)) if cur_item[i] == 1]
        else:
            new_array_indeces = [i for i in range(
                len(bytearray)) if bytearray[i] == 1]
        cur_item = cur_item[new_array_indeces]
        # remove numbers that don't have the common bit. look


def get_bytearray(input):
    bytelen = len(input.splitlines()[0])
    full_string = input.replace('\n', '')
    bytearray = []
    for i in range(bytelen):
        bytearray.append([])
        for j in range(i, len(full_string), bytelen):
            bytearray[i].append(int(full_string[j]))
    return bytelen, full_string, bytearray


def array_to_decimal(binary_array):
    return int(''.join([str(x) for x in binary_array]), 2)


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    gamma, epsilon = calculate_gamma_and_epsilon_binary_from(input)
    oxygen, co2 = calculate_oxygen_and_co2_binary_from(input, gamma, epsilon)
    gamma_score = array_to_decimal(gamma)
    epsilon_score = array_to_decimal(epsilon)
    print('Answer to part 1: ', gamma_score*epsilon_score)
    # print('Answer to part 2: ', ans_part2)
