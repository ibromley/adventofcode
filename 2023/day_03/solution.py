#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2023/day/3

def part_1(filename):
    grid = [[col for col in rows.rstrip()] for rows in open(filename)]
    part_num_sum = 0
    curr_num = ""
    near_symbol = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isnumeric():
                curr_num += grid[row][col]
                if is_part_number(row, col, grid):
                    near_symbol = is_part_number(row, col, grid)
            else:
                if len(curr_num) > 0:
                    if near_symbol:
                        part_num_sum += int(curr_num)
                    curr_num = ""
                    near_symbol = False
    return part_num_sum


def is_part_number(row, col, grid):
    if ((row - 1 >= 0 and col - 1 >= 0 and grid[row - 1][col - 1] != '.' and not grid[row - 1][col - 1].isnumeric())
       or (row - 1 >= 0 and grid[row - 1][col] != '.' and not grid[row - 1][col].isnumeric())
       or (col - 1 >= 0 and grid[row][col - 1] != '.' and not grid[row][col - 1].isnumeric())
       or (row + 1 < len(grid) and col + 1 < len(grid[0]) and grid[row + 1][col + 1] != '.' and not grid[row + 1][col + 1].isnumeric())
       or (row + 1 < len(grid) and grid[row + 1][col] != '.' and not grid[row + 1][col].isnumeric())
       or (col + 1 < len(grid[0]) and grid[row][col + 1] != '.' and not grid[row][col + 1].isnumeric())
       or (row - 1 >= 0 and col + 1 < len(grid[0]) and grid[row - 1][col + 1] != '.' and not grid[row - 1][col + 1].isnumeric())
       or (row + 1 < len(grid)  and col - 1 >= 0 and grid[row + 1][col - 1] != '.' and not grid[row + 1][col - 1].isnumeric())):
        return True

def near_gear(row, col, grid):
    if row - 1 >= 0 and col - 1 >= 0 and grid[row - 1][col - 1] == '*':
        return row - 1, col - 1
    if row - 1 >= 0 and grid[row - 1][col] == '*':
        return row - 1, col
    if col - 1 >= 0 and grid[row][col - 1] == '*':
        return row, col - 1
    if row + 1 < len(grid) and col + 1 < len(grid[0]) and grid[row + 1][col + 1] == '*':
       return row + 1, col + 1
    if row + 1 < len(grid) and grid[row + 1][col] == '*':
       return row + 1, col
    if col + 1 < len(grid[0]) and grid[row][col + 1] == '*':
       return row, col + 1
    if row - 1 >= 0 and col + 1 < len(grid[0]) and grid[row - 1][col + 1] == '*':
       return row - 1, col + 1
    if row + 1 < len(grid)  and col - 1 >= 0 and grid[row + 1][col - 1] == '*':
        return row + 1, col - 1

def part_2(filename):
    grid = [[col for col in rows.rstrip()] for rows in open(filename)]
    part_num_sum = 0
    curr_num = ""
    near_symbol = False
    gear_loc = False
    gear_map = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isnumeric():
                curr_num += grid[row][col]
                if is_part_number(row, col, grid):
                    near_symbol = is_part_number(row, col, grid)
                if near_gear(row, col, grid):
                    gear_loc = near_gear(row, col, grid)
            else:
                if len(curr_num) > 0:
                    if near_symbol:
                        if gear_loc in gear_map:
                            part_num_sum += gear_map[gear_loc] * int(curr_num)
                            del gear_map[gear_loc]
                        else:
                            if gear_loc:
                                gear_map[gear_loc] = int(curr_num)
                    curr_num = ""
                    near_symbol = False
                    gear_loc = None
    return part_num_sum


if __name__ == "__main__":
    num_sum = part_1('input.txt')
    print(f"Part 1: {num_sum}")
    num_sum = part_2('input.txt')
    print(f"Part 2: {num_sum}")