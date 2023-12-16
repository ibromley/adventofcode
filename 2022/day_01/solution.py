#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/1

def ingest_report(filename):
    input_list = []
    with open(filename) as f:
        all_file = f.read()
        groups =  [[int(y) for y in x.split("\n")] for x in all_file.split("\n\n")]
        sum_groups = [sum(group) for group in groups]
    return sum_groups

if __name__ == "__main__":
    groups = ingest_report('input.txt')
    print(f"Part 1: {max(groups)}")
    groups.sort()
    print(f"Part 2: {sum(groups[-3:])}")
