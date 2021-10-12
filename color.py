""" Fixes most of plain setColor function's arguments
    (just integer numbers, not variables or function calls) """

import os

LEFT = 'love.graphics.setColor('
RIGHT = ')'
DELIMITER = ','
            
def fix_line(line):
    first = line.find(LEFT)

    if first == -1:
        return line

    first += len(LEFT)

    last = line.find(RIGHT, first)

    arguments = line[first:last].split(DELIMITER)

    digit_args_counter = 0
    for arg in arguments:
        if not arg.strip().isdigit():
            break
        digit_args_counter += 1

    if not digit_args_counter:
        return line

    arguments_fixed = []
    for i in range(digit_args_counter):
        arguments_fixed.append(fix_number(arguments[i]))

    arguments_fixed[0] = arguments_fixed[0].strip()

    fixed_line = line[:first]

    for arg in arguments_fixed:
        fixed_line += arg + ','

    for arg in arguments[digit_args_counter:]:
        fixed_line += arg + ','

    fixed_line = fixed_line[:-1]

    fixed_line += line[last:]

    return fixed_line

def fix_number(number):
    fixed_number = int(number) / 255
    return f" {fixed_number:.2f}"

def fix_file(filename):
    with open(filename) as infile:
        for line in infile:
            yield fix_line(line)

def fix_folder(foldername):
    os.mkdir(outfolder(foldername))

def outfolder(foldername):
    folders_list = foldername.split('/')
    folders_list[0] = folders_list[0] + '-out'
    
    return '/'.join(folders_list)
    


def main():
    """Entry point"""

if __name__ == '__main__':
    main()
