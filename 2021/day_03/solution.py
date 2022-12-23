#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2021/day/3

import math

def ingest_report(filename):
    input_list = []
    with open(filename) as f:
        for line in f:
            input_list.append(int(line, 2))
    return input_list

def get_gamma_epsilon_product(input_list):
    #mask = 2048
    mask = 16
    gamma = 0
    epsilon = 0
    while mask > 0:
        local_sum = 0
        for num in input_list: 
            if num & mask:
                local_sum += 1
        if round(local_sum/len(input_list)):
            gamma += mask
        else:
            epsilon += mask
        mask >>= 1
    return gamma * epsilon

def get_life_support_rating(input_list):
    return get_oxygen_rating(input_list) * get_co2_rating(input_list)

def get_oxygen_rating(input_list):
    mask = 2048
    oxygen_rating = 0
    co2_rating = 0
    flip = 0
    #for i in range(6):
    while len(input_list) > 1:
        local_sum = 0
        for num in input_list:
            #print(f"num: {bin(mask)} {bin(num)}")
            if num & mask:
                local_sum += 1
        print(f"{local_sum} {len(input_list)}")
        if local_sum / len(input_list) >= 0.5 :
            print(round((local_sum/len(input_list))))
            print("in one")
            input_list = [num for num in input_list if num & mask]
            print(input_list)
        else:
            print('not in zero')
            input_list = [num for num in input_list if not (num & mask)]
        print("---")
        mask >>= 1
    [result] = input_list
    return result

def get_co2_rating(input_list):
    mask = 2048
    oxygen_rating = 0
    co2_rating = 0
    flip = 0
    #for i in range(6):
    while len(input_list) > 1:
        local_sum = 0
        for num in input_list:
            #print(f"num: {bin(mask)} {bin(num)}")
            if num & mask:
                local_sum += 1
        print(f"{local_sum} {len(input_list)}")
        if (local_sum / len(input_list)) >= 0.5 :
            print(round((local_sum/len(input_list))))
            print("in one")
            input_list = [num for num in input_list if not (num & mask)]
            
            print(input_list)
        else:
            print('not in zero')
            input_list = [num for num in input_list if num & mask]
        print("---")
        mask >>= 1
    [result] = input_list
    return result


if __name__ == "__main__":
    input_list = ingest_report('input.txt')
    product_p1 = get_gamma_epsilon_product(input_list)
    print(f"Part 1: {product_p1}")
    product_p2 = get_life_support_rating(input_list)
    print(f"Part 2: {product_p2}")