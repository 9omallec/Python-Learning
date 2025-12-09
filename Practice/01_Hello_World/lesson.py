# ===================================
# LESSON 1: Hello World & Print
# ===================================

# This is a comment - Python ignores anything after the # symbol
# Comments help explain what your code does

# The most basic Python command: print()
# This displays text on the screen
print("Hello, World!")
print("Welcome to Python!")

# You can print numbers too
print(42)
print(3.14)

# You can print multiple things at once
print("The answer is", 42)

# Print multiple lines
print("Line 1")
print("Line 2")
print("Line 3")

# ===================================
# Escape Sequences
# ===================================

# Special characters that start with \

# \n = new line (like pressing Enter)
print("Hello\nWorld")
# Output:
# Hello
# World

# \t = tab (adds spacing)
print("Name\tAge\tCity")
print("Connor\t35\tOmaha")
# Output:
# Name    Age     City
# Connor  35      Omaha

# \" = print a quote character
print("She said \"Hello!\"")
# Output: She said "Hello!"

# \\ = print a backslash
print("File path: C:\\Users\\Connor")
# Output: File path: C:\Users\Connor

# ===================================
# Print with Multiple Arguments
# ===================================

# Commas add automatic spaces
print("Hello", "World", "!")
# Output: Hello World !

# You can mix text and numbers
name = "Connor"
age = 35
print("Name:", name, "Age:", age)

# Change separator with sep=
print("2024", "11", "18", sep="-")
# Output: 2024-11-18

# Change ending with end=
print("Hello", end=" ")
print("World")
# Output: Hello World (on same line!)

