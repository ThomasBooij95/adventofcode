from import_text_file import import_text_file

'''
Day 6. Detect start of packet.
Start of packet part 1: 4 characters all different.
Start of packet part 2: 14 characters all different.
'''


def process_input(input: str, marker_length):
    i = 1
    cur_marker = ''
    for char in input:
        if char not in cur_marker and len(cur_marker) >= marker_length-1:
            cur_marker += char
            return i
        if char in cur_marker:
            cur_marker = cur_marker[str(cur_marker).find(char)+1:]
        cur_marker += char
        i += 1
    raise RuntimeError('No marker found')


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    output = process_input(input, 14)
    print('part 1: ', process_input(input, 4))
    print('part 2: ', process_input(input, 14))
