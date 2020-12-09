from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]

PREAMBLE_SIZE = 25


def find_invalid_number(num_sequence):
    for index in range(PREAMBLE_SIZE, len(num_sequence)):
        current_number = num_sequence[index]
        candidate_range = num_sequence[index - PREAMBLE_SIZE:index]
        is_valid = False

        for candidate_one in candidate_range:
            candidate_two = current_number - candidate_one

            if candidate_two in candidate_range:
                is_valid = True
                break

        if not is_valid:
            return current_number

    raise Exception('could not find the invalid number in the sequence.')


def solve1():
    numbers = list(map(int, get_input_lines(FILE_NUM)))

    return find_invalid_number(numbers)


def solve2():
    numbers = list(map(int, get_input_lines(FILE_NUM)))
    invalid_number = find_invalid_number(numbers)

    for start_index in range(len(numbers) - 1):
        accumulated_sum = numbers[start_index]

        for last_index in range(start_index + 1, len(numbers)):
            accumulated_sum += numbers[last_index]

            if accumulated_sum == invalid_number:
                target_sequence = numbers[start_index:last_index + 1]

                return min(target_sequence) + max(target_sequence)
            elif accumulated_sum > invalid_number:
                break


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
