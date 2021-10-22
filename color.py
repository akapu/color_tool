""" Fixes most of plain setColor function's arguments
    (just integer numbers, not variables or function calls) """

import os
import pathlib

LEFT = 'love.graphics.setColor('
RIGHT = ')'
DELIMITER = ','
            
def fix_line(line):
    first = line.find(LEFT)

    if first == -1:
        print('ok')
        return line

    first += len(LEFT)

    last = line.find(RIGHT, first)

    arguments = line[first:last].split(DELIMITER)

    digit_args_counter = 0
    for arg in arguments:
        if not arg.strip().isdigit():
            break
        digit_args_counter += 1

    if digit_args_counter < len(arguments):
        print('warning')
    else:
        print('ok')

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
    outfoldername = outfolder(foldername)
    os.mkdir(outfoldername)

    with os.scandir(foldername) as folder:
        for entity in folder:
            if entity.is_file() and entity.name[-4:] == '.lua':
                with open(os.path.join(outfoldername, entity.name), 'w') as outfile:
                    for line in fix_file(os.path.join(foldername, entity.name)): 
                        outfile.write(line)
            if entity.is_dir():
                fix_folder(os.path.join(foldername, entity.name))

def outfolder(foldername):
    folders_list = list(pathlib.PurePath(foldername).parts)
    folders_list[0] = folders_list[0] + '-out'
    
    return '/'.join(folders_list)

def main():
    """Entry point"""

if __name__ == '__main__':
    main()
