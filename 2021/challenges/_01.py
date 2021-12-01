from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    values = [int(x) for x in lines]
    increment_count = 0

    for value_index in range(1, len(values)):
        previous_value = values[value_index - 1]
        current_value = values[value_index]

        if current_value > previous_value:
            increment_count += 1

    return increment_count


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    values = [int(x) for x in lines]
    increment_count = 0

    for value_index in range(3, len(values)):
        previous_value = sum(values[value_index-3:value_index])
        current_value = sum(values[value_index-2:value_index+1])

        if current_value > previous_value:
            increment_count += 1

    return increment_count


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
