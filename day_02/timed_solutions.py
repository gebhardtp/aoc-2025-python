# Seeing the bad performance of my original solution made me want to run a performance test.
# I was initially convinced that the pure mathematical approach (division, modulo, powers of 10) 
# would be faster than converting numbers to strings for slicing and comparison.
# Plot twist: The string operations turned out to be significantly faster! 
# This was a huge learning moment—it shows just how optimized Python's built-in string handling really is. 
# Sometimes the cleaner, more readable code is also the quicker code!

import math
import time

def read_input(filepath):
    with open(filepath, 'r') as f:
        return f.readline().strip()

def part_01_math(puzzle_input):
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

def part_01_string(puzzle_input):
    invalid_ids_sum = 0
    id_ranges = puzzle_input.split(",")

    for id_range in id_ranges:
        bounds_list = id_range.split("-")
        low_bound = int(bounds_list[0])
        up_bound = int(bounds_list[1])

        for id in range(low_bound, up_bound + 1):
            s_id = str(id)
            length = len(s_id)
            
            if length % 2 != 0:
                continue
                
            mid = length // 2
            if s_id[:mid] == s_id[mid:]:
                invalid_ids_sum += id

    return invalid_ids_sum

def part_02_math(puzzle_input):
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

def part_02_string(puzzle_input):
    invalid_ids_sum = 0
    id_ranges = puzzle_input.split(",")

    for id_range in id_ranges:
        bounds_list = id_range.split("-")
        low_bound = int(bounds_list[0])
        up_bound = int(bounds_list[1])

        for id in range(low_bound, up_bound + 1):
            s_id = str(id)
            length = len(s_id)
            
            for pattern_len in range(1, (length // 2) + 1):
                if length % pattern_len == 0:
                    pattern = s_id[:pattern_len]
                    repeats = length // pattern_len
                    
                    if pattern * repeats == s_id:
                        invalid_ids_sum += id
                        break
            
    return invalid_ids_sum

def get_nth_digit(integer, n):
    return int(integer / (pow(10 , n - 1)) % 10)

def get_integer_length(integer):
    if integer == 0:
        return 1
    return int(math.log10(abs(integer))) + 1

def measure_performance(func, input_data, name):
    start_time = time.perf_counter()
    result = func(input_data)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"[{name}] Result: {result} | Time: {elapsed:.5f} sec")

def main():
    
    puzzle_input = read_input("day_02/input.txt") 
    
    print("--- Part 1 Comparison ---")
    measure_performance(part_01_math, puzzle_input, "Math  ")
    measure_performance(part_01_string, puzzle_input, "String")
    
    print("\n--- Part 2 Comparison ---")
    measure_performance(part_02_math, puzzle_input, "Math  ")
    measure_performance(part_02_string, puzzle_input, "String")

if __name__ == "__main__":
    main()