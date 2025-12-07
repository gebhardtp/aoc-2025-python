# --- Day 6: Trash Compactor ---

import math

def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
    
def solve(worksheet, part):
    grand_total = 0
    if part == 1:
        problems = get_problems_01(worksheet)
    elif part == 2:
        problems = get_problems_02(worksheet)
    else:
        raise Exception("part must be 1 or 2")
    for problem in problems:
        total = 0
        if problem[len(problem) - 1] == "*":
            total = math.prod(problem[:len(problem) - 1])
        elif problem[len(problem) - 1] == "+":
            total = sum(problem[:len(problem) - 1])
        grand_total += total
    return grand_total

def get_problems_01(worksheet):
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

def get_problems_02(worksheet):
    problems = []
    line_length = len(worksheet[0])
    worksheet_length = len(worksheet)
    problem = []
    for char_idx in range(line_length - 1, -1, -1):
        number_str = ""
        number = 0
        operator = ""
        for line_idx in range(worksheet_length):
            char = worksheet[line_idx][char_idx]
            if char != "*" and char != "+":
                number_str += worksheet[line_idx][char_idx]
            else:
                operator = char
        if number_str.strip() != "":
            number = int(number_str)
            problem.append(number)
        if operator != "":
            problem.append(operator)
            problems.append(problem)
            problem = []
    return problems

def main():
    worksheet = read_input("day_06/input.txt")
    print(f"Grand total 01: {solve(worksheet, 1)}")
    print(f"Grand total 02: {solve(worksheet, 2)}")

if __name__ == "__main__":
    main()
