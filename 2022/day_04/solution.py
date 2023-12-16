#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/4

def part_one(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            first, second = line.split(",")
            first = [int(x) for x in first.split('-')]
            second = [int(x) for x in second.split('-')]
            if ((first[0] <= second[0] and second[1] <= first[1])
                or (second[0] <= first[0] and first[1] <= second[1])):
                count += 1
    return count

def part_two(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            first, second = line.split(",")
            first = [int(x) for x in first.split('-')]
            second = [int(x) for x in second.split('-')]
            if ((first[1] >= second[0] and first[0] <= second[1])
                or (second[1] >= first[0] and second[0] <= first[1])):
                count += 1
    return count

if __name__ == "__main__":
    score = part_one('input.txt')
    print(f"Part 1: {score}")
    score = part_two('input.txt')
    print(f"Part 2: {score}")
