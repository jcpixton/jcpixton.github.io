import subprocess

logo = """
 _____________________
|  _________________  |
| | PythonMaster 0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def clear():
    subprocess.call('cls', shell=True)
    
def add(n1, n2):
    """Adds first number to second number, returns result"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts first number from second number, returns result"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies first number to second number, returns result"""
    return n1 * n2

def divide(n1, n2):
    """Divides first number by second number, returns result"""
    return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculate():
    print(logo)
    n1 = float(input("What is the first number?:\n"))
    for symbol in operations:
        print(symbol)
    calculate_again = True
    
    while calculate_again:
        operator = input("Pick an operation:\n")
        while operator not in operations:
            for symbol in operations:
                print(symbol)
            operator = input("Pick a valid operation:\n")
        n2 = float(input("What is the next number?:\n"))
        calculation_operator = operations[operator]
        result = calculation_operator(n1, n2)
        print(f"{n1} {operator} {n2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            n1 = result
        else:
            calculate_again = False
            clear()
            calculate()

calculate()