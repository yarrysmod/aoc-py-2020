from common import exec_func, get_input_lines_stream

FILE_NUM = '06'


def solve1():
    lines = get_input_lines_stream(FILE_NUM).read().split('\n\n')
    return sum([len(set(line.replace('\n', ''))) for line in lines])


def solve2():
    lines = get_input_lines_stream(FILE_NUM).read().split('\n\n')
    answered_question_count = 0

    for line in lines:
        questions = set(line.replace('\n', ''))
        participants = line.split()

        for question in questions:
            is_answered_by_all = True

            for participant in participants:
                if question not in participant:
                    is_answered_by_all = False
                    break

            answered_question_count += is_answered_by_all

    return answered_question_count


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
