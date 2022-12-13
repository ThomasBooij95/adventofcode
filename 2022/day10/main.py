from import_text_file import import_text_file


def get_signal_strength(input: str, verbose=False) -> "tuple[int, list]":
    cycle = 0
    cum = [[cycle, 1]]
    for item in input.splitlines():
        if item.split(" ")[0] == 'noop':
            cycle += 1
            if verbose:
                print('no operation: new cycle count: ', cycle)
        elif item.split(" ")[0] == 'addx':
            amount = int(item.split(" ")[1])
            if verbose:
                print('add folling amount:', amount)
            cycle += 2
            last_sum = cum[-1]
            cur_sum = [cycle, last_sum[1]+amount]
            if verbose:
                print(cur_sum)
            cum.append([cycle, last_sum[1]+amount])
    lookup_items = [20, 60, 100, 140, 180, 220]
    signal_strength = []

    for lookup_item in lookup_items:
        for i in range(len(cum)):
            item = cum[i]
            if item[0] >= lookup_item:
                signal_strength.append(lookup_item*cum[i-1][1])
                break
    if verbose:
        print(sum(signal_strength))
    return sum(signal_strength), cum


def print_cathode(input, cum):
    total_cycles = 240
    CTR = {'width': 40,
           'height': 6}
    sprite_center = 1
    output = []
    for cycle in range(1, total_cycles+1):
        sprite_center = get_register_value(cycle, cum)
        sprite_locations = [sprite_center-1, sprite_center, sprite_center+1]
        if (cycle-1) % 40 in sprite_locations:
            output.append('#')
        else:
            output.append('.')

    for row_index in range(CTR['height']):
        cur_row_list = output[row_index*CTR['width']:row_index*CTR['width']+CTR['width']]
        cur_row = "".join(cur_row_list)
        print(cur_row)


def get_register_value(cycle, cum) -> int:
    lookup_item = cycle
    for i in range(len(cum)):
        item = cum[i]
        if item[0] >= lookup_item:
            return int(cum[i-1][1])
    return cum[-1][1]


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    answer_part1, cum = get_signal_strength(input, verbose=False)
    print('Answer to part 1 is:', answer_part1)
    print('Answer to part 2 is:')
    print_cathode(input, cum)
