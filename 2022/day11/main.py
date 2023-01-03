from import_text_file import import_text_file
import re
import logging
import numpy as np
'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
'''


class Monkey:
    total_items_processed = 0

    def __init__(self,
                 id:                 int,
                 starting_items:     'list[int]',
                 operation,
                 test_divisor:       int,
                 throw_to_monkeys:   'list[int]') -> None:
        self.id = id
        self.items = starting_items
        self.worry_func = operation
        self.test_divisor = test_divisor
        self.throw_to_monkeys = throw_to_monkeys
        pass

    def __repr__(self) -> str:
        return f'Monkey {self.id} holding {len(self.items)} items'

    def increase_worry_first_item(self):
        old = self.items[0]
        self.items[0] = eval(self.worry_func)
        logging.debug(f'Worry level is changed to {self.items[0]}')

    def decrease_worry_first_item(self):
        self.items[0] = int(np.floor(self.items[0]/3))
        logging.debug(f'Worry level is decreased to {self.items[0]}')

    def test_first_item(self):
        if self.items[0] % self.test_divisor == 0:
            self.items[0] = self.items[0] % self.test_divisor
            logging.debug(
                f'Worry level is divisible by {self.test_divisor}, throw item to {self.throw_to_monkeys[0]}')
            return self.throw_to_monkeys[0]
        else:
            self.items[0] = self.items[0] % self.test_divisor
            logging.debug(
                f'Worry level is not divisible by {self.test_divisor}, throw item to {self.throw_to_monkeys[1]}')
            return self.throw_to_monkeys[1]

    def remove_first_item(self):
        logging.debug(
            f'Monkey {self.id} does not have item with worry level {self.items[0]} anymore')
        self.items.pop(0)

    def catch(self, caught_object: int):
        logging.debug(
            f'Monkey {self.id} caught item with worry level {caught_object}')
        self.items.append(caught_object)

    def has_items(self) -> bool:
        logging.debug(
            f'Monkey {self.id} has {len(self.items)} items')
        return len(self.items) > 0

    def increase_processing_counter(self):
        self.total_items_processed += 1
        logging.debug(
            f'Monkey {self.id} has processed {self.total_items_processed} items')


def create_monkeys(input: str) -> 'list[Monkey]':
    monkeys = []
    for item in input.splitlines():
        if re.match("^Monkey", item):
            cur_id = re.findall("\d+", item)[0]
        if re.match("^  Starting", item):
            cur_starting_items = [int(x) for x in re.findall("\d+", item)]
        if re.match("^  Operation", item):
            cur_operation = re.sub("  Operation: new = ", "", item)
        if re.match("^  Test", item):
            cur_test_divisor = int(re.findall("\d+", item)[0])
        if re.match("^    If true:", item):
            cur_throw_to_monkeys = [int(re.findall("\d+", item)[0])]
        if re.match("^    If false:", item):
            cur_throw_to_monkeys.append(            # type: ignore
                int(re.findall("\d+", item)[0]))
        if item == '':
            monkeys.append(Monkey(cur_id, cur_starting_items, cur_operation,  # type: ignore
                           cur_test_divisor, cur_throw_to_monkeys))  # type: ignore
    monkeys.append(Monkey(cur_id, cur_starting_items, cur_operation,  # type: ignore
                          cur_test_divisor, cur_throw_to_monkeys))  # type: ignore
    print(monkeys)
    return monkeys


def get_processing_counts(monkey_array: 'list[Monkey]'):
    nr_of_rounds = 20
    for round_nr in range(nr_of_rounds):
        logging.debug(f'----------- Start of Round {round_nr+1} -----------')
        for monkey in monkey_array:
            while monkey.has_items():
                monkey.increase_worry_first_item()
                monkey.decrease_worry_first_item()
                catcher_id = monkey.test_first_item()
                monkey_array[catcher_id].catch(monkey.items[0])
                monkey.remove_first_item()
                monkey.increase_processing_counter()

    counts = [monkey.total_items_processed for monkey in monkey_array]
    return counts


def get_processing_counts_part_2(monkey_array: 'list[Monkey]'):
    nr_of_rounds = 10_000
    for round_nr in range(nr_of_rounds):
        logging.warning(
            f'----------- Start of Round {round_nr+1} -----------')
        for monkey in monkey_array:
            if monkey.has_items():
                logging.debug(
                    f'current worry_level of first item {monkey.items[0]}')
            while monkey.has_items():
                monkey.increase_worry_first_item()
                catcher_id = monkey.test_first_item()
                logging.debug(
                    f'current worry level of first item = {monkey.items[0]}')
                monkey_array[catcher_id].catch(monkey.items[0])
                monkey.remove_first_item()
                monkey.increase_processing_counter()

    counts = [monkey.total_items_processed for monkey in monkey_array]
    return counts


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    input = import_text_file(isDemoSet=True)
    # monkey_array = create_monkeys(input)
    # counts = get_processing_counts(monkey_array)
    # counts.sort(reverse=True)

    # answer_part1 = counts[0]*counts[1]
    # print('Answer to part 1 is:', answer_part1)
    # # Part 2
    monkey_array = create_monkeys(input)
    counts = get_processing_counts_part_2(monkey_array)
    counts.sort(reverse=True)
    answer_part2 = counts[0]*counts[1]
    print(counts)
    print('Answer to part 2 is:', answer_part2)
