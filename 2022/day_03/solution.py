#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/3

def priority(letter):
    if letter.islower():
        priority = ord(letter) - ord('a') + 1
    else:
        priority = ord(letter) - ord('A') + 1 + 26
    return priority

def part_one(filename):
    sum_priority = 0
    with open(filename) as f:
        for line in f:
            left = set(c for c in line[:len(line) // 2].strip())
            right = set(c for c in line[len(line) // 2:].strip())
            common = left.intersection(right).pop()
            sum_priority += priority(common)   

    return sum_priority

def part_two(filename):
    sum_priority = 0
    with open(filename) as f:
        data = f.read().split("\n")
        for first, second, third in zip(data[0::3], data[1::3], data[2::3]):
            common = set(first).intersection(set(second)).intersection(set(third)).pop()
            sum_priority += priority(common)
    return sum_priority

if __name__ == "__main__":
    score = part_one('input.txt')
    print(f"Part 1: {score}")
    score = part_two('input.txt')
    print(f"Part 2: {score}")
