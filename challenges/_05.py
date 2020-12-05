from typing import List

from common import exec_func, get_input_lines, get_input_lines_stream

FILE_NUM = '05'

SEATS_PER_ROW = 8
MAX_ROW_INDEX = 127
MAX_SEAT_INDEX = 7


def get_slot_range(row_range: List[int], do_get_lower_half=False):
    half_range = int((row_range[1] - row_range[0] + 1) / 2)

    if do_get_lower_half:
        row_range[1] -= half_range
    else:
        row_range[0] += half_range

    return row_range


def get_slot(slot_commands: List[str], is_seat_slot=False) -> int:
    slot_range = [0, MAX_SEAT_INDEX] if is_seat_slot else [0, MAX_ROW_INDEX]
    lower_indicator = 'L' if is_seat_slot else 'F'

    for slot_command in slot_commands:
        slot_range = get_slot_range(slot_range, slot_command == lower_indicator)

    return slot_range[0]


def get_seat_id(command_line: str) -> int:
    row_commands = list(command_line[:7])
    seat_commands = list(command_line[7:])
    row_num = get_slot(row_commands)
    seat_num = get_slot(seat_commands, is_seat_slot=True)

    return row_num * SEATS_PER_ROW + seat_num


def get_sorted_abstract_instructions() -> List[int]:
    return sorted(map(lambda bin_num: int(bin_num, 2), get_input_lines_stream(FILE_NUM)
                      .read()
                      .replace('F', '0')
                      .replace('B', '1')
                      .replace('L', '0')
                      .replace('R', '1')
                      .split()
                      ))


def get_actual_instruction(instruction_num: int) -> str:
    directions = bin(instruction_num)[2:]
    back_forward_directions = directions[:7] \
        .replace('0', 'F') \
        .replace('1', 'B')
    left_right_directions = directions[7:] \
        .replace('0', 'L') \
        .replace('1', 'R')

    return back_forward_directions + left_right_directions


def solve1():
    highest_instruction = get_actual_instruction(get_sorted_abstract_instructions()[-1])

    return get_seat_id(highest_instruction)


def solve2():
    lines = get_sorted_abstract_instructions()
    last_index = 0

    for current_index in range(1, len(lines)):
        if (lines[current_index] - lines[last_index]) > 1:
            return get_seat_id(get_actual_instruction(lines[current_index] - 1))

        last_index = current_index


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
