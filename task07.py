# import numpy
import math

if __name__ == '__main__':
    with open('inputs/aoc-input-07.txt', 'r') as reader:
        positions = [int(x) for x in reader.readline().split(',')]

    # positions = numpy.array(positions)
    min_position = min(positions)
    max_position = max(positions)

    new_position = None
    fuel_spent = 99999999

    for test_postition in range(min_position, max_position + 1):
        rearangement_costs = [abs(test_postition - cur_pos) for cur_pos in positions]
        rearangement_costs_sum = sum(rearangement_costs)

        if rearangement_costs_sum < fuel_spent:
            fuel_spent = rearangement_costs_sum
            new_position = test_postition

    print(f"New position: {new_position}, fuel spent on rearangement: {fuel_spent}.")
