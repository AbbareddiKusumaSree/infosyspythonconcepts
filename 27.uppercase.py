# Program to print only uppercase letters from a given string
text = input("Enter a string: ")
result = ""
for char in text:
    if char.isupper():  
        result += char

print("Uppercase letters in the string:", result)
