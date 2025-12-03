# --- Day 2: Gift Shop ---

import math

def read_input(filepath):
    with open(filepath, 'r') as f:
        return f.readline()

def part_01(puzzle_input):
    invalid_ids_sum = 0

    id_ranges = puzzle_input.split(",")

    for id_range in id_ranges:
        bounds_list = id_range.split("-")
        low_bound = int(bounds_list[0])
        up_bound = int(bounds_list[1])

        for id in range(low_bound, up_bound + 1):
            int_len = get_integer_length(id)
            if int_len % 2 != 0:
                continue
            first_half = int(id / pow(10, int_len / 2))
            second_half = int(id % pow(10, int_len / 2))
            if first_half == second_half:
                invalid_ids_sum += id

    return invalid_ids_sum

def part_02(puzzle_input):
    invalid_ids_sum = 0
    id_ranges = puzzle_input.split(",")

    for id_range in id_ranges:
        bounds_list = id_range.split("-")
        low_bound = int(bounds_list[0])
        up_bound = int(bounds_list[1])

        for id in range(low_bound, up_bound + 1):
            int_len = get_integer_length(id)
            
            for rep_len in range(1, int(int_len / 2 + 1)):
                if int_len % rep_len != 0:
                    continue 

                buffer = 0
                counter = 0
                last_buffer = -1
                valid = True
                
                for n in range(int_len, 0, -1):
                    digit = get_nth_digit(id, n) 
                    buffer = buffer * 10 + digit
                    counter += 1
                    if counter >= rep_len:
                        if last_buffer != buffer and last_buffer != -1:
                            valid = False
                            break
                        last_buffer = buffer
                        buffer = 0
                        counter = 0
                if valid:
                    invalid_ids_sum += id
                    break 

    return invalid_ids_sum

def get_nth_digit(integer,n):
    return int(integer / (pow(10 , n - 1)) % 10)

def get_integer_length(integer):
    if integer == 0:
        return 1
    return int(math.log10(abs(integer))) + 1

def main():
    puzzle_input = read_input("day_02/input.txt")
    print(f"Part One: {part_01(puzzle_input)}")
    print(f"Part Two: {part_02(puzzle_input)}")

if __name__ == "__main__":
    main()
