from import_text_file import import_text_file


def process_input(input: str):
    for item in input.splitlines():
        print(item)


if __name__ == '__main__':
    input = import_text_file(isDemoSet=True)
    output = process_input(input)
