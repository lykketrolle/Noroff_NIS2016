"""
Name: Kjell Chr. Larsen


First in this assignment you’re going to make a program that calculates two
different variables that are typed in by the user. You going to use the addition,
subtraction, multiplication, division, floor division, modulus and exponent. Print
the answer for each different operation.
"""

print("Hi! and welcome to the Arethmetic program where you can enter two numbers \n"
      "that will be run through some different arethmetic operatoprs. \n\n")

value1 = int(input("Please enter a number: "))
value2 = int(input("Please enter another number: "))
print("")
print("Addition: ", value1 + value2)
print("Substraction: ", value1 - value2)
print("Multiplication: ", value1 * value2)
print("Division: ", value1 / value2)
print("Floor division: ", value1 // value2)
print("Modulus: ", value1 % value2)
print("Exponent: ", value1 ** value2)
