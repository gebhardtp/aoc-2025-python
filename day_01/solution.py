def read_input(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def part_01(puzzle_input):
    pos = 50
    zeros = 0
    for rotation in puzzle_input:
        if rotation[0] == "R":
            change = int(rotation[1:])
        elif rotation[0] == "L":
            change = -int(rotation[1:])
        pos += change
        pos %= 100
        if pos == 0:
            zeros += 1
    return zeros

def part_02_loop(puzzle_input):
    pos = 50
    zeros = 0
    for rotation in puzzle_input:
        direction = rotation[0]
        change = int(rotation[1:])
        for _ in range(0, change):
            if direction == "R":
                pos += 1
            elif direction == "L":
                pos -= 1
            pos %= 100
            if pos == 0:
                zeros += 1
    return zeros

def part_02(puzzle_input):
    pos = 50
    zeros = 0
    for rotation in puzzle_input:
        direction = rotation[0]
        change = int(rotation[1:])
        if direction == "R":
            new_pos = pos + change
            zeros += (new_pos // 100) - (pos // 100)
            pos = new_pos 
        elif direction == "L":
            new_pos = pos - change
            zeros += ((pos - 1) // 100) - ((new_pos - 1) // 100)
            pos = new_pos
    return zeros

def main():
    puzzle_input = read_input("day_01/input.txt")
    print(f"Part One:         {part_01(puzzle_input)}")
    print(f"Part Two (Loop):  {part_02_loop(puzzle_input)}")
    print(f"Part Two:         {part_02(puzzle_input)}")

if __name__ == "__main__":
    main()
