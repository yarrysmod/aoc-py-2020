from math import cos, sin, radians

from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SUBFOLDER = 'samples'

X_MOVES = ['E', 'W']
Y_MOVES = ['N', 'S']
TILT_MOVES = ['L', 'R']
FORWARD_MOVE = 'F'


def solve1(is_sample=False):
    lines = get_input_lines(FILE_NUM, SUBFOLDER if is_sample else None)
    instructions = [[inst[0], int(inst[1:])] for inst in lines]
    props = {
        'x': 0,
        'y': 0,
        'tilt_deg': 0
    }

    for instruction, units in instructions:
        if instruction == FORWARD_MOVE:
            rads = radians(props['tilt_deg'])
            x_ratio = cos(rads)
            y_ratio = sin(rads)

            props['x'] += x_ratio * units
            props['y'] += y_ratio * units

            continue

        multiplier = 1
        prop = ''

        if instruction in X_MOVES:
            prop, multiplier = 'x', -1 if X_MOVES.index(instruction) == 1 else 1
        elif instruction in Y_MOVES:
            prop, multiplier = 'y', -1 if Y_MOVES.index(instruction) == 1 else 1
        elif instruction in TILT_MOVES:
            prop, multiplier = 'tilt_deg', -1 if TILT_MOVES.index(instruction) == 1 else 1

        props[prop] += multiplier * units

    return round(abs(props['x']) + abs(props['y']))


def solve2():
    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True), 25)
    exec_func(solve1, 1482)
    exec_func(solve2)
