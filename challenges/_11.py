from copy import deepcopy

from challenges._template import SAMPLES_FOLDER
from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]

FLOOR = '.'
FREE_SEAT = 'L'
OCCUPIED_SEAT = '#'


def find_all_immediate_neighbors(row_index, seat_index, rows):
    return find_all_neighbors(row_index, seat_index, rows, True)


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
    lines = get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None)
    rows = [list(row) for row in lines]

    while check_has_changed(deepcopy(rows), rows, seats_callback, taken_tolerance):
        pass  # wait.. that's illegal!

    count_seats = sum([row.count(OCCUPIED_SEAT) for row in rows])

    print('\n'.join([' '.join(row) for row in rows]))

    return count_seats


def find_all_neighbors(row_index, seat_index, rows, consider_floor=False):
    x_length = len(rows[0])
    y_length = len(rows)
    neighbour_count = 0

    for y_diff in [-1, 0, 1]:
        for x_diff in [-1, 0, 1]:
            # early abort if it's the same seat
            if x_diff == 0 and y_diff == 0:
                continue

            seat_y = row_index + y_diff
            seat_x = seat_index + x_diff

            # check until it either reaches either end
            while 0 <= seat_y < y_length and 0 <= seat_x < x_length:
                seat = rows[seat_y][seat_x]

                # skip checking the floor or do if it's part 1
                if seat != FLOOR or consider_floor:
                    neighbour_count += seat == OCCUPIED_SEAT
                    break

                seat_y = seat_y + y_diff
                seat_x = seat_x + x_diff

    return neighbour_count


def solve2(is_sample=False):
    return solve1(is_sample, find_all_neighbors, 5)


if __name__ == '__main__':
    exec_func(lambda: solve1(True), 37)
    exec_func(solve1, 2427)
    exec_func(lambda: solve2(True), 26)
    exec_func(solve2, 2199)
