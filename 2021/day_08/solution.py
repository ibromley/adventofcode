#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/8


def ingest_positions(filename):
    entries = []
    with open(filename) as f:
        for line in f:
            sig_pat, output = line.split('|')
            entries.append((sig_pat.split(), output.split()))
    return entries

def p1_seven_segment(input_list):
    sum_simple_nums = 0
    for entry in input_list:
        sig_pat, output = entry
        for val in output:
            if (len(val) == 2 or len(val) == 3 
                or len(val) == 4 or len(val) == 7):
                sum_simple_nums += 1
    return sum_simple_nums

def sort_func(e):
    return len(e)

def p2_seven_segment(input_list):
    sum = 0
    for entry in input_list:
        sig_pat, output = entry
        lookup = {}
        sig_pat.sort(key=sort_func)
        for pat in sig_pat:
            if len(pat) == 2: # 1
                lookup[1] = set(pat)
            elif len(pat) == 3: # 7
                lookup[7] = set(pat)
            elif len(pat) == 4: # 4
                lookup[4] = set(pat)
            elif len(pat) == 7: # 8
                lookup[8] = set(pat)
            elif len(pat) == 5: # 2,3,5
                if len(set(pat).intersection(lookup[4]).difference(lookup[1])) == 2: # 5
                    lookup[5] = set(pat)
                elif len(set(pat).intersection(lookup[7])) == 3: # 3
                    lookup[3] = set(pat)
                else: # 2
                    lookup[2] = set(pat)
            elif len(pat) == 6: # 0,6,9
                if len(set(pat).intersection(lookup[5].union(lookup[1]))) == 6: # 9
                    lookup[9] = set(pat)
                elif len(set(pat).intersection(lookup[2].difference(lookup[1]))) == 4: # 6
                    lookup[6] = set(pat)
                else: # 0
                    lookup[0] = set(pat)

        digits = ''
        for num in output:
            [x] = [k for k, v in lookup.items() if v == set(num)]
            digits += str(x)
        sum += int(digits)

    return sum

if __name__ == "__main__":
    input_list = ingest_positions('input.txt')
    product_p1 = p1_seven_segment(input_list)
    print(f"Part 1: {product_p1}")
    product_p2 = p2_seven_segment(input_list)
    print(f"Part 2: {product_p2}")
