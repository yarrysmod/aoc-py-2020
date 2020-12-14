from math import prod
from typing import List

from challenges._template import SAMPLES_FOLDER
from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]
OUT_OF_ORDER_BUS = 'x'


def solve1(is_sample=False):
    lines = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None))
    depart_time = int(lines[0])
    bus_lines = [int(bus) for bus in lines[1].split(',') if bus != OUT_OF_ORDER_BUS]
    least_wait: int = max(bus_lines)
    best_bus_line = None

    for bus_line in bus_lines:
        current_wait = bus_line - depart_time % bus_line

        if least_wait > current_wait:
            least_wait = current_wait
            best_bus_line = bus_line

    return least_wait * best_bus_line


def get_bus_lines_with_details(is_sample=False):
    _, bus_input = list(get_input_lines(FILE_NUM, SAMPLES_FOLDER if is_sample else None))
    bus_lines: List[str] = bus_input.split(',')[::-1]
    buses = []
    difference = 0

    for bus in bus_lines:
        if bus != OUT_OF_ORDER_BUS:
            bus_line = int(bus)
            buses.append([bus_line, difference % bus_line])

        difference += 1

    return buses


def get_common_point(buses, calculations):
    bus_values = list(map(lambda x: x[0], buses))
    diff_to_first_bus = buses[-1][1]
    max_prod = prod(bus_values)

    for bus_index in range(len(buses)):
        bus, bus_difference = buses[bus_index]

        remainder = calculations[bus_index] % bus
        addition = remainder
        multiplicand = 1

        while addition % bus != bus_difference:
            multiplicand += 1
            addition = remainder * multiplicand

        calculations[bus_index] *= multiplicand

    pos_latest_bus = sum([calc % max_prod for calc in calculations]) % max_prod

    return pos_latest_bus - diff_to_first_bus


def solve2(is_sample=False):
    buses = get_bus_lines_with_details(is_sample)
    calculations = [1] * len(buses)

    for current_bus_index in range(len(buses)):
        current_bus, _ = buses[current_bus_index]

        for nested_bus_index in range(len(buses)):
            if current_bus_index == nested_bus_index:
                continue
            else:
                calculations[nested_bus_index] *= current_bus

    return get_common_point(buses, calculations)



if __name__ == '__main__':
    exec_func(lambda: solve1(True), 295)
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
