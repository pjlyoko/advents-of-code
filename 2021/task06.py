class Lanternfish:
    def __init__(self, internal_timer: int = 8):
        self.__internal_timer = internal_timer

    def next_day(self):
        self.__internal_timer -= 1
        if self.__internal_timer == -1:
            self.__internal_timer = 6
            return Lanternfish()

        return None


def part_1(lanternfish_list):
    for day in range(0, 80):
        new_lanternfishes = []
        for lanternfish in lanternfish_list:
            tmp = lanternfish.next_day()
            if tmp is not None:
                new_lanternfishes.append(tmp)

        if len(new_lanternfishes) > 0:
            for new_lanternfish in new_lanternfishes:
                lanternfish_list.append(new_lanternfish)

    print(len(lanternfish_list))


def part_2(lanternfish_list):
    number_of_lanternfishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for timer in lanternfish_list:
        number_of_lanternfishes[timer] += 1
    print(f"Initial state - {sum(number_of_lanternfishes[t] for t in number_of_lanternfishes)} fishes")

    for day in range(0, 256):
        resetting_lanternfishes = number_of_lanternfishes[0]

        number_of_lanternfishes[0] = number_of_lanternfishes[1]
        number_of_lanternfishes[1] = number_of_lanternfishes[2]
        number_of_lanternfishes[2] = number_of_lanternfishes[3]
        number_of_lanternfishes[3] = number_of_lanternfishes[4]
        number_of_lanternfishes[4] = number_of_lanternfishes[5]
        number_of_lanternfishes[5] = number_of_lanternfishes[6]
        number_of_lanternfishes[6] = number_of_lanternfishes[7]
        number_of_lanternfishes[7] = number_of_lanternfishes[8]

        number_of_lanternfishes[8] = resetting_lanternfishes
        number_of_lanternfishes[6] += resetting_lanternfishes
        print(f"Day {day} - {sum(number_of_lanternfishes[t] for t in number_of_lanternfishes)} fishes")

    print(sum(number_of_lanternfishes))


if __name__ == '__main__':
    with open('inputs/aoc-input-06.txt', 'r') as reader:
        initial_lanternfishes = reader.readline().split(',')
        initial_lanternfishes = [int(t) for t in initial_lanternfishes]

    lanternfish_list = [Lanternfish(internal_timer=t) for t in initial_lanternfishes]

    do_part_1 = False
    do_part_2 = True

    if do_part_1:
        part_1(lanternfish_list=lanternfish_list)

    if do_part_2:
        part_2(lanternfish_list=initial_lanternfishes)
