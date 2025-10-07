from mini_calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    should_accumulate = True
    print(logo)
    number1 = float(input("What is the first number?: "))

    while should_accumulate:
        for key in operation:
            print(key)
        oper = input("Pick an operation: ")
        number2 = float(input("What is the next number?: "))

        result = operation[oper](number1, number2)
        print(f"{number1} {oper} {number2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            number1 = result
        else:
            should_accumulate = False
            print("\n"*20)