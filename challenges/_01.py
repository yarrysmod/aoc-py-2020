from itertools import combinations
from math import prod
from common import exec_func, get_input_lines

TARGET_SUM = 2020
FILE_NUM = '01'


def solve1(total=TARGET_SUM, challenge_list=None):
    if challenge_list is None:
        challenge_list = sorted(map(int, filter(len, get_input_lines(FILE_NUM))))

    for num in challenge_list:
        required_num = total - num

        if required_num in challenge_list:
            return num * required_num


def solve2():
    challenge_list = sorted(map(int, filter(len, get_input_lines(FILE_NUM))))

    for num1_index, first_num in enumerate(challenge_list):
        total = TARGET_SUM - first_num
        inner_prod = solve1(total, challenge_list[num1_index:])

        if inner_prod is not None:
            return inner_prod * first_num


def solve1_old(num_values=2):
    challenge_input = list(map(int, get_input_lines(FILE_NUM)))

    for combination in combinations(challenge_input, num_values):
        if sum(combination) == TARGET_SUM:
            return prod(combination)


def solve2_old():
    return solve1_old(3)


if __name__ == "__main__":
    print('\n01.1')
    exec_func(solve1)

    print('\n01.2')
    exec_func(solve2)
