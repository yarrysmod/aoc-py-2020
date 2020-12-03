from math import prod

from common import get_input_lines, exec_func

TREE_CHAR = '#'
FILE_NUM = '03'


def solve1_old():
    tree_lines = list(get_input_lines(FILE_NUM))
    line_length = len(tree_lines[0])
    tree_count = 0
    x = 0

    for (line_index, tree_line) in enumerate(tree_lines):
        tree_count += tree_line[x] == TREE_CHAR
        x = (x + 3) % line_length

    return tree_count


def solve1(x_steps=3, y_steps=1, tree_lines=None):
    if tree_lines is None:
        tree_lines = list(get_input_lines(FILE_NUM))

    line_length = len(tree_lines[0])
    tree_count = 0
    x = 0

    for line_index in range(0, len(tree_lines), y_steps):
        tree_count += tree_lines[line_index][x] == TREE_CHAR
        x = (x + x_steps) % line_length

    return tree_count


def solve2_old():
    tree_lines = list(get_input_lines('03'))
    line_length = len(tree_lines[0])
    logic_list = [
        {
            'x': 0,
            'increment_by': 1,
            'check_every': 1,
            'count': 0
        },
        {
            'x': 0,
            'increment_by': 3,
            'check_every': 1,
            'count': 0
        },
        {
            'x': 0,
            'increment_by': 5,
            'check_every': 1,
            'count': 0
        },
        {
            'x': 0,
            'increment_by': 7,
            'check_every': 1,
            'count': 0
        },
        {
            'x': 0,
            'increment_by': 1,
            'check_every': 2,
            'count': 0
        }
    ]

    for (line_index, tree_line) in enumerate(tree_lines):
        for logic_line in logic_list:
            check_modulo = logic_line['check_every']

            if line_index % check_modulo != 0:
                continue

            x = logic_line['x']

            logic_line['count'] += tree_line[x] == TREE_CHAR
            logic_line['x'] = (x + logic_line['increment_by']) % line_length

    return prod(map(lambda x: x.get('count'), logic_list))


def solve2():
    solve_iterations = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    line_prod = 1

    for iter_prod in [solve1(i[0], i[1]) for i in solve_iterations]:
        line_prod *= iter_prod

    return line_prod


if __name__ == '__main__':
    exec_func(solve1_old)
    exec_func(solve1)

    exec_func(solve2_old)
    exec_func(solve2)
