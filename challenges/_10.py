from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]


def get_diff_map():
    sorted_adapter_list = [0] + sorted(map(int, get_input_lines(FILE_NUM)))
    sorted_adapter_list += [sorted_adapter_list[-1] + 3]

    diff_map = {1: 0, 2: 0, 3: 0}
    latest_adapter = sorted_adapter_list[0]

    for adapter in sorted_adapter_list[1:]:
        diff_to_current = adapter - latest_adapter

        diff_map[diff_to_current] += 1
        latest_adapter = adapter

    return diff_map


def solve1():
    diff_map = get_diff_map()

    return diff_map[1] * diff_map[3]


def solve2():
    adapters = [0] + sorted(map(int, get_input_lines(FILE_NUM)))
    possible_edges = [1] + ([0] * (max(adapters)))

    for edge in adapters[1:]:
        reachable_edges = []

        for previous_index in range(edge - 3, edge):
            if previous_index >= 0:
                reachable_edges.append(possible_edges[previous_index])

        possible_edges[edge] = sum(reachable_edges)

    return possible_edges[-1]


if __name__ == '__main__':
    exec_func(solve1, 2760)
    exec_func(solve2, 13816758796288)
