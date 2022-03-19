def arithmetic_arranger(equations, calculate=False):
    arranged_problems = ''
    operators = []
    numbers = []
    for equ in equations:
        try:
            numbers.extend([int(equ.split()[0]), int(equ.split()[2])])
        except:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

        operators.append(equ.split()[1])

    print(numbers)
    print(operators)

    if len(equations) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    # for op in operators:
    #     if op == "+" or op == "-":
    #         continue
    #     else:
    #         arranged_problems = "Error: Operator must be '+' or '-'."
    #     return arranged_problems
    # Alternative method to the sma thing as above
    if not all(map(lambda x: x == "+" or x == "-", operators)):
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    for num in numbers:
        if len(str(num)) >= 5:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

    above_row = ''
    bottom_row = ''
    totals = list(map(lambda x: eval(x), equations))
    ti = 0
    sol = ''
    dashes = ''
    k = 0
    for i in range(1, len(numbers), 2):
        spaces = max(len(str(numbers[i - 1])), len(str(numbers[i]))) + 2
        print(spaces)
        above_row += str(numbers[i - 1]).rjust(spaces) if i == len(numbers) - 1 else str(numbers[i - 1]).rjust(
            spaces) + "    "
        bottom_row += operators[i - (k + 1)] + " " + str(numbers[i]).rjust(spaces - 2) if i == len(numbers) - 1 else \
        operators[i - (k + 1)] + " " + str(numbers[i]).rjust(spaces - 2) + "    "
        dashes += '-' * spaces if i == len(numbers) - 1 else '-' * spaces + "    "
        sol += str(totals[ti]).rjust(spaces) if i == len(numbers) - 1 else str(totals[ti]).rjust(spaces) + "    "
        k += 1
        ti += 1

    if calculate:
        arranged_problems = '\n'.join((above_row, bottom_row, dashes, sol))
    else:
        arranged_problems = '\n'.join((above_row, bottom_row, dashes))
    return arranged_problems


print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))