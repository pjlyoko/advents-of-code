def day01_sonar_sweep_part_1():
    increases = 0
    previous = None
    with open('inputs/aoc-input-01.txt', 'r') as reader:
        for line in reader.readlines():
            cur_measurement = int(line)
            if previous is None:
                previous = cur_measurement
                continue
            if cur_measurement > previous:
                increases += 1
            previous = cur_measurement

    print(f"01-1: {increases}")


def day01_sonar_sweep_part_2():
    measurements = []
    measurements_sum = None
    increases = 0

    with open('inputs/aoc-input-01.txt', 'r') as reader:
        for line in reader.readlines():
            measurements.append(int(line))
            if len(measurements) < 3:
                continue
            elif len(measurements) == 3:
                measurements_sum = sum(measurements)
                continue
            del measurements[0]

            new_sum = sum(measurements)
            if new_sum > measurements_sum:
                increases += 1

            measurements_sum = new_sum

    print(f"01-2: {increases}")


if __name__ == '__main__':
    day01_sonar_sweep_part_1()
    day01_sonar_sweep_part_2()
