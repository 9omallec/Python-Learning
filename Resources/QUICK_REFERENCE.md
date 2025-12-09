# Python Quick Reference Card

**Keep this open while coding!**

---

## 🔢 Math Operators

| Operator | What it does | Example | Result |
|----------|--------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (decimal) | `10 / 3` | `3.333...` |
| `//` | Integer division | `10 // 3` | `3` |
| `%` | Remainder (modulo) | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

**Update operators:**
- `x += 5` → Add 5 to x
- `x -= 5` → Subtract 5 from x
- `x *= 5` → Multiply x by 5

---

## 📝 Variables

```python
# Create variables (no parentheses needed!)
name = "Connor"           # ✅ Correct
name = ("Connor")         # ❌ Unnecessary parentheses

# Multiple types
age = 35                  # Integer
price = 19.99             # Float
is_student = True         # Boolean
city = "Omaha"            # String
```

---

## 🔤 Strings

### Common String Methods
```python
text = "Hello World"

text.upper()              # "HELLO WORLD"
text.lower()              # "hello world"
text.title()              # "Hello World"
text.replace("World", "Python")  # "Hello Python"
len(text)                 # 11 (length)
```

### String Indexing & Slicing
```python
name = "Connor"
#      C o n n o r
#      0 1 2 3 4 5
#     -6-5-4-3-2-1

name[0]      # "C" (first character)
name[-1]     # "r" (last character)
name[0:3]    # "Con" (first 3 characters)
name[2:]     # "nnor" (from index 2 to end)
name[-3:]    # "nor" (last 3 characters)
```

### F-Strings (Best Way to Combine Text + Variables)
```python
name = "Connor"
age = 35

# ✅ Use f-strings
print(f"My name is {name} and I'm {age}")

# ❌ Don't use + for numbers
print("Age: " + age)      # ERROR!

# ✅ F-string handles conversion
print(f"Age: {age}")      # Works!
```

---

## 🎹 User Input

```python
# Get text input
name = input("What's your name? ")

# Get number input (must convert!)
age = int(input("What's your age? "))      # Integer
price = float(input("What's the price? ")) # Decimal

# Common mistake:
num = input("Enter number: ")
print(num + 10)  # ❌ ERROR! num is a string

# Correct:
num = int(input("Enter number: "))
print(num + 10)  # ✅ Works!
```

---

## 🔄 Type Conversions

```python
int("42")        # Convert string to integer → 42
float("3.14")    # Convert string to float → 3.14
str(42)          # Convert number to string → "42"

# Why this matters:
age = input("Age? ")  # Returns "25" (string)
age = int(age)        # Now it's 25 (number)
```

---

## ⚖️ Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater or equal | `x >= 5` |
| `<=` | Less or equal | `x <= 5` |

---

## 🔀 If/Else Statements

```python
# Basic if
if age >= 18:
    print("Adult")

# If/else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If/elif/else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# Combining conditions
if age >= 18 and has_license:
    print("Can drive")

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

---

## 🔁 Loops

### For Loops
```python
# Print 0-4
for i in range(5):
    print(i)

# Print 1-10
for i in range(1, 11):
    print(i)

# Count by 2s: 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)

# Loop through string
for letter in "Connor":
    print(letter)
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Loop until condition
password = ""
while password != "secret":
    password = input("Password: ")
```

### Loop Control
```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break  # Stop at 5

# Continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

---

## 📚 Lists

```python
# Create a list
foods = ["pizza", "tacos", "ramen"]

# Access items
foods[0]        # "pizza" (first)
foods[-1]       # "ramen" (last)

# Add items
foods.append("sushi")      # Add to end
foods.insert(0, "burger")  # Insert at position

# Remove items
foods.remove("pizza")      # Remove by value
foods.pop()                # Remove last item

# List operations
len(foods)      # Length
"pizza" in foods  # Check if exists
foods.sort()    # Sort alphabetically
```

---

## 🗂️ Dictionaries

```python
# Create dictionary
person = {
    "name": "Connor",
    "age": 35,
    "city": "Omaha"
}

# Access values
person["name"]     # "Connor"
person.get("age")  # 35

# Add/update
person["job"] = "Developer"
person["age"] = 36

# Loop through
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🎯 Functions

```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call it

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Connor")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8

# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # "Hello, Guest!"
greet("Connor")  # "Hello, Connor!"
```

---

## 🐛 Common Mistakes to Avoid

### ❌ Don't Do This | ✅ Do This Instead
```python
# Unnecessary parentheses
name = ("Connor")        # ❌
name = "Connor"          # ✅

# Wrong division operator
print(int(3 / 100))      # ❌ Wrong math!
print(100 // 3)          # ✅ Integer division

# Forgetting to convert input
age = input("Age? ")
print(age + 1)           # ❌ Can't add to string
age = int(input("Age? "))
print(age + 1)           # ✅ Works!

# Wrong slice for first character
name[0:0]                # ❌ Gets nothing!
name[0]                  # ✅ Gets first char

# Tuple in f-string
f"{first, last}"         # ❌ Shows ('Connor', "O'Malley")
f"{first} {last}"        # ✅ Shows Connor O'Malley
```

---

## 💡 Pro Tips

1. **F-strings are almost always the answer** for combining text and variables
2. **Use `//` for integer division**, not `int(a / b)`
3. **Remember: `input()` always returns a string** - convert it!
4. **Slice syntax: `[start:end]`** - end is NOT included
5. **Negative indices count from the end**: `[-1]` is last item
6. **Use descriptive variable names**: `temperature` not `temp`

---

**Print this out or keep it open in a second monitor!**
