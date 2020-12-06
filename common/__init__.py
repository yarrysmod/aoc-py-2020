from typing import Iterator, Callable, TextIO
import time


def get_input_lines(file_num: str) -> Iterator[str]:
    return filter(
        len, open(f'./resources/{file_num}-input.txt', 'r').read().split('\n'))


def get_input_lines_stream(file_num: str) -> TextIO:
    return open(f'./resources/{file_num}-input.txt', 'r')


def exec_func(func: Callable, assert_result=None):
    start_time = time.time()
    result = func()

    if assert_result:
        assert result == assert_result

    print(f'result: {result}')
    print(f"time: {time.time() - start_time} seconds")
