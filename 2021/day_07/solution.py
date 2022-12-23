#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/7


def ingest_positions(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(',')]

def part_1_fuel(h_posts):
    min_fuel = max(h_posts) * len(h_posts)
    for curr_pos in range(max(h_posts)):
        fuel = sum([abs(p - curr_pos) for p in h_posts])
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

def part_2_fuel(h_posts):
    min_fuel = max(h_posts) ** max(h_posts)
    for curr_pos in range(max(h_posts)):
        fuel = [abs(p - curr_pos) for p in h_posts]
        fuel_triangle = [round((n * (n + 1)) / 2) for n in fuel]
        if sum(fuel_triangle) < min_fuel:
            min_fuel = sum(fuel_triangle)
    return min_fuel 

if __name__ == "__main__":
    input_list = ingest_positions('input.txt')
    product_p1 = part_1_fuel(input_list)
    print(f"Part 1: {product_p1}")
    product_p2 = part_2_fuel(input_list)
    print(f"Part 2: {product_p2}")