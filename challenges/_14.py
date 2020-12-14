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


def get_converted_int(reverse_bin: List[str]):
    return int(''.join(reverse_bin[::-1]), 2)


def get_reversed_bin_list(num: int, fill_zeroes):
    return list(bin(num)[2:].zfill(fill_zeroes))[::-1]


def solve1(is_sample=False):
    lines = get_input_lines_stream(FILE_NUM, SAMPLES_FOLDER if is_sample else None).read()
    values = [line.rstrip().split('\n') for line in lines.split('mask = ')[1:]]
    value_memory = {}

    for value in values:
        change_bits = [change for change in enumerate(value[0][::-1]) if change[1] != NO_CHANGE_VALUE]
        min_mem_length = change_bits[-1][0] + 1
        mems = get_mems(value[1:])

        for mem_reg, mem_value in mems:
            bin_num_reversed = get_reversed_bin_list(mem_value, min_mem_length)

            for change_reg, change_val in change_bits:
                digit = bin_num_reversed[change_reg]

                if digit != change_val:
                    bin_num_reversed[change_reg] = str(1 - int(digit))

            value_memory[mem_reg] = get_converted_int(bin_num_reversed)

    return sum([int(val) for val in value_memory.values()])


def get_memory_regs(mem_reg, change_bits):
    bin_reg_reversed = get_reversed_bin_list(mem_reg, 0)
    swap_indexes = []
    magic_addresses = []

    for index in range(len(bin_reg_reversed)):
        change_bit = change_bits[index]

        if change_bit == '1':
            bin_reg_reversed[index] = '1'
        elif change_bit == NO_CHANGE_VALUE:
            swap_indexes.append(index)

    if len(swap_indexes) > 0:
        swap_pos_count = len(swap_indexes)
        for swap_value in range(2 ** swap_pos_count):
            swap_bin_list = get_reversed_bin_list(swap_value, swap_pos_count)

            for bin_index in range(len(swap_indexes)):
                swap_num = swap_bin_list[bin_index]
                swap_index = swap_indexes[bin_index]

                bin_reg_reversed[swap_index] = swap_num

            magic_addresses.append(get_converted_int(bin_reg_reversed))
    else:
        magic_addresses.append(get_converted_int(bin_reg_reversed))

    return magic_addresses


def solve2(is_sample=False):
    lines = get_input_lines_stream(FILE_NUM, SAMPLES_FOLDER if is_sample else None).read()
    values = [line.rstrip().split('\n') for line in lines.split('mask = ')[1:]]
    value_memory = {}

    for value in values:
        change_bits = value[0][::-1]
        mems = get_mems(value[1:])

        for mem_reg, mem_value in mems:
            for nested_mem_reg in get_memory_regs(mem_reg, change_bits):
                value_memory[nested_mem_reg] = mem_value

    return sum([int(val) for val in value_memory.values()])


if __name__ == '__main__':
    exec_func(lambda: solve1(True))
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
