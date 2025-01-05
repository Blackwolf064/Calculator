import math


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        raise ZeroDivisionError
    else:
        return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a ** b
def sqrt(a):
    return math.sqrt(a)

def calculate():
    print("This is a simple calculator!")
    print("Choose an operation: add, sub, mul, div, mod, pow, sqrt")
    operation = input("Enter your choice: ").lower()


    if operation in ['add', 'sub', 'mul', 'div', 'mod', 'pow', 'sqrt']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == 'add':
                print(f'result: {add(num1, num2)}')
            elif operation == 'sub':
                print(f'result: {sub(num1, num2)}')
            elif operation == 'mul':
                print(f'result: {mul(num1, num2)}')
            elif operation == 'div':
                print(f'result: {div(num1, num2)}')
            elif operation == 'mod':
                print(f'result: {mod(num1, num2)}')
            elif operation == 'pow':
                print(f'result: {pow(num1, num2)}')
            elif operation == 'sqrt':
                print(f'result: {sqrt(num1)}')
        except ValueError:
            print('Enter a valid number')
    else:
        print("Invalid operation")
calculate()


