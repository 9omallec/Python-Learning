# Python Syntax Quick Reference

**Look it up when you need it - don't memorize**

---

## 💡 How to Use This File

**This is NOT for memorization!**

This is your **quick lookup reference** while coding:
- Keep it open in a second window
- Ctrl+F to search for what you need
- Copy examples and modify for your code
- Come back as often as needed

**Remember:** Professional programmers look up syntax daily. You're not supposed to memorize everything!

---

## 📝 Print Statements

### Basic Print
```python
print("Hello")
print(42)
```

### Multiple Items
```python
print("Name:", "Connor", "Age:", 35)
# Output: Name: Connor Age: 35
```

### F-Strings (Recommended)
```python
name = "Connor"
age = 35
print(f"My name is {name} and I'm {age}")
```

### Special Characters
```python
print("Line 1\nLine 2")  # \n = new line
print("Tab\there")        # \t = tab
```

---

## 🔢 Variables

### Assignment
```python
name = "Connor"
age = 35
price = 19.99
is_active = True
```

### Multiple Assignment
```python
x, y, z = 1, 2, 3
a = b = c = 0
```

### Updating Variables
```python
count = 0
count = count + 1  # Increment
count += 1         # Shorthand
count -= 1         # Decrement
count *= 2         # Multiply
count /= 2         # Divide
```

---

## 📊 Data Types

### Checking Type
```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hello")   # <class 'str'>
type(True)      # <class 'bool'>
```

### Converting Types
```python
int("42")           # String to int: 42
float("3.14")       # String to float: 3.14
str(42)             # Int to string: "42"
int(3.14)           # Float to int: 3 (cuts off decimal)
```

---

## ➕ Math Operations

### Basic Operations
```python
10 + 5      # Addition: 15
10 - 5      # Subtraction: 5
10 * 5      # Multiplication: 50
10 / 5      # Division: 2.0 (always float)
10 // 5     # Integer division: 2 (no decimal)
10 % 3      # Modulo (remainder): 1
10 ** 2     # Exponent (power): 100
```

### Order of Operations
```python
2 + 3 * 4        # 14 (multiplication first)
(2 + 3) * 4      # 20 (parentheses first)
```

---

## 💬 Strings

### Creating Strings
```python
name = "Connor"
name = 'Connor'  # Both work
multiline = """Line 1
Line 2
Line 3"""
```

### String Operations
```python
"Hello" + "World"       # Concatenation: "HelloWorld"
"Hello" + " " + "World" # "Hello World"
"Ha" * 3                # Repetition: "HaHaHa"
len("Hello")            # Length: 5
```

### String Methods
```python
"hello".upper()         # "HELLO"
"HELLO".lower()         # "hello"
"hello".capitalize()    # "Hello"
"hello".title()         # "Hello"
"  hello  ".strip()     # "hello" (removes spaces)
"hello world".replace("world", "there")  # "hello there"
```

### String Formatting
```python
name = "Connor"
age = 35

# F-strings (Best)
f"I'm {name}, age {age}"

# Format method
"I'm {}, age {}".format(name, age)

# Old way (don't use)
"I'm %s, age %d" % (name, age)
```

### String Indexing
```python
text = "Hello"
text[0]      # "H" (first character)
text[-1]     # "o" (last character)
text[1:4]    # "ell" (characters 1-3)
text[:3]     # "Hel" (first 3)
text[2:]     # "llo" (from index 2 to end)
```

---

## ⌨️ User Input

### Basic Input
```python
name = input("What's your name? ")
# Returns string
```

### Converting Input
```python
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```

### Input Validation
```python
while True:
    age = int(input("Enter age: "))
    if age > 0:
        break
    print("Must be positive!")
```

---

## 🔀 If/Else Statements

### Basic If
```python
if age >= 18:
    print("Adult")
```

### If/Else
```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### If/Elif/Else
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

### Comparison Operators
```python
==    # Equal to
!=    # Not equal to
>     # Greater than
<     # Less than
>=    # Greater than or equal
<=    # Less than or equal
```

### Logical Operators
```python
age >= 18 and age < 65    # Both must be True
age < 18 or age >= 65     # At least one must be True
not is_banned             # Reverses True/False
```

### Nested If
```python
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Too young")
```

---

## 🔁 For Loops

### Basic For Loop
```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

### Range with Start/Stop
```python
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5
```

### Range with Step
```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

### Counting Backwards
```python
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, ..., 1
```

### Looping Over Strings
```python
for letter in "Hello":
    print(letter)
# Output: H, e, l, l, o
```

### Looping Over Lists
```python
for item in ["apple", "banana", "cherry"]:
    print(item)
```

---

## 🔄 While Loops

### Basic While
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### While with Break
```python
while True:
    answer = input("Type 'quit': ")
    if answer == "quit":
        break
```

### While with Continue
```python
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Skip 5
    print(count)
```

### Input Validation Loop
```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

---

## 📚 Lists

### Creating Lists
```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]
empty = []
```

### Accessing Items
```python
numbers = [10, 20, 30, 40]
numbers[0]      # 10 (first)
numbers[-1]     # 40 (last)
numbers[1:3]    # [20, 30] (slice)
```

