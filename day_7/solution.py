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
            adj_bag_list = []
            for content in contents.split(','):
                sub_bag = re.search('\d\s(\w+\s\w+)', content)
                if sub_bag:
                    sub_bag = sub_bag.groups(1)[0]
                    adj_bag_list.append(sub_bag)
            container_dict[bag] = adj_bag_list
    return container_dict

def bfs_on_bag_rules(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        current_bag = queue.pop()
        for rule in bag_rules:
            if current_bag in bag_rules[rule] and rule not in visited:
                visited.append(rule)
                queue.append(rule)
    return visited


if __name__ == "__main__":
    bag_rules = generate_bag_rule_list('day_7/luggage_rules.txt')
    num_bags_contained =  bfs_on_bag_rules(bag_rules, 'shiny gold')
    print("Part 1: ", len(num_bags_contained) - 1)