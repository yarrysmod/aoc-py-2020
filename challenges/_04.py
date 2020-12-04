from common import exec_func, get_input_lines_stream
from re import compile

FILE_NUM = '04'
REQUIRED_FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
HEIGHT_UNIT_BOUNDS = {
    'cm': [150, 193],
    'in': [59, 76],
}
HAIR_COLOR_REGEX = compile('^#[0-9a-f]{6}$')


def height_check(val):
    unit, size = val[-2:], val[:-2]

    if unit in HEIGHT_UNIT_BOUNDS and size.isnumeric():
        min_bound, max_bound = HEIGHT_UNIT_BOUNDS[unit]
        return min_bound <= int(size) <= max_bound

    return False


VALID_CHECKS = {
    'byr': lambda val: 1920 <= int(val) <= 2002,
    'iyr': lambda val: 2010 <= int(val) <= 2020,
    'eyr': lambda val: 2020 <= int(val) <= 2030,
    'hgt': height_check,
    'hcl': lambda val: HAIR_COLOR_REGEX.match(val) is not None,
    'ecl': lambda val: val in VALID_EYE_COLORS,
    'pid': lambda val: val.isnumeric() and len(val) == 9,
}


def valid1(passport: dict):
    for column in REQUIRED_FIELDS:
        if column not in passport:
            return False

    return True


def valid2(passport: dict):
    for column in REQUIRED_FIELDS:
        if column not in passport or VALID_CHECKS[column](passport[column]) is False:
            return False

    return True


def solve1(valid_func=valid1):
    current_passport = {}
    valid_pass_count = 0

    for line in get_input_lines_stream(FILE_NUM).read().split('\n\n'):
        segments = line.split()

        for key, value in map(lambda segment: segment.split(':'), segments):
            current_passport[key] = value

        valid_pass_count += valid_func(current_passport)
        current_passport = {}

    return valid_pass_count


def solve2():
    return solve1(valid2)


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
