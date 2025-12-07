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

def main():
    with open("day_07/test_input.txt") as file:
        diagram = file.read().splitlines()
        print(f"\nTotal splits: {part_01(diagram)}\n")

if __name__ == "__main__":
    main()