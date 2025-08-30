# Program to print only alphabets from a given string
text = input("Enter a string: ")
result = ""
for char in text:
    if char.isalpha():   
        result += char

print("Alphabets in the string:", result)
