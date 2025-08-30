#Write a program to print the factorial of N Factorial is the product of all positive integers less than or equal to N.
N = int(input("Enter a number N: "))
factorial = 1

for i in range(1, N + 1):
    factorial *= i

print("Factorial", factorial)
