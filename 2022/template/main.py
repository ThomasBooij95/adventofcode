from typing import List
from helpers.import_text_file import import_text_file
import os
from pathlib import Path
from .import_text_file import import_text_file

def process_input(input: str):
    for item in input.splitlines():
        pass
    pass


if __name__ == '__main__':
    input = import_text_file(os.getcwd()+'/2022/<insert>')
    output = process_input(input)
