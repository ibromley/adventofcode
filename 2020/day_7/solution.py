#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/7

import re

def generate_bag_rule_list(filename):
    container_dict = {}
    with open(filename) as f:
        for line in f:
            bag, contents = line.split('contain')
            bag = re.search('^(\w+\s\w+)', bag).groups(1)[0]
            adj_bag_list = {}
            for content in contents.split(','):
                sub_bag = re.search('(\d)\s(\w+\s\w+)', content)
                if sub_bag:
                    count, sub_bag = sub_bag.groups(0)
                    adj_bag_list[sub_bag] = int(count)
            container_dict[bag] = adj_bag_list
    return container_dict

def bfs_on_bag_rules(bag_rules, current_bag):
    visited = []
    queue = []
    visited.append(current_bag)
    queue.append(current_bag)
    while queue:
        current_bag = queue.pop()
        for rule, contained_bags in bag_rules.items():
            if current_bag in contained_bags and rule not in visited:
                visited.append(rule)
                queue.append(rule)
    return visited

def bfs_count_on_bag_rules(bag_rules, current_bag, count):
    queue = []
    queue.append((current_bag, count))
    sum_all_bags = count
    while queue:
        current_bag, count = queue.pop()
        for bag, sub_bag_count in bag_rules[current_bag].items():
            total_bags = count * sub_bag_count
            sum_all_bags += total_bags
            queue.append((bag, total_bags))
    return sum_all_bags

if __name__ == "__main__":
    bag_rules = generate_bag_rule_list('day_7/luggage_rules.txt')
    num_bags_contained =  bfs_on_bag_rules(bag_rules, 'shiny gold')
    print("Part 1: ", len(num_bags_contained) - 1)
    count_bags_contained = bfs_count_on_bag_rules(bag_rules, 'shiny gold', 1)
    print("Part 2: ", count_bags_contained - 1)
