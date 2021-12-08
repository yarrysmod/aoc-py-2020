from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    total_count = 0

    for line in lines:
        numbers: list
        output: list
        numbers, output = [[sorted(list(y)) for y in x.split(' ')] for x in line.split(' | ')]
        numbers.sort(key=lambda num: len(num))

        relevant_numbers = [numbers[0], numbers[1], numbers[2], numbers[9]]  # 1, 7, 4, 8

        total_count += len([op for op in output if op in relevant_numbers])

        pass

    return total_count


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))

    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
