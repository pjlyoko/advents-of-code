import numpy


class BingoBoard:
    def __init__(self, _board):
        self.__markings = numpy.zeros(shape=(5, 5), dtype=bool)
        self.__board = _board
        self.__last_called_number = None
        self.bingo = False
        self.score = None

    def mark_number_if_exists(self, number):
        if self.bingo:
            return
        self.__last_called_number = number
        for y in range(0, 5):
            for x in range(0, 5):
                if self.__board[y][x] == number:
                    self.__markings[y][x] = True
                    self.__check_bingo()

    def __check_bingo(self) -> bool:
        sums_by_column = numpy.sum(self.__markings, axis=0)
        for item in sums_by_column:
            if item == 5:
                self.bingo = True
                self.__calculate_score()
                return True

        sums_by_row = numpy.sum(self.__markings, axis=1)
        for item in sums_by_row:
            if item == 5:
                self.bingo = True
                self.__calculate_score()
                return True

        return False

    def __calculate_score(self):
        sum_of_unmarked = 0
        for y in range(0, 5):
            for x in range(0, 5):
                if not self.__markings[y][x]:
                    sum_of_unmarked += self.__board[y][x]

        self.score = sum_of_unmarked * self.__last_called_number


if __name__ == '__main__':
    bingo_boards: list[BingoBoard] = []

    with open('inputs/aoc-input-04.txt', 'r') as reader:
        drawn_numbers = [int(number) for number in reader.readline().strip().split(',')]
        line = reader.readline()
        board = None
        while line:
            line = line.strip()
            if line == '':
                if board is not None:
                    bingo_boards.append(BingoBoard(board))
                board = []
            else:
                board.append([int(number) for number in line.strip().split()])

            line = reader.readline()

    # HACK: Unfortunately, the last board is not included due to the code. Refactoring needed.
    bingo_boards.append(BingoBoard(board))
    winning_boards_indexes = []

    for drawn_number in drawn_numbers:
        results = []
        for board in bingo_boards:
            board.mark_number_if_exists(drawn_number)
            results.append(board.bingo)

        for (index, value) in enumerate(results):
            if value:
                if index not in winning_boards_indexes:
                    winning_boards_indexes.append(index)

    first_won = winning_boards_indexes[0]
    last_won = winning_boards_indexes[-1]
    print(f"First won: board #{first_won} with score of {bingo_boards[first_won].score}.")
    print(f"Last won: board #{last_won} with score of {bingo_boards[last_won].score}.")
