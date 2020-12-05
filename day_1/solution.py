#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/1

def ingest_report(filename):
    input_set = []
    with open(filename) as f:
        for line in f:
            entry = int(line) 
            input_set.append(entry)
    return input_set

def find_2_sum_to_k(input_set, k):
    diff_hash = {}
    for item in input_set:
        key = k - item
        diff_hash[key] = item
        if item in diff_hash:
            return item, diff_hash[item]

    print(diff_hash)

def find_3_sum_to_k(input_set, k):
    diff_hash = {}
    for item in input_set:
        leftover = k - item
        diff_hash[leftover] = item
        for last_num in input_set:
            if leftover - last_num in input_set: 
                return item, leftover - last_num, last_num


if __name__ == "__main__":
    input_set = ingest_report('day_1/expense_report.txt')
    x, y = find_2_sum_to_k(input_set, 2020)
    print("Part 1: ", x * y)
    x, y, z = find_3_sum_to_k(input_set, 2020)
    print("Part 2: ", x * y * z)