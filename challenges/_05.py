from typing import List

from common import exec_func, get_input_lines

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


def solve1():
    highest_seat_id = 0

    for line in get_input_lines(FILE_NUM):
        seat_id = get_seat_id(line)

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def solve2():
    pass # TODO


if __name__ == '__main__':
    exec_func(solve1)
    exec_func(solve2)
