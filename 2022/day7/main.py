from import_text_file import import_text_file
import logging
from collections import defaultdict

MAX_SIZE = 100_000


def parse_size_dict_from(txt: str):
    cwd = []
    SZ = defaultdict(int)  # Use so we don't need to initialize each key
    for item in txt.splitlines():
        words = item.split(' ')
        if words[1] == 'cd':
            if words[2] == '..':
                cwd.pop()
            elif words[2] == '/':
                cwd = []
            else:
                cwd.append(words[2])
        elif words[1] == 'ls':
            continue
        else:
            if words[0] == 'dir':
                continue
            else:
                # add current size to current directory and all parent directories.
                for i in range(len(cwd)+1):
                    index_path = '/'+'/'.join(cwd[:i])
                    SZ[index_path] += int(words[0])
    return SZ


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    txt = import_text_file(isDemoSet=False)
    SZ = parse_size_dict_from(txt)

    # Part 1: Calculate total size of directories smaller than 100_000.
    ans_part1 = 0
    for k, v in SZ.items():
        if v <= MAX_SIZE:
            ans_part1 += v
    print('answer part 1:', ans_part1)

    # Part 2: Determine size of smallest directory that can be deleted to free up enough space for the update.
    total_disksize = 70000000
    space_needed = 30000000
    dir_sizes = list(SZ.values())
    dir_sizes.sort(reverse=False)
    current_space_available = total_disksize - dir_sizes[-1]
    space_to_free = space_needed - current_space_available

    ans_part2 = 0
    for item in dir_sizes:
        if space_to_free < item:
            ans_part2 = item
            break
    print('answer to part 2:', ans_part2)
