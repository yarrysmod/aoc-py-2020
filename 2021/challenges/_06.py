from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'
HOME_DIR = '2021'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    fishes = [int(x) for x in lines[0].split(',')]

    for step in range(80):
        fish_count = range(len(fishes))

        for fish_index in fish_count:
            fishes[fish_index] -= 1

            if fishes[fish_index] < 0:
                fishes[fish_index] = 6
                fishes.append(8)

    return len(fishes)


def solve2(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None, HOME_DIR))
    fishes = [int(x) for x in lines[0].split(',')]
    fish_counts = get_fish_counts(fishes)
    pending_new_fish = 0

    for step in range(256):
        for count_index in range(len(fish_counts)):
            if count_index == 0:
                pending_new_fish = fish_counts[count_index]
            else:
                fish_counts[count_index - 1] = fish_counts[count_index]

            fish_counts[count_index] = 0

        # moving the old fish and new fish to their new positions
        if pending_new_fish:
            fish_counts[6] += pending_new_fish
            fish_counts[8] += pending_new_fish
            pending_new_fish = 0

    return sum(fish_counts)


def get_fish_counts(fishes):
    fish_list = [0] * 9

    for fish in fishes:
        fish_list[fish] += 1

    return fish_list


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
