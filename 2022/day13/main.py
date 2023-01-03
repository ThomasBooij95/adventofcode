from import_text_file import import_text_file
import ast
import logging
from copy import deepcopy


def process_input(input: str):
    packets = []
    for item in input.splitlines():
        if (item != ''):
            packets.append(ast.literal_eval(item))
    return packets


def packets_in_right_order(p1, p2):
    if p1 == p2:
        logging.debug('packages are the same')
    logging.debug(f'Packets to compare: p1 = {p1}, p2 = {p2} ')
    for i in range(len(p1)):
        try:
            logging.debug(f'Comparing {p1[i]} and {p2[i]}')
            if type(p1[i]) == int and type(p2[i]) == int:
                logging.debug('both are ints')
                if p1[i] < p2[i]:
                    return True
                elif p1[i] > p2[i]:
                    return False
                else:
                    pass

            elif type(p1[i]) == list and type(p2[i]) == list:
                logging.debug('both are lists')
                if p1[i] == p2[i]:  # If the lists are the same, continue to next element
                    logging.debug(
                        'both lists are the same, continue to next element.')
                    continue
                logging.debug(
                    'call packets_in_right_order() again recursively')
                return packets_in_right_order(p1[i], p2[i])
            else:
                logging.debug(
                    f'Exactly one packet is a list: {p1[i]} and {p2[i]}')
                if p1[i] == p2[i]:  # If the lists are the same, continue to next element
                    logging.debug(
                        'both lists are the same, continue to next element.')
                    continue
                logging.debug(
                    f'call packets_in_right_order() again recursively with {p1[i]} and {p2[i]}')
                if type(p1[i]) != list:
                    return packets_in_right_order([p1[i]], p2[i])
                if type(p2[i]) != list:
                    return packets_in_right_order(p1[i], [p2[i]])
        except:
            logging.debug(
                'p2 has run out of elements, so the packets are out of order')
            return False
    logging.debug('p1 has run out of elements, so the packets in order')
    return True


def find_sorted_pairs(packets):
    i = 0
    right_order = []
    iteration = 0
    answer_part1 = 0
    while True:
        logging.debug('----------------')
        res = packets_in_right_order(packets[i],
                                     packets[i+1])
        logging.debug(f'Packets in right order?: {res}')
        right_order.append(res)
        iteration += 1
        i += 2
        if res:
            answer_part1 += iteration
        if i > len(packets)-1:
            break
    return answer_part1


def bubble_sort_packets(packets):
    '''Implement bubble sort'''
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(packets)-1):
            if not packets_in_right_order(packets[i], packets[i+1]):
                tmp = packets[i]
                packets[i] = packets[i+1]
                packets[i+1] = tmp
                sorted = False
    return packets


def print_packets(packets):
    for item in packets:
        print(item)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG) # uncomment to enable debugging log
    input = import_text_file(isDemoSet=True)
    packets = process_input(input)
    answer_part1 = find_sorted_pairs(packets)
    print('Answer to part 1 is:', answer_part1)
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = bubble_sort_packets(packets)
    i = sorted_packets.index([[2]])+1
    j = sorted_packets.index([[6]])+1
    print('Answer to part 2 is:', i*j)
