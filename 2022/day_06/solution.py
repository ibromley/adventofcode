#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/6
import re 

def part_one_and_two(filename, buffer_size):
    buffer = []
    counter = 0
    with open(filename) as f:
        stream = f.read()
        for i in range(len(stream)):
            if len(set(stream[i:i + buffer_size])) == buffer_size:
                return i + buffer_size


if __name__ == "__main__":
    score = part_one_and_two('input.txt', 4)
    print(f"Part 1: {score}")
    score = part_one_and_two('input.txt', 14)
    print(f"Part 2: {score}")
