from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'

y_moves = ['up', 'down']


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    value_per_digit = [0] * len(lines[0])
    count_digits = len(lines[0])
    threshold = len(lines) / 2
    gamma, epsilon = 0, 0

    factor = 2 ** (count_digits - 1)

    for line in lines:
        values = list(map(int, line))

        for i in range(0, count_digits):
            value_per_digit[i] += values[i]

    for digit in range(0, count_digits):
        if value_per_digit[digit] > threshold:
            gamma += factor
        else:
            epsilon += factor

        factor /= 2

    return gamma * epsilon


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))

    oxygen_lines = []
    scrubber_lines = []
    count_digits = len(lines[0])

    for line in lines:
        if int(line[0]) == 1:
            oxygen_lines.append(line)
        else:
            scrubber_lines.append(line)

    for digit in range(0, count_digits):
        if digit == 0:
            oxygen_lines, scrubber_lines = get_split(lines, digit)
        else:
            if len(oxygen_lines) > 1:
                oxygen_lines = get_split(oxygen_lines, digit)[0]
            if len(scrubber_lines) > 1:
                scrubber_lines = get_split(scrubber_lines, digit)[1]

    return int(oxygen_lines[0], 2) * int(scrubber_lines[0], 2)


def get_split(lines: list, digit: int):
    split = [[], []]

    for line in lines:
        if line[digit] == '1':
            split[0].append(line)
        else:
            split[1].append(line)

    if len(split[0]) < len(split[1]):
        return [split[1], split[0]]

    return split


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
