#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2023/day/1
import re

def part_1(filename: str) -> int:
    sum = 0
    for line in open(filename):
        line_list = [int(c) for r in line for c in r if c.isnumeric()]
        line_num = line_list[0] * 10 + line_list[-1]
        sum += line_num
    return sum

def part_2(filename: str) -> int:
    sum = 0
    num_dict = {
        "zero": "z0o", "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", 
        "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"
    }
    for line in open(filename):
        for k,v in num_dict.items():
            line = re.sub(k,v, line)
        line_list = [int(c) for r in line for c in r if c.isnumeric()]
        line_num = line_list[0] * 10 + line_list[-1]
        sum += line_num
    return sum

if __name__ == "__main__":
    num_sum = part_1('input.txt')
    print(f"Part 1: {num_sum}")
    num_sum = part_2('input.txt')
    print(f"Part 2: {num_sum}")