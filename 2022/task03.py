def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    elif item.isupper():
        return ord(item) - ord('A') + 27


def analyze_line(items: str) -> int:
    items = items.strip()

    items_len = len(items)
    assert (items_len % 2 == 0)

    compartment_size = items_len // 2
    first_compartment = items[0: compartment_size]
    second_compartment = items[compartment_size:]

    common_items = []

    # There's no need to check items in both compartments, they have to be *common*
    for item in first_compartment:
        if item in second_compartment and item not in common_items:
            common_items.append(item)

    # I'm not sure if that's going to be true
    assert (len(common_items) <= 1)

    priorities = [priority(item) for item in common_items]

    return sum(priorities)


def analyze_3_lines(line1: str, line2: str, line3: str) -> int:
    common1 = []
    common = None

    for item in line1:
        if item in line2 and item not in common1:
            common1.append(item)

    assert (len(common1) > 0)

    for item in line3:
        if item in common1:
            common = item
            break

    assert (common is not None)

    return priority(common)


if __name__ == '__main__':
    sum_of_priorities = 0
    with open('inputs/aoc2022-input-03.txt', 'r') as f:
        line = f.readline()
        while line:
            sum_of_priorities += analyze_line(line)
            line = f.readline()

    print(f"{sum_of_priorities=}")

    sum_of_3elf_group_priorities = 0
    with open('inputs/aoc2022-input-03.txt', 'r') as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        line3 = f.readline().strip()

        while line1:
            sum_of_3elf_group_priorities += analyze_3_lines(line1, line2, line3)

            line1 = f.readline().strip()
            line2 = f.readline().strip()
            line3 = f.readline().strip()

    print(f"{sum_of_3elf_group_priorities=}")
