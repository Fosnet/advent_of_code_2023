

def is_symbol(c):
    return not (c.isdigit() or c == '.')


with open('inputs/3.txt', 'r') as f:
    grid = f.readlines()

vertical = len(grid)
horizontal = len(grid[0]) - 1


# Part 1
all_numbers = []
prev_character = '.'
for y in range(vertical):
    start_tracking = False
    number = ''
    for x in range(horizontal):
        character = grid[y][x]
        if character.isdigit():
            if not prev_character.isdigit():
                start_tracking = True
                start_x = x
            number += character
        elif start_tracking:
            start_tracking = False
            stop_x = x

            row_check = []
            if start_x - 1 < 0:
                start_x = 1
            if stop_x + 1 > horizontal:
                stop_x = horizontal - 1
            for xi in range(start_x - 1, stop_x+1):
                if y - 1 < 0:
                    y_coord = [0, 1]
                elif y >= vertical - 1:
                    y_coord = [-1, 0]
                else:
                    y_coord = [-1, 0, 1]
                for yi in y_coord:
                    row_check.append(is_symbol(grid[y+yi][xi]))

            if not any(row_check):
                number = ''

            if number:
                all_numbers.append(int(number))
                number = ''
            go_to_next = True


        prev_character = character

    if number:
        stop_x = x

        row_check = []
        if start_x - 1 < 0:
            start_x = 1
        if stop_x + 1 > horizontal:
            stop_x = horizontal - 1
        for xi in range(start_x - 1, stop_x + 1):
            if y - 1 < 0:
                y_coord = [0, 1]
            elif y >= vertical - 1:
                y_coord = [-1, 0]
            else:
                y_coord = [-1, 0, 1]
            for yi in y_coord:
                row_check.append(is_symbol(grid[y + yi][xi]))

        if not any(row_check):
            number = ''

        if number:
            all_numbers.append(int(number))
            number = ''
        go_to_next = True
    prev_character = '.'

print(sum(all_numbers))


# Part 2

class Part:
    def __init__(self, value, x, y):
        self.value = int(value)
        self.x = x
        self.y = y


all_numbers = []
prev_character = '.'
parts_list = []
for y in range(vertical):
    start_tracking = False
    number = ''
    for x in range(horizontal):
        character = grid[y][x]
        if character.isdigit():
            if not prev_character.isdigit():
                start_tracking = True
                start_x = x
            number += character
        elif start_tracking:
            start_tracking = False
            stop_x = x

            row_check = []
            if start_x - 1 < 0:
                start_x = 1
            if stop_x + 1 > horizontal:
                stop_x = horizontal - 1
            for xi in range(start_x - 1, stop_x+1):
                if y - 1 < 0:
                    y_coord = [0, 1]
                elif y >= vertical - 1:
                    y_coord = [-1, 0]
                else:
                    y_coord = [-1, 0, 1]
                for yi in y_coord:
                    row_check.append(is_symbol(grid[y+yi][xi]))
                    if is_symbol(grid[y+yi][xi]) and grid[y+yi][xi] == '*':
                        parts_list.append(Part(value=number, y=y+yi, x=xi))

            if not any(row_check):
                number = ''

            if number:
                all_numbers.append(int(number))
                number = ''
            go_to_next = True

        prev_character = character

    if number:
        stop_x = x

        row_check = []
        if start_x - 1 < 0:
            start_x = 1
        if stop_x + 1 > horizontal:
            stop_x = horizontal - 1
        for xi in range(start_x - 1, stop_x + 1):
            if y - 1 < 0:
                y_coord = [0, 1]
            elif y >= vertical - 1:
                y_coord = [-1, 0]
            else:
                y_coord = [-1, 0, 1]
            for yi in y_coord:
                row_check.append(is_symbol(grid[y + yi][xi]))
                if is_symbol(grid[y+yi][xi]) and grid[y+yi][xi] == '*':
                    parts_list.append(Part(value=number, y=y+yi, x=xi))

        if not any(row_check):
            number = ''

        if number:
            all_numbers.append(int(number))
            number = ''
        go_to_next = True
    prev_character = '.'

gear_ratios = []
for part1 in parts_list:
    for part2 in parts_list:
        if not part1 == part2:
            if part1.x == part2.x and part1.y == part2.y:
                gear_ratios.append(part1.value * part2.value)

print(int(sum(gear_ratios) / 2))  # does a*b and b*a so divide total by 2

