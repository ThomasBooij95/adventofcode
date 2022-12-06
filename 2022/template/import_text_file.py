from pathlib import Path
import os


def import_text_file(cwd) -> str:
    if os.environ['DEMO_SET'] == True:
        file = str(cwd)+'/demo-input.txt'
    else:
        file = '/test-input.txt'
    p = Path(__file__).with_name(file)
    with p.open('r') as f:
        return f.read()
