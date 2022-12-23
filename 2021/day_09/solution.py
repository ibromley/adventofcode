#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/9

def ingest_heights(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append([int(num) for num in line.strip()])
    return grid

def lowest_points(grid):
    x = 0
    y = 0
    lowest_points = []
    lowest_coords = []
    for y, y_row in enumerate(grid):
        for x, val in enumerate(y_row):
            adj_list = []
            check_left = x - 1
            check_right = x + 1
            check_up = y + 1
            check_down = y - 1
            if 0 <= check_left < len(grid[0]): 
                adj_list.append(grid[y][check_left])
            if 0 <= check_right < len(grid[0]):
                adj_list.append(grid[y][check_right])
            if 0 <= check_up < len(grid): 
                adj_list.append(grid[check_up][x])
            if 0 <= check_down < len(grid):
                adj_list.append(grid[check_down][x])

            is_lowest = [adj > val for adj in adj_list]
            
            if all(is_lowest):
                print(f"{adj_list} - {val} is the lowest")
                lowest_points.append(val)
                lowest_coords.append((x, y))

    return sum(lowest_points) + len(lowest_points), lowest_coords

def largest_basins(grid, lowest_coords):
    basin_sizes = []
    for coord in lowest_coords:
        x, y = coord
        find_terrain = [(x, y)]
        basin_coords = []
        while find_terrain:
            location = find_terrain.pop()

            if location not in basin_coords:
                basin_coords.append(location)

            new_locations = helper_check_adj(grid, location)
            for loc in new_locations:
                if loc not in basin_coords:
                    find_terrain.append(loc)

        basin_sizes.append(len(basin_coords))
    
    basin_sizes.sort()
    product = 1
    for size in basin_sizes[-3:]:
        product *= size
    return product


def helper_check_adj(grid, location):
    x, y = location
    adj_list = []
    check_left = x - 1
    check_right = x + 1
    check_up = y + 1
    check_down = y - 1
    if 0 <= check_left < len(grid[0]) and grid[y][check_left] != 9: 
        adj_list.append((check_left, y))
    if 0 <= check_right < len(grid[0]) and grid[y][check_right] != 9:
        adj_list.append((check_right, y))
    if 0 <= check_up < len(grid) and grid[check_up][x] != 9: 
        adj_list.append((x, check_up))
    if 0 <= check_down < len(grid) and grid[check_down][x] != 9:
        adj_list.append((x, check_down))

    return adj_list 

if __name__ == "__main__":
    grid = ingest_heights('input.txt')
    product_p1, lowest_coords = lowest_points(grid)
    print(f"Part 1: {product_p1}")
    product_p2 = largest_basins(grid, lowest_coords)
    print(f"Part 2: {product_p2}")