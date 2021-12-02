class Submarine:
    def __init__(self):
        self.__depth = 0
        self.__horizontal = 0
        self.__aim = 0

    # Methods for the first part
    def change_depth(self, change): self.__depth += change

    def change_horizontal(self, change): self.__horizontal += change

    def change_aim(self, change): self.__aim += change

    # Methods for the second part
    def down(self, x): self.__aim += x

    def up(self, x): self.__aim -= x

    def forward(self, x):
        self.__horizontal += x
        self.__depth += self.__aim * x

    def task_return(self): return self.__depth * self.__horizontal


def day02_dive_part_1(submarine: Submarine, filename: str):
    with open(filename, 'r') as reader:
        for line in reader.readlines():
            try:
                command, value = line.split(' ')
            except ValueError:
                continue
            value = int(value)

            if command == 'forward':
                submarine.change_horizontal(value)
            elif command == 'down':
                submarine.change_depth(value)
            elif command == 'up':
                submarine.change_depth(-value)


def day02_dive_part_2(submarine: Submarine, filename: str):
    with open(filename, 'r') as reader:
        for line in reader.readlines():
            try:
                command, value = line.split(' ')
            except ValueError:
                continue
            value = int(value)

            if command == 'forward':
                submarine.forward(value)
            elif command == 'down':
                submarine.down(value)
            elif command == 'up':
                submarine.up(value)


if __name__ == '__main__':
    submarine1 = Submarine()
    day02_dive_part_1(submarine1, 'inputs/aoc-input-02.txt')
    print(submarine1.task_return())

    submarine2 = Submarine()
    day02_dive_part_2(submarine2, 'inputs/aoc-input-02.txt')
    print(submarine2.task_return())
