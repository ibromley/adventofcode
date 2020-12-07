#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/4

import re

def simple_validations(filename):
    count = 0
    with open(filename) as f:
        data = f.read()
        record_list = data.split('\n\n')
        for record in record_list:
            req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            field_pairs = re.split('\s', record)
            keys = [field.split(':')[0] for field in field_pairs]
            missing_fields = [req_field for req_field in req_fields if req_field not in keys]
            if len(missing_fields) == 0:
                count += 1
    return count

def strict_validations(filename):
    count = 0
    with open(filename) as f:
        data = f.read()
        record_list = data.split('\n\n')
        for record in record_list:
            req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            field_pairs = re.split('\s', record)
            pairs_split = [field.split(':') for field in field_pairs]
            key_value = {key: value for key, value in pairs_split}
            results = re.search('(\d+)(in|cm)', key_value.get('hgt', ''))
            height, unit = results.groups() if results else (0, 0)
            if (
                (1920 <= int(key_value.get('byr', 0)) <= 2002) and
                (2010 <= int(key_value.get('iyr', 0)) <= 2020) and
                (2020 <= int(key_value.get('eyr', 0)) <= 2030) and
                ((unit == 'in' and 59 <= int(height) <= 76) or 
                (unit == 'cm' and 150 <= int(height) <= 193)) and
                (re.search('^#[0-9a-f]{6}$', key_value.get('hcl', ''))) and
                (key_value.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
                (re.search('^\d{9}$', key_value.get('pid', ''))) and
                (all(key in key_value.keys() for key in req_fields))
            ):
                count+=1
    return count

if __name__ == "__main__":
    valid_passports = simple_validations('day_4/passport_data.txt')
    print('Part 1: ', valid_passports)
    valid_passports = strict_validations('day_4/passport_data.txt')
    print('Part 2: ', valid_passports)
