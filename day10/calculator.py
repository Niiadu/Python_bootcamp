
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_calculation = False
    while not continue_calculation:
        operational_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operational_symbol} {num2} = {answer}")
    
    
        calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit ").lower()
        if calculating == "y":
            num1 = answer
            continue_calculation = False
        else:
            continue_calculation = True
            calculator()

calculator()
    
    
    