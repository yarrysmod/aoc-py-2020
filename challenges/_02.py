from re import compile
from common import exec_func, get_input_lines

reg = compile("(\\d+)-(\\d+) (\\w): (\\w+)")


def solve1():
    return len(list(
        filter(is_valid_1, get_input_lines('02'))
    ))


def solve2():
    return len(list(
        filter(is_valid_2, get_input_lines('02'))
    ))


def is_valid_1(line) -> bool:
    match = reg.match(line)
    min_occurrences = int(match.group(1))
    max_occurrences = int(match.group(2))
    char = match.group(3)
    valid_chars = list(filter(lambda x: x == char, list(match.group(4))))

    return min_occurrences <= len(valid_chars) <= max_occurrences


def is_valid_2(line) -> bool:
    match = reg.match(line)
    match_index = int(match.group(1)) - 1
    second_index = int(match.group(2)) - 1
    char = match.group(3)
    password = list(match.group(4))

    return (password[match_index] == char) != (password[second_index] == char)


if __name__ == "__main__":
    exec_func(solve1)
    exec_func(solve2)
