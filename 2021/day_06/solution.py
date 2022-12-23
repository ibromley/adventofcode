#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/6


class Lanternfish:

    def __init__(self, timer):
        self.timer = timer
        self.new_fish = False

    def __repr__(self):
        return self.timer

    def day_passes(self):
        if self.timer == 0:
            self.timer = 6
            self.new_fish = True
        else:
            self.timer -= 1


class LaternfishSchool:
    
    def __init__(self, initial_timers):
        self.fishes = [Lanternfish(t) for t in initial_timers]
        self.day = 0

    def __repr__(self):
        return f"After {self.day} days: " + ','.join(str(f.timer) for f in self.fishes)

    def __len__(self):
        return len(self.fishes)

    def day_passes(self):
        for fish in self.fishes:
            fish.day_passes()
            if fish.new_fish:
                self.fishes.append(Lanternfish(9))
                fish.new_fish = False
        self.day += 1


class LaternfishSchoolOptimized:
    
    def __init__(self, initial_timers):
        self.fishes = [0 for i in range(9)]
        for timer in initial_timers:
            self.fishes[timer] += 1
        self.day = 0

    def __repr__(self):
        return f"After {self.day} days: " + ','.join(str(f) for f in self.fishes)

    def __len__(self):
        return sum(self.fishes)

    def day_passes(self):
        # fishes count down one by day
        reset = self.fishes.pop(0)
        self.fishes[6] += reset
        self.fishes.append(reset)
        print(self.fishes)
        self.day += 1

def ingest_state(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(',')]


if __name__ == "__main__":
    initial_state = ingest_state('input.txt')
    school = LaternfishSchool(initial_state)
    print(school)
    for i in range(80):
        school.day_passes()
        print(len(school))
        #print(school)
    print(len(school))

    school = LaternfishSchoolOptimized(initial_state)
    print(school)
    for i in range(256):
        school.day_passes()
        print(len(school))
    print(len(school))