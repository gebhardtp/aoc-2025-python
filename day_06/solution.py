# --- Day 6: Trash Compactor ---

import math

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
    
def part_01(worksheet):
    grand_total = 0
    problems = get_problems(worksheet)
    for problem in problems:
        total = 0
        if problem[len(problem) - 1] == "*":
            total = math.prod(problem[:len(problem) - 1])
        elif problem[len(problem) - 1] == "+":
            total = sum(problem[:len(problem) - 1])
        grand_total += total
    return grand_total

def get_problems(worksheet):
    problems = []
    for line_idx, line in enumerate(worksheet):
        line_list = line.split()
        for collumn_idx, collumn in enumerate(line_list):
            try:
                collumn = int(collumn)
            except ValueError:
                pass
            if line_idx == 0:
                problems.append([collumn])
            else:
                problems[collumn_idx].append(collumn)
    return problems

def main():
    worksheet = read_input("day_06/input.txt")
    print(f"Grand total: {part_01(worksheet)}")

if __name__ == "__main__":
    main()
