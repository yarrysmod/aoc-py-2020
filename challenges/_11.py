from copy import deepcopy
from itertools import compress

from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SUBFOLDER = 'samples'

FLOOR = '.'
FREE_SEAT = 'L'
OCCUPIED_SEAT = '#'

coord_gens = [
    # horizontal
    lambda x, y, diff: [x + diff, y],
    lambda x, y, diff: [x - diff, y],

    # vertical
    lambda x, y, diff: [x, y + diff],
    lambda x, y, diff: [x, y - diff],

    # diagonal
    lambda x, y, diff: [x - diff, y - diff],
    lambda x, y, diff: [x + diff, y + diff],

    lambda x, y, diff: [x - diff, y + diff],
    lambda x, y, diff: [x + diff, y - diff],
]


def is_matching(list_a, list_b):
    for index in range(len(list_a)):
        if list_a[index] != list_b[index]:
            return False

    return True


def find_all_immediate_neighbors(row_index, seat_index, rows):
    neighbour_count = 0
    first_row = row_index - 1 if (row_index - 1) >= 0 else 0
    last_row = row_index + 2 if (row_index + 2) < len(rows) else len(rows)

    first_seat = seat_index - 1 if (seat_index - 1) >= 0 else 0
    last_seat = seat_index + 2 if (seat_index + 2) < len(rows[0]) else len(rows[0])

    for curr_row in range(first_row, last_row):
        for curr_seat in range(first_seat, last_seat):
            if curr_row == row_index and curr_seat == seat_index:
                continue

            neighbour_count += rows[curr_row][curr_seat] == OCCUPIED_SEAT

    return neighbour_count


def check_has_changed(original_rows, rows, seats_callback=find_all_immediate_neighbors, taken_tolerance=4):
    has_changed = False

    for row_index, row in enumerate(rows):
        for seat_index, seat in enumerate(row):
            if seat == FLOOR:
                continue

            neighbour_count = seats_callback(row_index, seat_index, original_rows)

            if seat == FREE_SEAT and neighbour_count == 0:
                row[seat_index] = OCCUPIED_SEAT
                has_changed = True
            elif seat == OCCUPIED_SEAT and neighbour_count >= taken_tolerance:
                row[seat_index] = FREE_SEAT
                has_changed = True

    return has_changed


def solve1(is_sample=False, seats_callback=find_all_immediate_neighbors, taken_tolerance=4):
    lines = get_input_lines(FILE_NUM, SUBFOLDER if is_sample else None)
    rows = [list(row) for row in lines]

    while check_has_changed(deepcopy(rows), rows, seats_callback, taken_tolerance):
        pass  # wait.. that's illegal!

    count_seats = sum([row.count(OCCUPIED_SEAT) for row in rows])

    print('\n'.join([' '.join(row) for row in rows]))

    return count_seats


def find_all_direction_neighbors(row_index, seat_index, rows):
    x_length = len(rows[0])
    y_length = len(rows)
    direction_pending = [True] * 8
    neighbour_count = 0
    diff = 1

    while direction_pending.count(True) > 0:
        for index, coord_gen in list(compress(enumerate(coord_gens), direction_pending)):
            x, y = coord_gen(row_index, seat_index, diff)
            has_valid_coordinates = 0 <= x < x_length and 0 <= y < y_length

            if has_valid_coordinates:
                seat = rows[x][y]

                if seat != FLOOR:
                    neighbour_count += seat == OCCUPIED_SEAT
                    direction_pending[index] = False
            else:
                direction_pending[index] = False
                continue

        diff += 1

    return neighbour_count


def solve2(is_sample=False):
    return solve1(is_sample, find_all_direction_neighbors, 5)


if __name__ == '__main__':
    exec_func(lambda: solve1(True), 37)
    exec_func(solve1, 2427)
    exec_func(lambda: solve2(True), 26)
    exec_func(solve2, 2199)
