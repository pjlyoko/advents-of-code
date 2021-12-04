import numpy
from numpy import ndarray


def most_common_bit_at_position(report_data: ndarray, position: int, or_equal: bool = True) -> bool:
    sum_by_columns = numpy.sum(report_data, axis=0)
    number_of_reports = len(report_data)

    if or_equal:
        tmp = []

        for number_of_trues in sum_by_columns:
            number_of_falses = number_of_reports - number_of_trues
            tmp.append(True if number_of_trues >= number_of_falses else False)

        sum_by_columns = tmp
    else:
        sum_by_columns = [item > (number_of_reports // 2) for item in sum_by_columns]

    return sum_by_columns[position]


# TODO: These 2 functions... it should be possible to make them one (the code is actually duplicated)
def least_common_bit_at_position(report_data: ndarray, position: int, or_equal: bool = True) -> bool:
    sum_by_columns = numpy.sum(report_data, axis=0)
    number_of_reports = len(report_data)

    if or_equal:
        tmp = []
        # half_reports = number_of_reports // 2

        for number_of_trues in sum_by_columns:
            number_of_falses = number_of_reports - number_of_trues
            tmp.append(True if number_of_trues < number_of_falses else False)
        sum_by_columns = tmp
        # sum_by_columns = [item <= (number_of_reports // 2) for item in sum_by_columns]
    else:
        sum_by_columns = [item < (number_of_reports // 2) for item in sum_by_columns]

    return sum_by_columns[position]


def bits_to_number(bits_list: list) -> int:
    number = 0
    for i in range(0, len(bits_list)):
        power = len(bits_list) - i - 1
        if bits_list[i]:
            number += 2 ** power

    return number


def day_03_binary_diagnostics_part_1(report_data: ndarray) -> tuple[int, int]:
    number_of_reports = len(report_data)
    sum_by_columns = numpy.sum(report_data, axis=0)
    gamma_bits = [item > (number_of_reports // 2) for item in sum_by_columns]
    epsilon_bits = [not bit for bit in gamma_bits]

    gamma = bits_to_number(gamma_bits)
    epsilon = bits_to_number(epsilon_bits)

    return gamma, epsilon


def oxygen_generator(report_data: ndarray) -> list:
    copy_report_data = numpy.copy(report_data)
    for i in range(0, copy_report_data.shape[1]):
        most_common_bit = most_common_bit_at_position(copy_report_data, i)
        for j in range(copy_report_data.shape[0], 0, -1):
            jdx = j - 1
            if copy_report_data[jdx][i] != most_common_bit:
                copy_report_data = numpy.delete(copy_report_data, jdx, 0)
                if len(copy_report_data) == 1:
                    return copy_report_data[0]


def co2_scrubber(report_data: ndarray) -> list:
    copy_report_data = numpy.copy(report_data)
    for i in range(0, copy_report_data.shape[1]):
        least_common_bit = least_common_bit_at_position(copy_report_data, i)

        for j in range(copy_report_data.shape[0], 0, -1):
            jdx = j - 1
            if copy_report_data[jdx][i] != least_common_bit:
                copy_report_data = numpy.delete(copy_report_data, jdx, 0)
                if len(copy_report_data) == 1:
                    return copy_report_data[0]


def day_03_binary_diagnostics_part_2(report_data: ndarray) -> tuple[int, int]:
    oxygen_rating = bits_to_number(oxygen_generator(report_data))
    scrubber_rating = bits_to_number(co2_scrubber(report_data))

    return oxygen_rating, scrubber_rating


if __name__ == '__main__':
    with open('inputs/aoc-input-03.txt', 'r') as reader:
        report = [list(line.strip()) for line in reader.readlines()]
        reformatted_report = []
        for r in report:
            reformatted_report.append([x == '1' for x in r])
        reformatted_report = numpy.array(reformatted_report)
    gamma_rate, epsilon_rate = day_03_binary_diagnostics_part_1(reformatted_report)
    print(gamma_rate * epsilon_rate)

    oxygen_generator_rating, co2_scrubber_rating = day_03_binary_diagnostics_part_2(reformatted_report)
    print(oxygen_generator_rating * co2_scrubber_rating)