### Modifying Lists
```python
numbers = [1, 2, 3]
numbers.append(4)           # Add to end: [1,2,3,4]
numbers.insert(0, 0)        # Insert at index: [0,1,2,3,4]
numbers.remove(2)           # Remove value 2: [0,1,3,4]
numbers.pop()               # Remove last: [0,1,3]
numbers.pop(0)              # Remove at index: [1,3]
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()              # [1, 1, 3, 4, 5]
numbers.reverse()           # [5, 4, 3, 1, 1]
len(numbers)                # 5
numbers.count(1)            # 2 (appears twice)
numbers.index(4)            # 2 (index of value 4)
```

### Looping Over Lists
```python
for item in numbers:
    print(item)

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
```

---

## 🔧 Functions

### Basic Function
```python
def greet():
    print("Hello!")

greet()  # Call the function
```

### Function with Parameters
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Connor")
```

### Function with Return
```python
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

### Function with Default Value
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # "Hello, Guest!"
greet("Connor")   # "Hello, Connor!"
```

### Multiple Returns
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3])
```

---

## 📖 Dictionaries

### Creating Dictionaries
```python
person = {
    "name": "Connor",
    "age": 35,
    "city": "New York"
}
```

### Accessing Values
```python
person["name"]           # "Connor"
person.get("age")        # 35
person.get("email", "")  # "" (default if missing)
```

### Modifying Dictionaries
```python
person["age"] = 36           # Update
person["email"] = "a@b.com"  # Add new
del person["city"]           # Delete
```

### Dictionary Methods
```python
person.keys()       # All keys
person.values()     # All values
person.items()      # Key-value pairs
```

### Looping Over Dictionaries
```python
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🛠️ Common Built-in Functions

### Math Functions
```python
abs(-5)            # 5 (absolute value)
min(1, 5, 3)       # 1
max(1, 5, 3)       # 5
sum([1, 2, 3])     # 6
round(3.14159, 2)  # 3.14
```

### Type Checking
```python
isinstance(42, int)         # True
isinstance("hi", str)       # True
```

### Other Useful Functions
```python
len("hello")        # 5
len([1, 2, 3])      # 3
input("Prompt: ")   # Get user input
print("Output")     # Display output
range(5)            # 0,1,2,3,4
```

---

## 🚨 Common Error Patterns

### SyntaxError: Missing Colon
```python
# WRONG
if age > 18
    print("Adult")

# RIGHT
if age > 18:
    print("Adult")
```

### IndentationError
```python
# WRONG
if age > 18:
print("Adult")

# RIGHT
if age > 18:
    print("Adult")
```

### NameError: Undefined Variable
```python
# WRONG
print(name)  # name doesn't exist

# RIGHT
name = "Connor"
print(name)
```

### TypeError: Wrong Type
```python
# WRONG
age = input("Age: ")
if age > 18:  # Can't compare string to number

# RIGHT
age = int(input("Age: "))
if age > 18:
```

### IndexError: Out of Range
```python
numbers = [1, 2, 3]
# WRONG: numbers[5]  # Index doesn't exist

# RIGHT: Check length first
if len(numbers) > 5:
    print(numbers[5])
```

---

## 🎨 Code Style (PEP 8)

### Variable Names
```python
# Good
user_name = "Connor"
total_price = 99.99
is_active = True

# Bad (but works)
userName = "Connor"  # camelCase (not Python style)
UserName = "Connor"  # PascalCase (for classes only)
```

### Spacing
```python
# Good
x = 5
result = x + 10

# Bad (but works)
x=5
result=x+10
```

### Constants
```python
# Use CAPS for constants
MAX_SIZE = 100
PI = 3.14159
```

---

## 💡 Quick Tips

1. **Use f-strings** for formatting (not % or .format())
2. **Use `//` for integer division**, `/` for float division
3. **Strings are immutable** - can't change individual characters
4. **Lists are mutable** - can change items
5. **Indentation matters** - use 4 spaces (not tabs)
6. **`==` compares values**, `=` assigns values
7. **String comparison is case-sensitive**
8. **Range stops BEFORE the end number**
9. **List indices start at 0**
10. **Google is your friend** - programmers look things up constantly!

---

## 🔍 How to Find What You Need

**In this file:**
- Use Cmd+F (Mac) or Ctrl+F (Windows)
- Search for keyword (e.g., "loop", "string", "list")

**Online:**
- Google: "python how to [what you want to do]"
- Example: "python how to reverse a string"
- Example: "python how to check if number is even"

---

## 📌 Remember

**This is a REFERENCE, not a study guide!**

- Don't try to memorize everything
- Look things up as you need them
- Build projects to learn syntax naturally
- The more you use it, the more you'll remember
- It's totally normal to forget syntax
- Pro programmers look things up daily

**Your job:** Understand concepts and solve problems
**This file's job:** Remind you of syntax when needed

---

**Last Updated:** 2025-12-08
**Purpose:** Quick lookup reference (not memorization)
**Usage:** Keep open while coding, Ctrl+F to search
