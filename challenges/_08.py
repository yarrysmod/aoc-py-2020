from common import exec_func, get_input_lines

FILE_NUM = __file__[-5:-3]

INST_TYPES = {
    'JUMP_TO_LINE': 'jmp',
    'ADD_TO_ACC': 'acc',
    'NO_OPERATION': 'nop'
}
OPPOSITE_INST = {
    INST_TYPES['JUMP_TO_LINE']: INST_TYPES['NO_OPERATION'],
    INST_TYPES['NO_OPERATION']: INST_TYPES['JUMP_TO_LINE']
}


def get_instructions():
    instructions = []
    jump_list = []

    for line in get_input_lines(FILE_NUM):
        instruction_type, val = line.split(' ')
        val = int(val)
        instruction_entry = [str(instruction_type), val]
        is_potential_jump = instruction_type in [INST_TYPES['JUMP_TO_LINE'], INST_TYPES['NO_OPERATION']]

        instructions.append(instruction_entry)

        index = len(instructions) - 1
        jump_list.append([index] + instruction_entry) if is_potential_jump else None

    return [instructions, jump_list]


def get_sum_with_detail(instructions):
    is_clean_execution = True
    accumulator = 0
    jumped_to = []
    index = 0

    while index < len(instructions):
        instruction, value = instructions[index]

        if index in jumped_to:
            is_clean_execution = False
            break

        jumped_to.append(index)

        if instruction == INST_TYPES['JUMP_TO_LINE']:
            index += value
        else:
            if instruction == INST_TYPES['ADD_TO_ACC']:
                accumulator += value

            index += 1

    return [accumulator, is_clean_execution]


def solve1():
    instructions, _ = get_instructions()
    accumulator, _ = get_sum_with_detail(instructions)

    return accumulator


def solve2():
    instructions, jump_list = get_instructions()

    for index, instruction, value in jump_list:
        instructions[index] = [OPPOSITE_INST[instruction], value]
        accumulator, is_clean_execution = get_sum_with_detail(instructions)

        if is_clean_execution:
            return accumulator

        instructions[index] = [instruction, value]

    raise Exception('could not make a clean execution to find the result.')


if __name__ == '__main__':
    exec_func(solve1, 1723)
    exec_func(solve2)
