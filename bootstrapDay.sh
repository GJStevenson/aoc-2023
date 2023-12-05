#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

day_number=$1
day_directory="day_$(printf "%02d" $day_number)"
input_url="https://adventofcode.com/2023/day/$day_number/input"
description_url="https://adventofcode.com/2023/day/$day_number"

mkdir -p $day_directory

description=$(curl -s $description_url | awk '/<article class="day-desc">/,/<\/article>/' | sed 's/<[^>]*>//g' | awk '{gsub(/&nbsp;/, " "); print}' | sed 's/$/\n/')

echo "
\"\"\"
${description}
\"\"\"

def main():
    lines = read_input()
    print(lines)

    print('Part 1:', part_1(lines))
    print('Part 2:', part_2(lines))


def part_1(lines):
    return 0


def part_2(lines):
    return 0


def read_input():
    with open('${day_directory}/input.txt') as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    main()
" > "${day_directory}/day_${day_number}.py"

touch "${day_directory}/input.txt"

echo "Files created for day $day_number in $day_directory."
