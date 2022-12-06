from import_text_file import import_text_file

'''
Day 6. Detect start of packet.
Start of packet part 1: 4 characters all different.
Start of packet part 2: 14 characters all different.
'''


def find_first_marker_position(inputstring: str, marker_length: int):
    i = 1
    cur_marker = ''
    for char in inputstring:
        if char not in cur_marker and len(cur_marker) >= marker_length-1:
            cur_marker += char
            return i
        if char in cur_marker:
            cur_marker = cur_marker[str(cur_marker).find(char)+1:]
        cur_marker += char
        i += 1
    raise RuntimeError('No marker found')


if __name__ == '__main__':
    inputstring = import_text_file(isDemoSet=False)
    print('Answer to part 1: ', find_first_marker_position(
        inputstring=inputstring, marker_length=4))
    print('Answer to part 2: ', find_first_marker_position(
        inputstring=inputstring, marker_length=14))
