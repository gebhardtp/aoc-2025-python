# --- Day 3: Lobby ---

# applied my learnings from yesterday and used string manipulation

def read_input(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def part_01(banks):
    total_joltage = 0

    for bank in banks:
        largest = ("0", 0)
        for i, digit in enumerate(bank):
            if digit > largest[0] and not i >= len(bank) - 1:
                largest = (digit, i)
        
        sec_largest = ("0", 0)
        for i, digit in enumerate(bank[largest[1]+1:], largest[1]+1):
           if digit > sec_largest[0]:
               sec_largest = (digit, i)

        total_joltage += int(largest[0]+sec_largest[0])

    return total_joltage

def part_02(banks):
    total_joltage = 0
    num_batteries = 12

    for bank in banks:
        largest = ""
        found_at = -1

        for x in range(num_batteries):
            cur_largest = ("0", 0)

            for i, digit in enumerate(bank[found_at + 1:], found_at + 1):
                if i > len(bank) - num_batteries + x:
                    break
                elif digit > cur_largest[0]:
                    cur_largest = (digit, i)

            largest += cur_largest[0]
            found_at = cur_largest[1]

        total_joltage += int(largest)

    return total_joltage

def main():
    puzzle_input = read_input("day_03/input.txt")
    print(f"Output joltage (2 batteries):  {part_01(puzzle_input)}")
    print(f"Output joltage (12 batteries): {part_02(puzzle_input)}")

if __name__ == "__main__":
    main()