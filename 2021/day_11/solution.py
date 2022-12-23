#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/11

import copy

class Grid:

    def __init__(self, grid_array):
        self.grid = grid_array

    def __repr__(self):
        printout = ''
        for row in self.grid:
            printout += ' '.join(str(x) for x in row) + '\n'
        return printout

class Octopus:

    def __init__(self, energy):
        self.energy = energy
        self.has_flashed = False
        self.ready_to_flash = False

    def __repr__(self):
        return str(self.energy)

def ingest_energy_levels(filename):
    line_list = []
    with open(filename) as f:
        for line in f:
            num_line = []
            for oct in line.strip():
                num_line.append(Octopus(int(oct)))
            line_list.append(num_line)
    return Grid(line_list)

def get_adj_values(grid, x, y):
    adj_values = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (0 <= y + dy < len(grid.grid) 
            and 0 <= x + dx < len(grid.grid[0])
            and not(dy == 0 and dx == 0)):
                adj_values.append((y + dy, x + dx))
    print(f"({x},{y}) -> {adj_values}")
    return adj_values

def get_total_flashes(grid):
    new_grid = copy.deepcopy(grid)
    for y, y_line in enumerate(grid.grid):
        for x, val in enumerate(y_line):
            new_grid.grid[y][x].energy += 1
            if grid.grid[y][x].energy > 9 and not grid.grid[y][x].has_flashed:
                print(f"Flashing {x} , {y}")
                grid.grid[y][x].has_flashed = True 

                adj_coords = get_adj_values(grid, x, y)
                adj_flashes = [(x, y) for x, y in get_adj_values(grid, x, y) if grid.grid[y][x].energy >= 9]

                # understanding adj_flash = True
                # while adj_flashes:
                #    (adj_x, adj_y) = adj_coords.pop()
                #    if grid.grid[adj_y][adj_x].energy > 9:
                #        adj_coords.append(get_adj_values(grid, adj_x, adj_y))


    #return grid
    return new_grid 




if __name__ == "__main__":
    energy_grid = ingest_energy_levels('input_small.txt')
    print(energy_grid)
    for i in range(3):
        energy_grid = get_total_flashes(energy_grid)
        print(energy_grid)
    #print(f"Part 1: {product_p1}")
    #product_p2 = complete_lines(line_list)
    #print(f"Part 2: {product_p2}")
