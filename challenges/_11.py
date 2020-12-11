from copy import deepcopy

from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SUBFOLDER = 'samples'

FLOOR = '.'
FREE_SEAT = 'L'
OCCUPIED_SEAT = '#'


def is_matching(list_a, list_b):
    for index in range(len(list_a)):
        if list_a[index] != list_b[index]:
            return False

    return True


def get_taken_seats(row_index, seat_index, rows):
    seats = []
    first_row = row_index - 1 if (row_index - 1) >= 0 else 0
    last_row = row_index + 2 if (row_index + 2) < len(rows) else len(rows)

    first_seat = seat_index - 1 if (seat_index - 1) >= 0 else 0
    last_seat = seat_index + 2 if (seat_index + 2) < len(rows[0]) else len(rows[0])

    for curr_row in range(first_row, last_row):
        for curr_seat in range(first_seat, last_seat):
            if curr_row == row_index and curr_seat == seat_index:
                continue
            seats.append(rows[curr_row][curr_seat])

    return [seat for seat in seats if seat == OCCUPIED_SEAT]


def change_rows(original_rows, rows):
    for row_index, row in enumerate(rows):
        for seat_index, seat in enumerate(row):
            if seat == FLOOR:
                continue

            occupied_neighbors = get_taken_seats(row_index, seat_index, original_rows).count(OCCUPIED_SEAT)

            if seat == FREE_SEAT and occupied_neighbors == 0:
                row[seat_index] = OCCUPIED_SEAT
            elif seat == OCCUPIED_SEAT and occupied_neighbors >= 4:
                row[seat_index] = FREE_SEAT

    return rows


def solve1(is_sample=False):
    lines = get_input_lines(FILE_NUM, SUBFOLDER if is_sample else None)
    rows = [list(row) for row in lines]
    original_rows = deepcopy(rows)

    while not is_matching(original_rows, change_rows(original_rows, rows)):
        original_rows = deepcopy(rows)

    pretty_print = '\n'.join([' '.join(row) for row in rows])
    count_seats = pretty_print.count(OCCUPIED_SEAT)

    return '\n' + pretty_print + f'\n{count_seats}'


def solve2():
    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(solve2)
