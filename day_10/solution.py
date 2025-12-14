# --- Day 10: Factory ---

from collections import deque

def part01(machines):
    min_button_presses = 0

    machines_info = get_machines_info(machines)

    for machine in machines_info:
        target_state = tuple(machine['lamps'])
        buttons = machine['buttons']
        start_state = tuple([False] * len(target_state))
        
        queue = deque([(start_state, 0)])
        
        visited = {start_state}
        
        while queue:
            current_state, presses = queue.popleft()
            
            if current_state == target_state:
                min_button_presses += presses
                break
            
            for button in buttons:
                next_state_list = list(current_state)
                for toggle in button:
                    next_state_list[toggle] = not next_state_list[toggle]
                next_state = tuple(next_state_list)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, presses + 1))

    return min_button_presses

def get_machines_info(machines):
    machines_info = []
    for machine in machines:
        machine = machine.split()

        lamps = []
        for lamp in machine[0][1:-1]:
            lamps.append(False if lamp == '.' else True)
        
        buttons = []
        for button in machine[1:-1]:
            lamps_toggled = button[1:-1].split(',')
            lamps_toggled_int = tuple([int(i) for i in lamps_toggled])
            buttons.append(lamps_toggled_int)
        
        joltages = [int(i) for i in machine[-1][1:-1].split(',')]

        machines_info.append({'lamps': lamps, 'buttons': buttons, 'joltages': joltages})
    return machines_info   

def main():
    with open('day_10/input.txt') as input_file:
        machines = input_file.read().splitlines()
        print(part01(machines))
        
if __name__ == '__main__':
    main()