from common import exec_func, get_input_lines_stream
from re import compile

FILE_NUM = '04'
REQUIRED_FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
HEIGHT_REGEX = compile('(\\d+)(\\w+)')
HEIGHT_UNIT_CHECKS = {
    'cm': lambda val: 150 <= int(val) <= 193,
    'in': lambda val: 59 <= int(val) <= 76
}
HAIR_COLOR_REGEX = compile('^#[0-9a-f]{6}$')


def height_check(val):
    match = HEIGHT_REGEX.match(val)
    size = match.group(1)
    unit = match.group(2)

    if unit in HEIGHT_UNIT_CHECKS and size.isnumeric():
        return HEIGHT_UNIT_CHECKS[unit](size)

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
    return all(column in passport for column in REQUIRED_FIELDS)


def valid2(passport: dict):
    if valid1(passport):
        is_valid = all(VALID_CHECKS[column](passport[column]) for column in REQUIRED_FIELDS)
        return is_valid

    return False


def solve1(valid_func=valid1):
    current_passport = {}
    valid_pass_count = 0

    with get_input_lines_stream(FILE_NUM) as f:
        for line in f:
            line = line.rstrip()

            if line:
                segments = line.split(' ')
                for key, value in map(lambda segment: segment.split(':'), segments):
                    current_passport[key] = value
            else:
                valid_pass_count += valid_func(current_passport)
                current_passport = {}

    valid_pass_count += valid_func(current_passport)

    return valid_pass_count


def solve2():
    return solve1(valid2)


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
