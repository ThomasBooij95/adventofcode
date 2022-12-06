from import_text_file import import_text_file
from enum import Enum

'''
Day 2: Rock paper sissors tournament. 
Total score: Sum(list_round_scores)
Round score: Shape_points + outcome_points
Shape points: 1 for Rock, 2 for Paper, 3 for Scissors

A: Opponent Rock
B: Opponent Paper
C: Opponent Scissor

X: Player Rock
Y: Player Paper
Z: Player Scissor
'''


class Shape_points(Enum):
    X = 1
    Y = 2
    Z = 3


class Outcome_points(Enum):
    loss = 0
    draw = 3
    win = 6


class Rules(Enum):
    AX = 'draw'
    AY = 'win'
    AZ = 'loss'
    BX = 'loss'
    BY = 'draw'
    BZ = 'win'
    CX = 'win'
    CY = 'loss'
    CZ = 'draw'


def process_input(input: str):
    total_score = 0
    for item in input.splitlines():
        opponent = item[0]
        player = item[2]
        shape_points = calculate_shape_points(player)
        outcome_points = calculate_outcome_points(opponent, player)
        round_points = shape_points + outcome_points
        total_score += round_points
    return total_score


def calculate_outcome_points(opponent, player):
    result = Rules[opponent+player].value
    return Outcome_points[result].value


def calculate_shape_points(player):
    return Shape_points[player].value


if __name__ == '__main__':
    input = import_text_file(isDemoSet=False)
    print(process_input(input))
