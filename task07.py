from tqdm import tqdm


def calculate_fuel_spent(begin_pos, end_pos):
    if begin_pos == end_pos:
        return 0

    if begin_pos > end_pos:
        begin_pos, end_pos = end_pos, begin_pos

    distance = end_pos - begin_pos
    # 1, 2, ..., distance
    return (1 + distance) / 2 * distance


def part_one(positions_list):
    min_position = min(positions_list)
    max_position = max(positions_list)

    new_position = None
    fuel_spent = None

    for test_postition in tqdm(range(min_position, max_position + 1), leave=True):
        rearangement_costs = [abs(test_postition - cur_pos) for cur_pos in positions_list]
        rearangement_costs_sum = sum(rearangement_costs)

        if fuel_spent is None or rearangement_costs_sum < fuel_spent:
            fuel_spent = rearangement_costs_sum
            new_position = test_postition

    return new_position, fuel_spent


def part_two(positions_list):
    min_position = min(positions_list)
    max_position = max(positions_list)

    new_position = None
    fuel_spent = None

    for test_postition in tqdm(range(min_position, max_position + 1), leave=True):
        rearangement_costs = [calculate_fuel_spent(cur_pos, test_postition) for cur_pos in positions_list]
        rearangement_costs_sum = sum(rearangement_costs)

        if fuel_spent is None or rearangement_costs_sum < fuel_spent:
            fuel_spent = rearangement_costs_sum
            new_position = test_postition

    return new_position, fuel_spent


if __name__ == '__main__':
    with open('inputs/aoc-input-07.txt', 'r') as reader:
        positions = [int(x) for x in reader.readline().split(',')]

    pos, fuel = part_one(positions)
    print(f"Part one. new position: {pos}, fuel spent on rearangement: {fuel}.")

    pos, fuel = part_two(positions)
    print(f"Part two. new position: {pos}, fuel spent on rearangement: {fuel}.")
