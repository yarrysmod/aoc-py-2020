from typing import List

from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]

MAX_DIFF = 3


def get_diff_map():
    sorted_adapter_list = [0] + sorted(map(int, get_input_lines(FILE_NUM)))
    sorted_adapter_list += [sorted_adapter_list[-1] + 3]

    diff_map = {
        1: 0,
        2: 0,
        3: 0
    }
    latest_adapter = sorted_adapter_list[0]

    for index, adapter in enumerate(sorted_adapter_list[1:]):
        diff_to_current = adapter - latest_adapter
        next_adapter = sorted_adapter_list[index]

        if diff_to_current <= MAX_DIFF and (next_adapter - adapter) <= MAX_DIFF:
            diff_map[diff_to_current] += 1
            latest_adapter = adapter

    if latest_adapter == sorted_adapter_list[-1]:
        return diff_map
    else:
        raise Exception('did not find the correct adapter sequence.')


def solve1():
    diff_map = get_diff_map()

    return diff_map[1] * diff_map[3]


def get_removable_adapters(root_adapter, adapters):
    removable_adapters = []

    for index, adapter in enumerate(adapters[:-1]):
        next_adapter = adapters[index]
        following_adapter = adapters[index + 1]
        diff_to_next = next_adapter - root_adapter
        diff_to_following = following_adapter - root_adapter

        if diff_to_next > MAX_DIFF or diff_to_following > MAX_DIFF:
            break

        removable_adapters.append(adapter)

    return removable_adapters


def get_arrangement_count(removable_adapters, adapters: List[int]):
    arrangements_count = len(removable_adapters)

    for adapter in removable_adapters:
        reduced_adapters = list(adapters)
        reduced_adapters.remove(adapter)
        removable_adapters = get_removable_adapters(reduced_adapters[0], reduced_adapters[1:])

        if len(removable_adapters) > 0:
            arrangements_count += get_arrangement_count(removable_adapters, reduced_adapters)

    return arrangements_count


def solve2(): # TODO
    adapters = [0] + sorted(map(int, get_input_lines(FILE_NUM)))
    adapters_til_third_to_last = adapters[:-2]
    arrangements_count = 1

    for index, adapter in enumerate(adapters_til_third_to_last):
        next_adapter_index = index + 1
        adapters_after_current = adapters[next_adapter_index:-1]
        removable_adapters = get_removable_adapters(adapter, adapters_after_current)
        nested_arrangements = get_arrangement_count(removable_adapters, adapters_after_current)

        arrangements_count += nested_arrangements

    return arrangements_count


if __name__ == '__main__':
    exec_func(solve1, 2760)
    exec_func(solve2)
