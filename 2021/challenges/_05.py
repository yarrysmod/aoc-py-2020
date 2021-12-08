from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def get_max(instructions):
    return max([max(i) for i in instructions])


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    instructions = get_instructions(lines)
    max_coord = get_max(instructions)
    field = get_field(max_coord + 1, max_coord + 1)

    populate_field(field, instructions)

    return get_danger_count(field)


def get_instructions(lines):
    instructions = []

    for line in lines:
        from_xy, to_xy = line.split(' -> ')
        x1, y1 = [int(x) for x in from_xy.split(',')]
        x2, y2 = [int(x) for x in to_xy.split(',')]
        instructions.append([x1, y1, x2, y2])

    return instructions


def get_danger_count(field):
    danger_count = 0

    for row in field:
        for cell in row:
            if cell > 1:
                danger_count += 1

    return danger_count


def draw_vertical_line(field, x, y1, y2):
    y_range = range(y1, y2 + 1) if y2 > y1 else range(y1, y2 - 1, -1)

    for y in y_range:
        field[y][x] += 1


def draw_horizontal_line(field, y, x1, x2):
    x_range = range(x1, x2 + 1) if x2 > x1 else range(x1, x2 - 1, -1)

    for x in x_range:
        field[y][x] += 1


def draw_diagonal_line(field, x1, x2, y1, y2):
    x = x1
    y = y1
    steps = abs(x2 - x1)

    for step in range(steps + 1):
        field[y][x] += 1

        x += 1 if x2 > x else -1
        y += 1 if y2 > y else -1


def populate_field(field, instructions, include_diagonals=False):
    for inst in instructions:
        x1, y1, x2, y2 = inst

        is_vertical = x1 == x2
        is_horizontal = y1 == y2

        if is_vertical:
            draw_vertical_line(field, x1, y1, y2)
        elif is_horizontal:
            draw_horizontal_line(field, y1, x1, x2)
        elif include_diagonals:
            draw_diagonal_line(field, x1, x2, y1, y2)


def get_field(max_x, max_y):
    field = []

    for y in range(0, max_y):
        field.append([0] * max_x)

    return field


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    instructions = get_instructions(lines)
    max_coord = get_max(instructions)
    field = get_field(max_coord + 1, max_coord + 1)

    populate_field(field, instructions, True)

    return get_danger_count(field)


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
