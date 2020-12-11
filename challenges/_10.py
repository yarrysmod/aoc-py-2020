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


def solve2():
    adapters = [0] + sorted(map(int, get_input_lines(FILE_NUM)))
    possible_edges = [1] + ([0] * (max(adapters)))
    edges_count = len(possible_edges)

    for edge_index in range(edges_count):
        # skip the edge if it's not in the adapters
        if edge_index not in adapters:
            continue

        reachable_edges = []

        for previous_index in range(edge_index - 3, edge_index):
            if previous_index >= 0:
                reachable_edges.append(possible_edges[previous_index])

        possible_edges[edge_index] += sum(reachable_edges)

    return possible_edges[-1]


if __name__ == '__main__':
    exec_func(solve1, 2760)
    exec_func(solve2, 13816758796288)
