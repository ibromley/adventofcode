#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/2

import re

def count_instances_policy(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            lower, upper, letter, password = re.split('-|\s|:\s', line.strip())
            occurences = len([c for c in password if c == letter])
            if int(lower) <= occurences <= int(upper):
                count+=1
    return count

def check_positions_policy(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            p1, p2, letter, password = re.split('-|\s|:\s', line.strip())
            if ((password[int(p1) - 1] == letter) ^ # XOR operator
                (password[int(p2) - 1] == letter)):
                count += 1
    return count

if __name__ == "__main__":
    valid_passwords = count_instances_policy('day_2/policy_list.txt')
    print("Part 1: ", valid_passwords)
    valid_passwords = check_positions_policy('day_2/policy_list.txt')
    print("Part 2: ", valid_passwords)