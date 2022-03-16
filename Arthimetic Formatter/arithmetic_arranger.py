def arithmetic_arranger(equations, calculate=False):
    arranged = ''
    if len(equations) > 5:
        arranged = "Error: Too many problems."
        return arranged

    if not all([True if ("+" in st or "-" in st) else False for st in equations]):
        arranged = "Error: Operator must be '+' or '-' "
        return arranged

    numbers = []
    for equ in equations:
        p = equ.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged = "Error: Numbers must only contain digits."
        return arranged

    if not(all(map(lambda x: len(x) < 5, numbers))):
        arranged = "Error: Numbers cannot be more than four digits"
        return arranged

    above_row = ''
    bottom_row = ''
    totals = list(map(lambda x: eval(x), equations))
    sol = ''
    dashes = ''
    for i in range(0, len(numbers), 2):
        spaces = max(len(numbers[i]), len(numbers[i + 1])) + 2
        above_row += numbers[i].rjust(spaces) + "    "
        dashes += '-'*spaces + "    "
        sol += str(totals[i//2]).rjust(spaces) + "    "
    j = 0
    for i in range(0, len(numbers), 2):
        spaces = max(len(numbers[i]), len(numbers[i+1])) + 1
        bottom_row += equations[j].split()[1]
        bottom_row += numbers[i+1].rjust(spaces) + "    "
        j += 1

    if calculate:
        arranged = '\n'.join((above_row, bottom_row, dashes, sol))
    else:
        arranged = '\n'.join((above_row, bottom_row, dashes))
    return arranged


