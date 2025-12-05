# --- Day 5: Cafeteria ---

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
    
def part_01(database):
    number_of_fresh_ingredients = 0

    fresh_ranges = read_fresh(database)
    available_ids = read_available(database)

    for id in available_ids:
        found_in_range = False
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= id <= fresh_range[1]:
                found_in_range = True
                break
        if found_in_range:
            number_of_fresh_ingredients += 1
            continue

    return number_of_fresh_ingredients

def part_02(database):
    number_of_fresh_ids = 0
    fresh_ranges = read_fresh(database)
    fresh_ranges.sort()

    merged_ranges = merge_overlapping_ranges(fresh_ranges, 0)

    for merged_range in merged_ranges:
        number_of_fresh_ids += merged_range[1] - merged_range[0] + 1
    
    return number_of_fresh_ids

def merge_overlapping_ranges(fresh_ranges, index=0):
    if index >= len(fresh_ranges) - 1:
        return fresh_ranges
    
    if fresh_ranges[index][1] >= fresh_ranges[index + 1][0]:
        new_end = max(fresh_ranges[index][1], fresh_ranges[index + 1][1])
        fresh_ranges[index] = (fresh_ranges[index][0], new_end)
        fresh_ranges.pop(index + 1)
    else:
        index += 1

    return merge_overlapping_ranges(fresh_ranges, index)


def read_available(database):
    read_ids = False
    available_ids = []
    for line in database:
        if read_ids:
            available_ids.append(int(line))
        elif line == "":
            read_ids = True
    return available_ids

def read_fresh(database):
    fresh_ranges = []
    for line in database:
        if line == "":
            break
        fresh_range = line.split("-")
        fresh_ranges.append((int(fresh_range[0]), int(fresh_range[1])))
    return fresh_ranges

def main():
    database = read_input("day_05/input.txt")
    print(f"Fresh ingredients: {part_01(database)}")
    print(f"Fresh IDs: {part_02(database)}")

if __name__ == "__main__":
    main()
