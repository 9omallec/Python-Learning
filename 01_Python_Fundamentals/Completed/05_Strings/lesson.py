# ===================================
# LESSON 5: String Manipulation
# ===================================

# Strings are text values in quotes
greeting = "Hello, Python!"

# String methods (functions that work on strings):
print(greeting.upper())      # HELLO, PYTHON!
print(greeting.lower())      # hello, python!
print(greeting.replace("Python", "World"))  # Hello, World!

# Length of a string:
print(len(greeting))  # 14 characters

# Combining strings (concatenation):
# Method 1: Using + (must all be strings!)
first_name = "Connor"
last_name = "Rodriguez"
full_name = first_name + " " + last_name
print(full_name)

# Method 2: Using commas in print (adds spaces automatically)
print(first_name, last_name)

# Method 3: Using f-strings (BEST METHOD!)
full_name = f"{first_name} {last_name}"
print(full_name)

age = 20
print(f"My name is {first_name} and I am {age} years old")

# f-strings can do math:
print(f"In 5 years, I'll be {age + 5}")

# String indexing (getting individual characters):
word = "Python"
print(word[0])  # P (first character)
print(word[1])  # y (second character)
print(word[-1]) # n (last character)

# String slicing (getting parts of a string):
print(word[0:3])   # Pyt (characters 0, 1, 2)
print(word[2:])    # thon (from 2 to end)
print(word[:4])    # Pyth (from start to 4)

# Useful string methods:
text = "  hello world  "
print(text.strip())       # "hello world" (removes spaces)
print(text.title())       # "  Hello World  " (capitalize words)
print(text.count("l"))    # 3 (count how many times "l" appears)
print("hello" in text)    # True (check if "hello" is in text)

# ===================================
# More String Methods
# ===================================

# Searching for text:
sentence = "Python is awesome and Python is fun"
print(sentence.find("Python"))      # 0 (first occurrence at index 0)
print(sentence.find("awesome"))     # 10 (starts at index 10)
print(sentence.find("Java"))        # -1 (not found)

# Checking start and end:
filename = "report.pdf"
print(filename.startswith("report"))  # True
print(filename.endswith(".pdf"))      # True
print(filename.endswith(".txt"))      # False

# Checking content type:
print("123".isdigit())    # True - all digits
print("abc".isalpha())    # True - all letters
print("abc123".isalnum()) # True - letters and numbers
print("HELLO".isupper())  # True - all uppercase
print("hello".islower())  # True - all lowercase

# String multiplication:
print("=" * 20)     # ====================
print("ha" * 3)     # hahaha

# Splitting strings into lists:
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

sentence = "Hello World"
words = sentence.split()  # Splits on spaces by default
print(words)  # ['Hello', 'World']
