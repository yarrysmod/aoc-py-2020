from common import exec_func, get_input_lines_stream

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def get_boards(formatted_lines):
    return [
        [
            [
                [z, False] for z in y.split()
            ] for y in x.split('\n')
        ] for x in formatted_lines[1:]
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
        for cell in row:
            if cell[0] == value:  # exit condition
                cell[1] = True

                return True


def is_winning_sequence(sequence):
    return all(x[1] is True for x in sequence)


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

    # check the diagonals
    # diagonal_a = [board[x][x] for x in range(0, row_length)]
    # diagonal_b = [board[row_length - x][x - 1] for x in range(row_length, 0, -1)]
    #
    # return is_winning_sequence(diagonal_a) or is_winning_sequence(diagonal_b)


def get_unmarked(board):
    unmarked = []

    for row in board:
        for cell in row:
            if not cell[1]:
                unmarked.append(int(cell[0]))

    return unmarked


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
