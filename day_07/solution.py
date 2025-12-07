# --- Day 7: Laboratories ---

def part_01(diagram):
    total_splits = 0
    for line_index in range(1, len(diagram)):
        for char_index in range(len(diagram[line_index])):
            char = diagram[line_index][char_index]
            char_above = diagram[line_index - 1][char_index]
            if char == "." and (char_above == "S" or char_above == "|"):
                diagram[line_index] = replace_char(diagram[line_index], "|", char_index)
            elif char == "^" and char_above == "|":
                total_splits += 1
                if char_index > 0:
                    diagram[line_index] = replace_char(diagram[line_index], "|", char_index - 1)
                if char_index < len(diagram[line_index]):
                    diagram[line_index] = replace_char(diagram[line_index], "|", char_index + 1)
    print_diagram_lines(diagram)
    return total_splits

def replace_char(string, char, char_index):
    return string[:char_index] + char + string[char_index + 1:]

def print_diagram_lines(diagram_lines):
    print("\nPrinting Diagram ...\n")
    for line in diagram_lines:
        print(line)

def part_02(diagram):
    possible_paths = 0

    rows = len(diagram)
    collumns = len(diagram[0])
    diagram_values = [[0 for _ in range(collumns)] for _ in range(rows)]

    for row in range(rows):
        for collumn in range(collumns):
            if diagram[row][collumn] == "S":
                diagram_values[row][collumn] = 1

    for row in range(rows - 1):
        for collumn in range(collumns):
            if diagram_values[row][collumn] > 0:
                current_tile = diagram[row][collumn]
                if current_tile == '.' or current_tile == 'S':
                    diagram_values[row+1][collumn] += diagram_values[row][collumn]
                elif current_tile == '^':
                    if collumn > 0:
                        diagram_values[row+1][collumn-1] += diagram_values[row][collumn]
                    if collumn < collumns - 1:
                        diagram_values[row+1][collumn+1] += diagram_values[row][collumn]
    
    possible_paths = sum(diagram_values[-1])
    return possible_paths

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()

def main():
    print(f"\nTotal splits: {part_01(read_input("day_07/input.txt"))}")
    print(f"\nPossible paths: {part_02(read_input("day_07/input.txt"))}\n")

if __name__ == "__main__":
    main()