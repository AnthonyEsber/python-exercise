import operator
dic_ops = {"+" : operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def calculate(op, a, b):
    return(op not in dic_ops and "invalid operation") or dic_ops[op](a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

print(calculate(operation, num1, num2))