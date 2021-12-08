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
            cost_per_unit = abs(to_pos - from_pos)

            current_cost += count * cost_per_unit

        cost_pos.append(current_cost)

    return min(cost_pos)


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    crab_pos = [int(x) for x in lines[0].split(',')]

    all_pos = [x for x in range(max(crab_pos) + 1)]
    count_pos = [len([x for x in crab_pos if x == up]) for up in all_pos]
    cost_pos = []

    for to_pos in all_pos:
        current_cost = 0

        for from_index in range(len(all_pos)):
            from_pos, count = all_pos[from_index], count_pos[from_index]
            change_per_unit = abs(to_pos - from_pos)

            if change_per_unit:
                cost_per_unit = (change_per_unit * (change_per_unit + 1)) / 2
                current_cost += count * cost_per_unit

        cost_pos.append(current_cost)

    return min(cost_pos)


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
