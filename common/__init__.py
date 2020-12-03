from typing import Iterator, Callable
import time


def get_input_lines(file_num: str) -> Iterator[str]:
    return filter(
        len, open(f'./resources/{file_num}-input.txt', 'r').read().split('\n'))


def exec_func(func: Callable):
    start_time = time.time()
    print(func())
    print(f"--- {time.time() - start_time} seconds ---")
