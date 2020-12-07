from common import exec_func, get_input_lines_stream

FILE_NUM = '07'

LOOP_ABORT = 'no other bags.\n'


def get_rules() -> dict[str, list]:
    rules = {}

    with get_input_lines_stream(FILE_NUM) as file:
        for line in file:
            parent_bag, child_parts = line.split(' bags contain ')
            children = child_parts.split(', ')

            if parent_bag not in rules:
                rules[parent_bag] = []

            for child in children:
                if child == LOOP_ABORT:
                    continue

                quantity_delimiter = child.index(' ')
                name_delimiter = child.rindex(' ')
                quantity = int(child[:quantity_delimiter])
                child_bag = child[quantity_delimiter + 1:name_delimiter]

                rules[parent_bag].append([child_bag, quantity])

    return rules


def has_bag(rules: dict[str, list], hit_set: set, parent_bag: str, bag_to_find: str):
    bag_rules = rules[parent_bag]

    for child_bag, _ in bag_rules:
        is_hit = child_bag == bag_to_find
        has_hit = child_bag in hit_set

        if is_hit or has_hit or has_bag(rules, hit_set, child_bag, bag_to_find):
            hit_set.add(child_bag)
            return True

    return False


def bag_accumulator(rules: dict[str, list], parent_bag: str, is_main_bag=False):
    bag_rules = rules[parent_bag]
    bag_count = 0 if is_main_bag else 1

    for child_bag, quantity in bag_rules:
        bag_count += quantity * bag_accumulator(rules, child_bag)

    return bag_count


def solve1():
    rules = get_rules()
    hit_set = set()
    bag_to_find = 'shiny gold'
    bag_count = 0

    for parent_bag in [x for x in rules.keys() if x != bag_to_find]:
        if has_bag(rules, hit_set, parent_bag, bag_to_find):
            hit_set.add(parent_bag)
            bag_count += 1

    return bag_count


def solve2():
    rules = get_rules()
    bag_to_fill = 'shiny gold'

    return bag_accumulator(rules, bag_to_fill, True)


if __name__ == '__main__':
    exec_func(solve1, 259)
    exec_func(solve2, 45018)
