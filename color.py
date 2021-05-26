""" Fixes most of plain setColor function's arguments
    (just integer numbers, not variables or function calls) """

LEFT = 'love.graphics.setColor('
RIGHT = ')'
DELIMITER = ','

def fix_color(filename):
    fixed_file = []

    with open(filename) as file:
        for line in file:
            line = fix_line(line)
            fixed_file.append(line)
            
def fix_line(line):
    first = line.find(LEFT)

    if first == -1:
        return line

    last = line.find(RIGHT, first)

    arguments = line[first:last].split(DELIMITER)

    digit_args_counter = 0
    for arg in arguments:
        if not arg.strip().isdigit():
            break
        digit_args_counter += 1

    arguments_fixed = []
    for i in range(digit_args_counter):
        arguments_fixed.append(fix_number(arguments[i]))


    return line

def fix_number(number):
    return number

def main():
    """Entry point"""

if __name__ == '__main__':
    main()
