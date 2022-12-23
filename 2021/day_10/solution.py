#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/10

matching_braces = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def ingest_lines(filename):
    line_list = []
    with open(filename) as f:
        for line in f:
            line_list.append(line.strip())
    return line_list

def score_lines(line_list):
    point_values = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in line_list:
        print(f"line: {line}")
        line_stack = []
        for c in line:
            if c in matching_braces.keys():
                line_stack.append(matching_braces[c])
            else:
                last_char = line_stack.pop()
                if c != last_char:
                    print(f"error! Expected {last_char} got {c}")
                    score += point_values[c]
                    break
    return score

def complete_lines(line_list):
    point_values = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    all_scores = []
    for line in line_list:
        print(f"line: {line}")
        score = 0
        line_stack = []
        for c in line:
            if c in matching_braces.keys():
                line_stack.append(matching_braces[c])
            else:
                last_char = line_stack.pop()
                if c != last_char:
                    line_stack = []
                    break

        while line_stack:
            score *= 5
            score += point_values[line_stack.pop()]

        if score:
            all_scores.append(score)

        print(f"final score: {score}")

    all_scores.sort()
    return all_scores[len(all_scores) // 2]


if __name__ == "__main__":
    line_list = ingest_lines('input.txt')
    product_p1 = score_lines(line_list)
    print(f"Part 1: {product_p1}")
    product_p2 = complete_lines(line_list)
    print(f"Part 2: {product_p2}")