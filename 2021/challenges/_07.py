from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    crab_pos = [int(x) for x in lines[0].split(',')]

    unique_pos = list(set(crab_pos))
    count_pos = [len([x for x in crab_pos if x == up]) for up in unique_pos]
    cost_pos = []

    for to_pos in unique_pos:
        current_cost = 0

        for from_index in range(len(unique_pos)):
            from_pos, count = unique_pos[from_index], count_pos[from_index]

            current_cost += count * abs(to_pos - from_pos)

        cost_pos.append(current_cost)

    return min(cost_pos)


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))

    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
