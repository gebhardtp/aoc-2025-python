# --- Day 5: Cafeteria ---

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
    
def part_01(database):
    number_of_fresh_ingredients = 0

    fresh_ranges, available_ids = read_fresh_and_available(database)

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

def read_fresh_and_available(database):
    reading_ranges = True
    fresh_ranges = []
    available_ids = []
    for line in database:
        if line == "":
            reading_ranges = False
            continue
        if reading_ranges:
            fresh_range = line.split("-")
            fresh_ranges.append((int(fresh_range[0]), int(fresh_range[1])))
        else:
            available_ids.append(int(line))
    return fresh_ranges, available_ids

def main():
    database = read_input("day_05/input.txt")
    print(f"Fresh ingredients: {part_01(database)}")

if __name__ == "__main__":
    main()