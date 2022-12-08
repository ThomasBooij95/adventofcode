from import_text_file import import_text_file
import logging
from functools import reduce
'''
Day 7.1: Find directories with at most a total size of 100_000

First, make a datastructure of the file-tree. A dict of dicts seems appropriate. 
Sample dict:

sample_dict = {
    '/': {
        'dirs': {
            'a':
            {'dirs': {},
             'files': {
                'b.dat': 300
            }}
        },
        'files': {
            'a.txt': 200,
            'b.dat': 300
        }
    }
}

Sample Input:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
'''
sample_dict = {
    '/': {
        'dirs': {
            'a':
            {'dirs': {},
             'files': {
                'b.dat': 300
            }}
        },
        'files': {
            'a.txt': 200,
            'b.dat': 300
        }
    }
}


MAX_SIZE = 100_000


def initializeTree():
    return {
        'dirs': {},
        'files': {}}


def parse_to_tree(txt: str):
    tree = initializeTree()
    cwd = []
    instructions = txt.splitlines()
    num_of_instructions = len(instructions)
    i = 0
    while i < num_of_instructions:
        command = instructions[i]
        logging.info(f'cmd:{command}')
        if command.startswith('$ cd'):
            cwd = change_cwd(cwd, command)
            i += 1
        elif command.startswith('$ ls'):
            i += 1
            command = instructions[i]
            logging.info(command)
            while not command.startswith('$'):
                # logging.info('handle ls')
                if (i <= num_of_instructions-1):
                    tree = store_sizes_of_cwd(tree, command, cwd)
                else:
                    return tree
                i += 1
                if (i <= num_of_instructions-1):
                    command = instructions[i]  # go to next instruction.
        else:
            raise RuntimeError(f'unknown command: {command}')
    return tree


def store_sizes_of_cwd(tree, command: str, cwd):
    # print(tree)
    logging.debug(get_cwd_string(cwd))
    # print(command)
    if command.startswith('dir'):
        command = command.replace('dir ', '')
        keys = ['dirs']
        for item in cwd:
            keys.append(item)
            keys.append('dirs')

        current_node = {command: {
            'dirs': {},
            'files': {}
        }}
        return nested_set(tree, keys, current_node)
    else:  # store file and size.
        current_size = command.split(" ", 1)[0]
        current_key = command.split(" ", 1)[1]
        keys = []
        for item in cwd:
            keys.append('dirs')
            keys.append(item)
        keys.append('files')
        keys.append(current_key)
        return nested_set(tree, keys, current_size)


def nested_set(dic, keys, value, create_missing=True):
    d = dic
    for key in keys[:-1]:
        if key in d:
            d = d[key]
        elif create_missing:
            d = d.setdefault(key, {})
        else:
            return dic
    if keys[-1] in d or create_missing:
        d[keys[-1]] = value
    return dic


def change_cwd(cwd, command: str):
    direction = command.replace('$ cd ', '')
    if direction == '/':
        logging.info(f'change directory to home')
        return []
    elif direction == '..':
        cwd.pop()
    else:
        cwd.append(direction)

    cwd_string = get_cwd_string(cwd)
    logging.info(f'change directory to {cwd_string}')
    return cwd


def get_cwd_string(cwd):
    cwd_string = '/'+'/'.join(cwd)
    return cwd_string


def calculate_size_of(tree):
    dir_sizes = []
    # nonlocal totalsum

    def myprint(d,  visited_dirs):
        for k, v in d.items():
            if isinstance(v, dict):
                if k != 'dirs' and k != 'files':
                    visited_dirs.append(k)
                myprint(v, visited_dirs)
                # last_value = v
            else:
                nonlocal totalsum
                totalsum += int(v)
                # last_value = v
        print('wait here')
        if d != {}:
            if not isinstance(v, dict):  # type:ignore
                nonlocal list_of_sums
                list_of_sums.append(totalsum)
                totalsum = 0

    totalsum = 0
    list_of_sums = []
    myprint(tree, [])
    # print(totalsum)  # 18938388 -> 48381165(correct total size)
    return list_of_sums


def get_all_keys(d):
    for key, value in d.items():
        yield key
        if isinstance(value, dict):
            yield from get_all_keys(value)


if __name__ == '__main__':
    TOTAL_SUM = 0
    logging.basicConfig(level=logging.CRITICAL)
    txt = import_text_file(isDemoSet=True)
    tree = parse_to_tree(txt)
    size_of_dirs = calculate_size_of(tree)
    print(sum(size_of_dirs))
