#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/5
import re 

def setup(filename):
    with open(filename) as f:
        stacks, moves = f.read().split("\n\n")
        stacks = stacks.split("\n")[::-1]
        num_stacks = len(stacks.pop(0).split())
        indicies = [i * 4 + 1 for i in range(num_stacks)]
        config = [[stack[i] for stack in stacks if stack[i].isalpha()] for i in indicies]
        
        all_moves = []
        for move in moves.split("\n"):
            result = re.search(r"(\d+)\D+(\d+)\D+(\d+)", move)
            all_moves.append([int(val) for val in result.groups()])

    return config, all_moves

def part_one(config, moves):
    for amt, origin, dest in moves:
        for i in range(amt):
            config[dest - 1].append(config[origin - 1].pop())
    return ''.join([p[-1] for p in config])


def part_two(config, moves):
    for amt, origin, dest in moves:
        temp = []
        for i in range(amt):
            item = config[origin - 1].pop()
            temp.append(item)
        while temp:
            config[dest - 1].append(temp.pop())
    return ''.join([p[-1] for p in config])

if __name__ == "__main__":
    score = part_one(*setup('input.txt'))
    print(f"Part 1: {score}")
    score = part_two(*setup('input.txt'))
    print(f"Part 2: {score}")
