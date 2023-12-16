#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2023/day/2
import re

def part_1(filename):
    all_game_ids = 0
    possible = {"red": 12, "green": 13, "blue": 14}
    for line in open(filename):
        impossible = False
        game_id = int(re.search("(?<=Game\W)\d+", line).group(0))
        draws = line.strip().split(": ")[1].split("; ")
        for draw in draws:
            for single in draw.split(", "):
                count, color = single.split()
                if int(count) > possible[color]:
                    impossible = True
        all_game_ids += game_id if not impossible else 0
    return all_game_ids

def part_2(filename):
    sum_powers = 0
    for line in open(filename):
        game_id = int(re.search("(?<=Game\W)\d+", line).group(0))
        draws = line.strip().split(": ")[1].split("; ")
        color_counts = {"red": 0, "green": 0, "blue": 0}
        for draw in draws:
            for single in draw.split(", "):
                count, color = single.split()
                if int(count) > color_counts[color]:
                    color_counts[color] = int(count)
        multiple = 1
        for c in color_counts.values():
            multiple *= c
        sum_powers += multiple    
    return sum_powers

if __name__ == "__main__":
    num_sum = part_1('input.txt')
    print(f"Part 1: {num_sum}")
    num_sum = part_2('input.txt')
    print(f"Part 2: {num_sum}")