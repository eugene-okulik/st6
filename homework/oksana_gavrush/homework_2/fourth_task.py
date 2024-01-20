import math

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

hypotenuse_result = math.sqrt(a**2 + b**2)
triangle_result = a * b / 2

print(hypotenuse_result)
print(triangle_result)
