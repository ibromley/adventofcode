#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/4


class BingoBoard:

    def __init__(self, grid):
        self.grid = grid
        self.has_won = False

    def __repr__(self):
        return str(self.grid)

    def mark(self, num):
        for r_i, row in enumerate(self.grid):
            for c_i, col in enumerate(row):
                if col == num:
                    self.grid[r_i][c_i] = 'x'

    def check_row_bingo(self):
        for row in self.grid:
            if all(num == row[0] for num in row):
                return True
    
    def check_col_bingo(self):
        for i in range(5):
            col_list = [row[i] for row in self.grid]
            if all(num == col_list[0] for num in col_list):
                return True

    def check_bingo(self):
        return self.check_row_bingo() or self.check_col_bingo()

    def get_score(self, last_num):
        num_list = [col for row in self.grid for col in row if type(col) == int]
        return sum(num_list) * last_num

def ingest_bingo(filename):
    input_list = []
    with open(filename) as f:
        num_list = [int(n) for n in f.readline().split(",")]
        print(num_list)
        all_boards = []
        for line in f:
            grid = []
            for row in range(5):
                bingo_row = [int(n) for n in f.readline().split()]
                grid.append(bingo_row)
            all_boards.append(grid)    
    return num_list, all_boards



if __name__ == "__main__":
    num_list, all_boards = ingest_bingo('input.txt')
    print(num_list)
    boards = [BingoBoard(grid) for grid in all_boards]
    print(boards)
    num_list_clone = num_list
    found_bingo = False
    while True not in [board.check_bingo() for board in boards]:
        print(f"num_list: {num_list}")
        num = num_list_clone.pop(0)
        for board in boards:
            board.mark(num)
            print(board)
            if board.check_bingo():
                print("found bingo")
                found_bingo = True
                print(board.get_score(num))
                break
    
    for num in num_list:
        for board in boards:
            if not board.has_won:
                board.mark(num)
                print(board)
                if board.check_bingo():
                    print("found bingo")
                    found_bingo = True
                    print(board.get_score(num))
                    board.has_won = True

    #print(f"Part 1: {product_p1}")
    #product_p2 = get_life_support_rating(input_list)
    #print(f"Part 2: {product_p2}")