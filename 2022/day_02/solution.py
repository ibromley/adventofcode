#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/2

def part_one(filename):
    lookup = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    with open(filename) as f:
        for line in f:
            opponent, you = line.split()
            opponent = chr(ord(opponent) + (ord('X') - ord('A')))
            score += lookup[you]
            if opponent == you: # draw
                score += 3
            elif ((opponent == 'X' and you == 'Y') # win
                or (opponent == 'Y' and you == 'Z')
                or (opponent == 'Z' and you == 'X')):
                score += 6
    return score

def part_two(filename):
    lookup = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0
    with open(filename) as f:
        for line in f:
            opponent, status = line.split()
            score += lookup[status]
            if status == 'X': # lose
                score += (ord(opponent) - ord('A') - 1) % 3 + 1 
            elif status == 'Y': # draw
                score += (ord(opponent) - ord('A')) % 3 + 1
            elif status == 'Z': # win
                score += (ord(opponent) - ord('A') + 1) % 3 + 1
    return score

if __name__ == "__main__":
    score = part_one('input.txt')
    print(f"Part 1: {score}")
    score = part_two('input.txt')
    print(f"Part 2: {score}")