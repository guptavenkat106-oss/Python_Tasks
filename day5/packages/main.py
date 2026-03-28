from utilities import math_operations
from utilities import string_operations

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", math_operations.add(num1, num2))
print("Multiplication:", math_operations.multiply(num1, num2))

text = input("Enter a string: ")

print("Uppercase:", string_operations.to_uppercase(text))
print("Character count:", string_operations.count_characters(text))
