#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/3

import re

def read_forest_map(filename):
    grid = [] 
    with open(filename) as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def trees_found_simple(grid):
    x = 0
    y = 0
    x_max = len(grid[0]) 
    y_max = len(grid) 
    trees_found = 0
    for y in range(y_max):
        location = grid[y % y_max][x % x_max]
        if location == '#':
            trees_found += 1 
        x+=3
    return trees_found

def trees_found_custom(grid, right, down):
    x = 0
    y = 0
    x_max = len(grid[0]) 
    y_max = len(grid)
    trees_found = 0
    for y in range(0, y_max, down):
        location = grid[y % y_max][x % x_max]
        if location == '#':
            trees_found += 1 
        x+=right
    return trees_found


if __name__ == "__main__":
    grid = read_forest_map('day_3/forest_map.txt')
    trees_found = trees_found_simple(grid)
    print("Part 1: ", trees_found)
    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    all_trees = [trees_found_custom(grid, path[0], path[1]) for path in paths]
    product = 1
    for tree_count in all_trees:
        product *= tree_count 
    print("Part 2: ", product)
