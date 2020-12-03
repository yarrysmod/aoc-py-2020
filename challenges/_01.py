from itertools import combinations
from math import prod
from common import exec_func, get_input_lines


def solve1(num_values=2):
    challenge_input = list(map(int, get_input_lines('01')))

    for combination in combinations(challenge_input, num_values):
        if sum(combination) == 2020:
            return prod(combination)


def solve2():
    return solve1(3)


if __name__ == "__main__":
    exec_func(solve1)
    exec_func(solve2)
