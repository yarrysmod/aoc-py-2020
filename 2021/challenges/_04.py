from common import exec_func, get_input_lines_stream

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'

DRAWN_DIGIT = '-1'


def get_boards(formatted_lines):
    return [
        [y.split() for y in x.split('\n')]
        for x in formatted_lines[1:]
    ]


def solve1(is_sample=False):
    lines = get_input_lines_stream(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR).read()
    formatted_lines = lines.split('\n\n')
    values = formatted_lines[0].split(',')
    boards = get_boards(formatted_lines)

    for value in values:
        for board in boards:
            if activate_board_value(value, board) and is_winner(board):
                unmarked_sum = sum(get_unmarked(board))

                return unmarked_sum * int(value)


def solve2(is_sample=False):
    lines = get_input_lines_stream(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR).read()
    formatted_lines = lines.split('\n\n')
    values = formatted_lines[0].split(',')
    boards = get_boards(formatted_lines)

    for value in values:
        for board_index in range(0, len(boards)):
            board = boards[board_index]

            if not board:
                continue

            if activate_board_value(value, board) and is_winner(board):
                boards[board_index] = None

                if all(board is None for board in boards):
                    unmarked_sum = sum(get_unmarked(board))

                    return unmarked_sum * int(value)


def activate_board_value(value, board):
    for row in board:
        for cell_index in range(0, len(row)):
            if row[cell_index] == value:  # exit condition
                row[cell_index] = DRAWN_DIGIT

                return True


def is_winning_sequence(sequence):
    return all(x is DRAWN_DIGIT for x in sequence)


def is_winner(board):
    row_length = len(board[0])

    # check horizontal
    for row in board:
        if is_winning_sequence(row):
            return True

    # check vertical
    for cell_index in range(0, row_length):
        column = [row[cell_index] for row in board]

        if is_winning_sequence(column):
            return True


def get_unmarked(board):
    unmarked = []

    for row in board:
        for cell in row:
            if cell is not DRAWN_DIGIT:
                unmarked.append(int(cell))

    return unmarked


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
