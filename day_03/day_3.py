
"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..

...*......

..35..633.

......#...

617*......

.....+.58.

..592.....

......755.

...$.*....

.664.598..



In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""

def main():
    lines = read_input()

    print('Part 1:', part_1(lines))
    print('Part 2:', part_2(lines))


def part_1(lines):
    has_adj_symbol_func = lambda val: not val.isdigit() and val != '.' 

    parts = []
    for y, line in enumerate(lines):
        found_part = False
        part_num = []
        for x, char in enumerate(line):
            if char.isdigit():
                part_num.append(char)
                num_adj_symbols = find_adj_coords(lines, x, y, has_adj_symbol_func)
                if (len(num_adj_symbols) > 0):
                    found_part = True
            else:
                if found_part:
                    parts.append(int(''.join(part_num)))
                part_num = []
                found_part = False

        if found_part:
            parts.append(int(''.join(part_num)))
        part_num = []
        found_part = False
    return sum(parts)


def part_2(lines):
    has_adj_part = lambda val: val.isdigit() 

    gear_ratios = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char is '*':
                adj_numbers = {extract_number(lines[coord[0]], coord[1]) for coord in find_adj_coords(lines, x, y, has_adj_part)}

                if len(adj_numbers) == 2:
                    gear_ratios.append(adj_numbers.pop() * adj_numbers.pop())

    return sum(gear_ratios)
                

def find_adj_coords(lines, x, y, eval_func):
    coords = []
    for yj in range(y-1, y+2):
        for xi in range(x-1, x+2):
            if yj >= 0 and yj < len(lines) and xi >= 0 and xi < len(lines[yj]) :
                if eval_func(lines[yj][xi]):
                    coords.append((yj, xi))

    return coords


def extract_number(s, index):
    if 0 <= index < len(s):
        start_index, end_index = index, index

        # Move left
        while start_index >= 0 and s[start_index].isdigit():
            start_index -= 1

        # Move right
        while end_index < len(s) and s[end_index].isdigit():
            end_index += 1

        if start_index != end_index:
            return int(''.join(s[start_index + 1:end_index]))

    return None


def read_input():
    with open('day_03/input.txt') as f:
        return [[char for char in line.strip()] for line in f.readlines()]

if __name__ == '__main__':
    main()

