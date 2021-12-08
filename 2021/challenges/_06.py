from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    fishes = [int(x) for x in lines[0].split(',')]

    for step in range(80):
        fish_count = range(len(fishes))

        for fish_index in fish_count:
            fishes[fish_index] -= 1

            if fishes[fish_index] < 0:
                fishes[fish_index] = 6
                fishes.append(8)

    return len(fishes)


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))

    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
