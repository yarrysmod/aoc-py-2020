from common import exec_func, get_input_lines_stream

FILE_NUM = '06'


def get_groups():
    return get_input_lines_stream(FILE_NUM).read().split('\n\n')


def solve1():
    return sum([len(set(group.replace('\n', ''))) for group in get_groups()])


def solve2():
    answered_question_count = 0

    for group in get_groups():
        lines = group.split()
        chars = lines.pop()

        for line in lines:
            for char in chars:
                if char not in line:
                    chars = chars.replace(char, '')

        answered_question_count += len(chars)

    return answered_question_count


if __name__ == '__main__':
    exec_func(solve1, 6947)
    exec_func(solve2, 3398)
