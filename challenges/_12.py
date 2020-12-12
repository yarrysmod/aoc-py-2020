from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SUBFOLDER = 'samples'

X_MOVES = ['E', 'W']
Y_MOVES = ['N', 'S']
TILT_MOVES = ['R', 'L']

FORWARD_MOVE = 'F'
SINGLE_TURN = 90
ALL_MOVES = ['E', 'S', 'W', 'N']


def get_instructions(is_sample):
    lines = get_input_lines(FILE_NUM, SUBFOLDER if is_sample else None)
    instructions = [[inst[0], int(inst[1:])] for inst in lines]

    return instructions


def get_new_x(pos, move, units):
    modifier = -1 if X_MOVES.index(move) == 1 else 1

    return pos + modifier * units


def get_new_y(pos, move, units):
    modifier = -1 if Y_MOVES.index(move) == 1 else 1

    return pos + modifier * units


def solve1(is_sample=False):
    instructions = get_instructions(is_sample)
    x, y = 0, 0
    tilt_index = 0

    for instruction, units in instructions:
        if instruction in X_MOVES:
            x = get_new_x(x, instruction, units)
        elif instruction in Y_MOVES:
            y = get_new_y(y, instruction, units)
        elif instruction in TILT_MOVES:
            turns = int(units / SINGLE_TURN)

            if TILT_MOVES.index(instruction) == 0:
                tilt_index = (tilt_index + turns) % 4
            else:
                tilt_index = (tilt_index - turns) % 4
        elif instruction == FORWARD_MOVE:
            tilt_move = ALL_MOVES[tilt_index]

            if tilt_move in X_MOVES:
                x = get_new_x(x, tilt_move, units)
            else:
                y = get_new_y(y, tilt_move, units)

    return abs(x) + abs(y)


def solve2(is_sample=False):
    instructions = get_instructions(is_sample)
    wp_x, wp_y = 10, 1
    ship_x, ship_y = 0, 0

    for instruction, units in instructions:
        if instruction in X_MOVES:
            wp_x = get_new_x(wp_x, instruction, units)
        elif instruction in Y_MOVES:
            wp_y = get_new_y(wp_y, instruction, units)
        elif instruction in TILT_MOVES:
            is_clockwise = TILT_MOVES.index(instruction) == 0

            for _ in range(int(units / SINGLE_TURN)):
                if is_clockwise:
                    # x(n) = y(n-1), y(n) = -x(n-1)
                    wp_x, wp_y = wp_y, -wp_x
                else:
                    # x(n) = -y(n-1), y(n) = x(n-1)
                    wp_x, wp_y = -wp_y, wp_x
        if instruction == FORWARD_MOVE:
            ship_x += units * wp_x
            ship_y += units * wp_y

    return abs(ship_y) + abs(ship_x)


if __name__ == '__main__':
    exec_func(lambda: solve1(True), 25)
    exec_func(solve1, 1482)
    exec_func(lambda: solve2(True), 286)
    exec_func(solve2)
