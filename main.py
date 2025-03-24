#!/usr/bin/python3
import shlex

from calculator_app import add, multiply, divide, subtract

num1 = input("Available operations: Add, Subtract, divide, multiply: Please type one out!, then the two numbers to be operated on:  ")

inputs = shlex.split(num1)

operation = inputs[0]
x = int(inputs[1])
y = int(inputs[2])

if operation == 'add' or operation == 'Add' or operation == 'ADD':
    print(f"Addition of {x} and {y} is {add(x, y)}")
elif operation == "subtract" or operation == "Subtract" or operation == "SUBTRACT":
    print(f"Subtracting {x} and {y} resulted in {subtract(x, y)}")
elif operation == "multiply" or operation == "Multiply" or operation == "MULTIPLY":
    print(f"Multiplication of {x} and {y} is {multiply(x, y)}")
elif operation == "divide" or operation == "Divide" or operation == "DIVIDE":
    print(f"Division of {x} and {y} is {divide(x, y)}")
else:
    print("Ensure you have proper numbers in integer formart of type out the operation")
