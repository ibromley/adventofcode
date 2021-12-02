#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/5


def get_seat_locations(filename):
    seat_locations = []
    with open(filename) as f:
        for line in f:
            row_low, row_high = 0, 127
            col_low, col_high = 0, 7
            for dir_char in line:
                row_mid = row_low + (row_high - row_low) // 2
                col_mid = col_low + (col_high - col_low) // 2
                if dir_char == 'F':
                    row_high = row_mid 
                elif dir_char == 'B':
                    row_low = row_mid + 1
                elif dir_char == 'R':
                    col_low= col_mid + 1
                elif dir_char == 'L':
                    col_high = col_mid
            seat_id = row_low * 8 + col_low
            seat_locations.append({'row': row_low, 'col': col_low, 'seat_id': seat_id})
    return seat_locations

def print_seating_chart(seat_locations):
    seating_chart = [['X'] * 8 for i in range(128)]
    for seat in seat_locations:
        seating_chart[seat['row']][seat['col']] = '.' 
    for num, row in enumerate(seating_chart):
        print(f'{num:>3}', row)

def find_my_seat(seat_locations):
    id_list = [seat['seat_id'] for seat in seat_locations]
    total = (min(id_list) + max(id_list)) * (len(id_list) + 1) / 2
    return int(total) - sum(id_list) 
   
if __name__ == "__main__":
    seat_locations = get_seat_locations('day_5/boarding_pass_list.txt')
    print('Part 1: ', max(seat['seat_id'] for seat in seat_locations))
    print_seating_chart(seat_locations)
    my_seat_id = find_my_seat(seat_locations)
    print('Part 2: ', my_seat_id)
