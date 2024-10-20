def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        parts = problem.split()
        first_operand, operator, second_operand = parts[0], parts[1], parts[2]

        # Check for valid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands are digits
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check operand length
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

        # Calculate the result if needed
        if display_answers:
            if operator == '+':
                results.append(str(int(first_operand) + int(second_operand)))
            else:
                results.append(str(int(first_operand) - int(second_operand)))

    # Prepare the formatted lines
    first_line = ""
    second_line = ""
    dashes_line = ""
    results_line = ""

    for i in range(len(problems)):
        length = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(length) + "    "
        second_line += operators[i] + second_operands[i].rjust(length - 1) + "    "
        dashes_line += "-" * length + "    "
        if display_answers:
            results_line += results[i].rjust(length) + "    "

    # Remove trailing spaces and construct the final output
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dashes_line = dashes_line.rstrip()
    arranged_problems = first_line + "\n" + second_line + "\n" + dashes_line

    if display_answers:
        results_line = results_line.rstrip()
        arranged_problems += "\n" + results_line

    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
