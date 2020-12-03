from math import prod

from common import get_input_lines, exec_func

TREE_CHAR = '#'


def solve1():
    tree_lines = list(get_input_lines('03'))
    line_length = len(tree_lines[0])
    tree_count = 0
    x = 0

    for (line_index, tree_line) in enumerate(tree_lines):
        has_hit_tree = tree_line[x] == TREE_CHAR
        tree_count += 1 if has_hit_tree else 0
        x = (x + 3) % line_length

    return tree_count


def solve2():
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


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
