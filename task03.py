import numpy
from numpy import ndarray


def day03_binary_diagnostics_part_1(report_data: ndarray) -> tuple[int, int]:
    number_of_reports = len(report_data)
    sum_by_columns = numpy.sum(report_data, axis=0)
    gamma_bits = [item > (number_of_reports // 2) for item in sum_by_columns]
    epsilon_bits = [not bit for bit in gamma_bits]

    gamma = 0
    epsilon = 0
    for i in range(0, len(gamma_bits)):
        power = len(gamma_bits) - i - 1
        if gamma_bits[i]:
            gamma += 2 ** power
        if epsilon_bits[i]:
            epsilon += 2 ** power

    return gamma, epsilon


if __name__ == '__main__':
    with open('inputs/aoc-input-03.txt', 'r') as reader:
        report = [list(line.strip()) for line in reader.readlines()]
        reformatted_report = []
        for r in report:
            reformatted_report.append([x == '1' for x in r])
        reformatted_report = numpy.array(reformatted_report)
    gamma_rate, epsilon_rate = day03_binary_diagnostics_part_1(reformatted_report)
    print(gamma_rate * epsilon_rate)
