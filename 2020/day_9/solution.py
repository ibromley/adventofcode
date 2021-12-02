#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/9


def parse_data_recieved(filename):
    number_list = []
    with open(filename) as f:
        for line in f:
            number_list.append(int(line))        
    return number_list 

def check_validity(number_list, p_len):
    for i in range(p_len, len(number_list) - 1):
        target = number_list[i]
        preamble = number_list[i - p_len :i] 
        difference = [target - num for num in preamble]
        if len(set(preamble).intersection(difference)) < 2:
            return number_list[i]

def get_weakness(number_list, target):
    low = 0
    high = 1
    while not sum(number_list[low:high]) == target:
        if sum(number_list[low:high]) > target:
            low += 1
            high = low + 1
        high += 1
    return number_list[low:high]

if __name__ == "__main__":
    number_list = parse_data_recieved('day_9/receieved_data.txt')
    invalid_num = check_validity(number_list, 25)
    print("Part 1: ", invalid_num)
    contiguous_set = get_weakness(number_list, invalid_num)
    print("Part 2: ", (min(contiguous_set) + max(contiguous_set)))