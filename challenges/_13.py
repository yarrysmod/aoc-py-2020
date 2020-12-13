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


def solve2(is_sample=False):
    pass


if __name__ == '__main__':
    exec_func(lambda: solve1(True), 295)
    exec_func(solve1)
    exec_func(lambda: solve2(True))
    exec_func(solve2)
