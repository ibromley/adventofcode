#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2022/day/7

class Node:
    def __init__(self, value, parent=None, size=0):
        self.value = value
        self.parent = parent
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, value):
        for child in self.children:
            if child.value == value:
                return child

    def __repr__(self):
        return f"{self.value} size={self.size} -> {[self.children]}\n"


def create_tree(filename):
    root = Node("/")
    with open(filename) as f:
        ptr = root
        for line in f:
            if line[0] == "$": # command
                cmd = line[2:4]
                if cmd == 'cd':
                    arg = line[5:].strip()
                    if arg == '/':
                        ptr = root
                    elif arg == '..':
                        ptr = ptr.parent
                    else:
                        ptr = ptr.find_child(arg)
            else: # info
                if line[:3] == 'dir': # directory
                    _, name = line.split()
                    size = 0
                else: # file
                    size, name = line.split()
                if ptr.find_child(name) is None:
                    ptr.add_child(Node(name, ptr, int(size)))
    print(root)
    calculate_dir_size(root, root.size)
    print(root)
    return root

def calculate_dir_size(node, total):
    if node.children is None:
        return node, node.size
    else:
        size_sum = sum([calculate_dir_size(n, total)[1] for n in node.children])
        node.size += size_sum
        return node, node.size


def part_one(node, total, target):
    if node.children is None:
        return node, total
    else:
        print(total, "---", node)
        total += node.size if node.size <= target else 0
        for n in node.children:
            total = part_one(n, total, target)[1]
        return node, total

def part_two(filename):
    pass

if __name__ == "__main__":
    root = create_tree('input_small.txt')
    score = part_one(root, 0, 100000)[1]
    print(f"Part 1: {score}")
    score = part_two('input.txt')
    print(f"Part 2: {score}")