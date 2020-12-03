from re import compile
from typing import Callable
from common import exec_func, get_input_lines, get_input_lines_stream

FILE_NUM = '02'
reg = compile("(\\d+)-(\\d+) (\\w): (\\w+)")


def solve1_old():
    return len(list(filter(valid_1_old, get_input_lines(FILE_NUM))))


def solve2_old():
    return len(list(filter(valid_2_old, get_input_lines(FILE_NUM))))


def valid_1_old(line) -> bool:
    match = reg.match(line)
    min_occurrences = int(match.group(1))
    max_occurrences = int(match.group(2))
    char = match.group(3)
    valid_chars = list(filter(lambda x: x == char, list(match.group(4))))

    return min_occurrences <= len(valid_chars) <= max_occurrences


def valid_2_old(line) -> bool:
    match = reg.match(line)
    match_index = int(match.group(1)) - 1
    second_index = int(match.group(2)) - 1
    char = match.group(3)
    password = list(match.group(4))

    return (password[match_index] == char) != (password[second_index] == char)


def call_parsed(line: str, callback: Callable):
    range_indicator_index = line.index('-')
    char_delimiter = line.index(' ')
    password_delimiter = line.index(': ')

    min_occurrences = int(line[:range_indicator_index])
    max_occurrences = int(line[range_indicator_index + 1:char_delimiter])
    char = line[char_delimiter + 1:password_delimiter]
    password = line[password_delimiter + 2:]

    # ____ seems the way below is still too slow...
    # left_part, password = line.split(': ')
    # range_part, char = left_part.split(' ')
    # min_occurrences, max_occurrences = list(map(int, range_part.split('-')))

    return callback(min_occurrences, max_occurrences, char, password)


def valid1(min_occurrences, max_occurrences, char, password):
    return min_occurrences <= len([x for x in password if x == char]) <= max_occurrences


def solve1(condition=valid1):
    valid_passwords = 0

    with get_input_lines_stream(FILE_NUM) as f:
        for line in f:
            valid_passwords += call_parsed(line, condition)

    return valid_passwords


def valid2(min_occurrences, max_occurrences, char, password):
    return (password[min_occurrences - 1] == char) != (password[max_occurrences - 1] == char)


def solve2():
    return solve1(valid2)


if __name__ == "__main__":
    exec_func(solve1_old)
    exec_func(solve1)

    exec_func(solve2_old)
    exec_func(solve2)
