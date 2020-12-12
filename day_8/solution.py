#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/8

import re

def parse_instruction_list(filename):
    instruction_list = []
    with open(filename) as f:
        for line in f:
            op, arg = line.split(' ')
            instruction_list.append((op, int(arg)))
    return instruction_list

def run_program(instruction_list):
    accumulator = 0
    pc = 0
    seen_instruction = []
    while pc not in seen_instruction:
        op, arg = instruction_list[pc] 
        seen_instruction.append(pc)
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            accumulator += arg 
            pc += 1
        elif op == 'jmp':
            pc += arg
    return accumulator

def fix_program(instruction_list):
    swap_locations = []
    found_end = False
    while not found_end: 
        accumulator = 0
        pc = 0
        made_swap = False
        seen_instruction = []
        while pc not in seen_instruction:
            if pc == len(instruction_list):
                found_end = True
                break
            op, arg = instruction_list[pc] 
            seen_instruction.append(pc)
            if (op in ['nop', 'jmp'] and not made_swap and pc not in swap_locations):
                made_swap = True
                swap_locations.append(pc)
                op = 'nop' if op == 'jmp' else 'jmp'
            if op == 'nop':
                pc += 1
            elif op == 'acc':
                accumulator += arg 
                pc += 1
            elif op == 'jmp':
                pc += arg
    return accumulator


if __name__ == "__main__":
    instruction_list = parse_instruction_list('day_8/instructions.txt')
    accumulator = run_program(instruction_list)
    print("Part 1: ", accumulator)
    accumulator = fix_program(instruction_list)
    print("Part 2: ", accumulator)
