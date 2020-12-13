from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None))

    pass


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None))

    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
