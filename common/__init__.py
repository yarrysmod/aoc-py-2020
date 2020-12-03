from typing import Iterator, Callable, TextIO
import time


def get_input_lines(file_num: str) -> Iterator[str]:
    return filter(
        len, open(f'./resources/{file_num}-input.txt', 'r').read().split('\n'))


def get_input_lines_stream(file_num: str) -> TextIO:
    return open(f'./resources/{file_num}-input.txt', 'r')


def exec_func(func: Callable):
    start_time = time.time()
    print(f'result: {func()}')
    print(f"time: {time.time() - start_time} seconds")
