#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/5

import re

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Line: ({self.x1},{self.y1}) -> ({self.x2},{self.y2})"

class Plot:

    def __init__(self, size):
        self.grid = [['.' for i in range(size)] for j in range(size)]

    def __repr__(self):
        printout = ''
        for row in self.grid:
            printout += ' '.join(str(x) for x in row) + '\n'
        return printout

    def plot_line(self, line):
        x = line.x1
        y = line.y1
        self.plot_point(x, y)
        while x != line.x2 or y != line.y2:
            if line.x2 > x:
                x +=1
            elif line.x2 < x:
                x -= 1
            if line.y2 > y:
                y += 1
            elif line.y2 < y:
                y -= 1
            self.plot_point(x, y)

    def plot_point(self, x, y):
        if self.grid[y][x] == '.':
            self.grid[y][x] = 1
        else:
            self.grid[y][x] += 1

    def find_intersections(self):
        xings = [x for row in self.grid for x in row if type(x) == int and x >= 2]
        return len(xings)

def ingest_lines(filename):
    line_list = []
    with open(filename) as f:
        for line in f:
            match = re.match(r'(\d+),(\d+)\W->\W(\d+),(\d+)', line)
            (x1, y1, x2, y2) = (int(val) for val in match.groups(0))
            line_list.append(Line(x1, y1, x2, y2))
    return line_list


if __name__ == "__main__":
    line_list = ingest_lines('input.txt')
    plot = Plot(1000)
    #h_v_lines = [l for l in line_list if l.x1 == l.x2 or l.y1 == l.y2]
    h_v_lines = line_list
    for line in h_v_lines:
        plot.plot_line(line)
    print(plot)
    print(plot.find_intersections())