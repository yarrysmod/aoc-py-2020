from pathlib import Path
from typing import Iterator, Callable, TextIO
import time


def get_input_lines_stream(file_num: str, sub_folder=None, home_folder=None) -> TextIO:
    file_name = f"{file_num}-input.txt"
    sub_dir = f"{sub_folder}/" if sub_folder else ""
    res_dir = f'./{f"{home_folder}/" if home_folder else ""}resources/'

    resource_path = Path.joinpath(
        Path(__file__).parent.parent,
        f'{res_dir}{sub_dir}{file_name}'
    )

    return open(resource_path, 'r')


def get_input_lines(file_num: str, sub_folder=None, home_folder=None) -> Iterator[str]:
    return filter(lambda line: len(line) > 0,
                  get_input_lines_stream(file_num, sub_folder, home_folder).read().split('\n'))


def exec_func(func: Callable, assert_result=None):
    start_time = time.time()
    result = func()

    if assert_result:
        assert result == assert_result

    print(f'result: {result}')
    print(f"time: {time.time() - start_time} seconds")
