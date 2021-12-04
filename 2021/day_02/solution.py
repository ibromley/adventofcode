#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/2

def ingest_report(filename):
    input_list = []
    with open(filename) as f:
        for line in f:
            dir, val = line.split(" ")
            input_list.append((dir, int(val)))
    return input_list

def get_final_dir_product(input_list):
    sum_pos = 0
    sum_depth = 0
    for direction, val in input_list:
        if direction == 'forward':
            sum_pos += val
        elif direction == 'up':
            sum_depth -= val
        elif direction == 'down':
            sum_depth += val
    return sum_pos * sum_depth 

def get_final_aim_product(input_list):
    sum_pos = 0
    sum_depth = 0
    sum_aim = 0
    for direction, val in input_list:
        if direction == 'forward':
            sum_pos += val
            sum_depth += val * sum_aim
        elif direction == 'up':
            sum_aim -= val
        elif direction == 'down':
            sum_aim += val
    return sum_pos * sum_depth 


if __name__ == "__main__":
    input_list = ingest_report('input.txt')
    product_p1 = get_final_dir_product(input_list)
    print(f"Part 1: {product_p1}")
    product_p2 = get_final_aim_product(input_list)
    print(f"Part 2: {product_p2}")