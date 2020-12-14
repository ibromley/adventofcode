#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/10


def parse_adapter_ratings(filename):
    rating_list = []
    with open(filename) as f:
        for line in f:
            rating_list.append(int(line))        
    return rating_list 

def find_joltage_diffs(ratings):
    ratings.append(max(ratings) + 3)
    curr_adapter = 0
    dist = {1 : 0, 2 : 0, 3 : 0}
    while ratings: 
        valid = [pos for pos in ratings if pos <= curr_adapter + 3]
        chosen = min(valid)
        dist[chosen - curr_adapter] +=1
        curr_adapter = ratings.pop(0)
    return dist

def find_joltage_paths(ratings):
    ratings.insert(0, 0)
    paths = {} 
    paths[0] = 1
    for rating in ratings: 
        for diff in range(1, 4):
            curr_rating = rating + diff
            if curr_rating in ratings:
                if paths.get(curr_rating):
                    paths[curr_rating] += paths[rating]
                else:
                    paths[curr_rating] = paths[rating]
    return paths


if __name__ == "__main__":
    ratings = parse_adapter_ratings('day_10/adapter_ratings.txt')
    dist = find_joltage_diffs(sorted(ratings))
    print("Part 1: ", (dist[1] * dist[3]))
    paths = find_joltage_paths(sorted(ratings))
    print("Part 2: ", max(paths.values()))
