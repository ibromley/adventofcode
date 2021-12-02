#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/1

def ingest_report(filename):
    input_list = []
    with open(filename) as f:
        for line in f:
            entry = int(line) 
            input_list.append(entry)
    return input_list

def increase_from_prev(input_list):
    num_increases = 0
    prev = input_list[0]
    for index, val in enumerate(input_list, 1):
        if val > prev:
            num_increases += 1
        prev = val
    return num_increases

def sliding_window_increases(input_list):
    num_increases = 0
    prev_sum = input_list[0] + input_list[1] + input_list[2]
    for i in range(1, len(input_list) - 2):
        sum = input_list[i] + input_list[i + 1] + input_list[i + 2]
        if sum > prev_sum:
            num_increases += 1
        prev_sum = sum
    return num_increases


if __name__ == "__main__":
    input_list = ingest_report('input.txt')
    num_increases_p1 = increase_from_prev(input_list)
    print(f"Part 1: {num_increases_p1}")
    num_increases_p2 = sliding_window_increases(input_list)
    print(f"Part 2: {num_increases_p2}")
