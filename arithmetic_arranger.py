# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
# https://replit.com/@harmonify/arithmetic-arranger#arithmetic_arranger.py

def arithmetic_arranger(problems: list[str], displayed_answer: bool = False) -> None:
    row1 = row2 = row3 = row4 = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        x, operator, y = problem.split()
        str_len = (len(x) if len(x) > len(y) else len(y)) + 2

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not (x.isnumeric() and y.isnumeric()):
            return "Error: Numbers must only contain digits."
        if str_len > 6:
            return "Error: Numbers cannot be more than four digits."

        row1 += f"{x:>{str_len}}    "
        row2 += f"{operator} {y:>{str_len-2}}    "
        row3 += f"{'-' * str_len}    "
        row4 += f"{eval(problem):>{str_len}}    "

    result = [row1, row2, row3]
    if displayed_answer:
        result.append(row4)

    return "\n".join(map(lambda x: x.rstrip(), result))


def main(args=None):
    print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
    # '    3      3801      45      123\n'
    # '+ 855    -    2    + 43    +  49\n'
    # '-----    ------    ----    -----'

    print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
    # 'Error: Too many problems.'

    print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
    # "Error: Operator must be '+' or '-'."

    print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
    # 'Error: Numbers cannot be more than four digits.'
    
    print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
    # 'Error: Numbers must only contain digits.'
    print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
    #   32         1      9999      523
    # +  8    - 3801    + 9999    -  49
    # ----    ------    ------    -----
    #   40     -3800     19998      474

if __name__ == '__main__':
    main()
