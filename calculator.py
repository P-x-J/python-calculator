import sys

from operators import add, divide, multiply, substract


def main(args):
    arguments_list = sys.argv[2:]

    operator_functions = {
        "divide": divide,
        "add": add,
        "substract": substract,
        "multiply": multiply
        }
    
    if operator_functions not in arguments_list:
        sys.exit("No operator specified")


    operator_name = sys.argv[1]

    operator_func = operator_functions.get(operator_name)

    if len(sys.argv[2:]) == 2:
        while True:
            try:
                number1 = float(sys.argv[2])
                number2 = float(sys.argv[3])
            except (IndexError, ValueError):
                print("Please provide two numeric arguments after the operator.")
                pass
            else: 
                break

    result = operator_func(number1, number2)


if __name__ == '__main__':
    main()