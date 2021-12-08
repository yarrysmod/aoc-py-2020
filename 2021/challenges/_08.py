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
    total_count = 0

    for line in lines:
        numbers: list
        output: list
        numbers, output = [[sorted(list(y)) for y in x.split(' ')] for x in line.split(' | ')]
        numbers.sort(key=lambda num: len(num))

        relevant_numbers = get_correct_nums(numbers)

        total_count += int(''.join([str(relevant_numbers.index(op)) for op in output]))

        pass

    return total_count


def get_correct_nums(numbers):
    combos = [None, numbers[0], None, None, numbers[2], None, None, numbers[1], numbers[9], None]

    zero_six_nine = numbers[6:9]
    combos[9] = [num for num in zero_six_nine if len([y for y in combos[4] if y in num]) == len(combos[4])][0]
    zero_six_nine.remove(combos[9])
    combos[0] = [num for num in zero_six_nine if len([y for y in combos[7] if y in num]) == len(combos[7])][0]
    zero_six_nine.remove(combos[0])
    combos[6] = zero_six_nine[0]

    two_three_five = numbers[3:6]
    combos[3] = [num for num in two_three_five if len([y for y in combos[1] if y in num]) == len(combos[1])][0]
    two_three_five.remove(combos[3])
    one_four_intersect = [digit for digit in combos[4] if digit not in combos[1]]
    combos[5] = [
        num for num in two_three_five
        if len([y for y in one_four_intersect if y in num]) == len(one_four_intersect)
    ][0]
    two_three_five.remove(combos[5])
    combos[2] = two_three_five[0]

    return combos


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
