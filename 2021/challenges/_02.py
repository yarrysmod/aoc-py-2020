from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'

y_moves = ['up', 'down']


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    coords = {
        'x': 0,
        'y': 0
    }

    for line in lines:
        direction, units = line.split(' ')
        coord = 'x'
        is_addition = True

        if direction in y_moves:
            coord = 'y'
            if direction == y_moves[0]:
                is_addition = False

        if is_addition:
            coords[coord] += int(units)
        else:
            coords[coord] -= int(units)

    return coords['x'] * coords['y']


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    h_pos, depth, aim = 0, 0, 0

    for line in lines:
        direction, units = line.split(' ')
        units = int(units)

        if direction == 'forward':
            h_pos += units
            depth += aim * units
        elif direction == 'up':
            aim -= units
        else:
            aim += units

    return h_pos * depth


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
