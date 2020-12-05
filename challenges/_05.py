from typing import List

from common import exec_func, get_input_lines_stream

FILE_NUM = '05'

SEATS_PER_ROW = 8


def get_seat_id(instruction_num: int) -> int:
    bin_num = bin(instruction_num)[2:]
    row_count = int(bin_num[:7], 2)
    seat_num = int(bin_num[7:], 2)

    return row_count * SEATS_PER_ROW + seat_num


def get_sorted_abstract_instructions() -> List[int]:
    return sorted(map(lambda bin_num: int(bin_num, 2), get_input_lines_stream(FILE_NUM)
                      .read()
                      .replace('F', '0')
                      .replace('B', '1')
                      .replace('L', '0')
                      .replace('R', '1')
                      .split()
                      ))


def solve1():
    instruction_sum = get_sorted_abstract_instructions()[-1]

    return get_seat_id(instruction_sum)


def solve2():
    lines = get_sorted_abstract_instructions()
    last_index = 0

    for current_index in range(1, len(lines)):
        if (lines[current_index] - lines[last_index]) > 1:
            return get_seat_id(lines[current_index] - 1)

        last_index = current_index


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
