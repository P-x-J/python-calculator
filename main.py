import sys

from operators import add, divide, multiply, subtract


def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 main.py <operator> <number1> <number2>")

    arguments_list = sys.argv[2:]

    operator_functions = {
        "divide": divide,
        "add": add,
        "subtract": subtract,
        "multiply": multiply
        }
    
    print(str(sys.argv[1]))

    if sys.argv[1] not in operator_functions:
        sys.exit("No operator specified")


    operator_name = sys.argv[1]
    operator_func = operator_functions.get(operator_name)


    if len(sys.argv[2:]) != 2:
        sys.exit("Two numbers must be given")

    try:
        number1 = float(sys.argv[2])
        number2 = float(sys.argv[3])
    except (IndexError, ValueError):
        sys.exit("Please provide two numeric arguments after the operator.")
    
    result = operator_func(number1, number2)

    print(result)


if __name__ == '__main__':
    main()