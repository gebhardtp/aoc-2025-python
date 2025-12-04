# --- Day 4: Printing Department ---

def read_input(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def part_01(rolls_of_paper):
    number_of_accessible_rolls = 0

    for row_index, roll_row in enumerate(rolls_of_paper):
        for collumn_index, roll in enumerate(roll_row):
            if roll == ".":
                continue
            
            number_of_adjacent_rolls = 0
            positions_to_check = [
                (row_index - 1, collumn_index - 1), (row_index - 1, collumn_index), (row_index - 1, collumn_index + 1),
                (row_index, collumn_index - 1), (row_index, collumn_index + 1),
                (row_index + 1, collumn_index - 1), (row_index + 1, collumn_index), (row_index + 1, collumn_index + 1)
            ]

            for position in positions_to_check:
                max_row_index = len(rolls_of_paper) - 1
                max_collumn_index = len(roll_row) - 1
                if position[0] < 0 or position[1] < 0 or position[0] > max_row_index or position[1] > max_collumn_index:
                    continue
                if rolls_of_paper[position[0]][position[1]] == "@":
                    number_of_adjacent_rolls += 1
                if number_of_adjacent_rolls >= 4:
                    break

            if number_of_adjacent_rolls < 4:
                number_of_accessible_rolls += 1

    return number_of_accessible_rolls

def part_02(rolls_of_paper):
    pass

def main():
    puzzle_input = read_input("day_04/input.txt")
    print(f"Accessible rolls:  {part_01(puzzle_input)}")
    # print(f"02: {part_02(puzzle_input)}")

if __name__ == "__main__":
    main()