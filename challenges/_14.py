from typing import List

from common import exec_func, get_input_lines_stream

FILE_NUM = __file__[-5:-3]
SAMPLES_FOLDER = 'samples'

NO_CHANGE_VALUE = 'X'


def get_mems(values: List[str]):
    mems: List[List[int]] = []

    for value in values:
        mem_part, value = value.split('] = ')
        _, address = mem_part.split('mem[')

        mems.append([int(address), int(value)])

    return mems


def solve1(is_sample=False):
    lines = get_input_lines_stream(FILE_NUM, SAMPLES_FOLDER if is_sample else None).read()
    values = [line.rstrip().split('\n') for line in lines.split('mask = ')[1:]]
    value_memory = {}

    for value in values:
        change_bits = [change for change in enumerate(value[0][::-1]) if change[1] != NO_CHANGE_VALUE]
        min_mem_length = change_bits[-1][0] + 1
        mems = get_mems(value[1:])

        for mem_reg, mem_value in mems:
            bin_num_reversed = list(bin(mem_value)[2:].zfill(min_mem_length))[::-1]

            for change_reg, change_val in change_bits:
                digit = bin_num_reversed[change_reg]

                if digit != change_val:
                    bin_num_reversed[change_reg] = str(1 - int(digit))

            value_memory[mem_reg] = int(''.join(bin_num_reversed[::-1]), 2)

    return sum([int(val) for val in value_memory.values()])


def solve2(is_sample=False):
    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    # exec_func(lambda: solve2(True))
    # exec_func(solve2)
