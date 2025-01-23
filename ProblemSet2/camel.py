# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and 
# outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

camel = input("Introduce a word: ")

print("snake_case: ", end="")

for char in camel:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

print()