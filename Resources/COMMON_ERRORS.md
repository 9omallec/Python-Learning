# Common Python Errors & How to Fix Them

**Your debugging companion!**

---

## 🔴 NameError: name 'variable' is not defined

### What it means:
Python doesn't know what that variable is.

### Common causes:

**1. Didn't run all the lines together**
```python
# You ran only this line:
print(fahr)  # ❌ ERROR: name 'fahr' is not defined

# Fix: Run BOTH lines together
fahr = 100
print(fahr)  # ✅ Works!
```

**2. Typo in variable name**
```python
fahrenheit = 100
print(farenheit)  # ❌ ERROR: Spelled wrong!
print(fahrenheit) # ✅ Correct spelling
```

**3. Variable is in a different scope**
```python
def my_function():
    x = 5

print(x)  # ❌ ERROR: x only exists inside the function
```

---

## 🔴 TypeError: can only concatenate str (not "int") to str

### What it means:
You're trying to mix strings and numbers with `+`.

### Examples:

```python
age = 35
print("I am " + age)  # ❌ ERROR!

# Fix option 1: Use f-string
print(f"I am {age}")  # ✅ Works!

# Fix option 2: Convert to string
print("I am " + str(age))  # ✅ Works but not Pythonic
```

---

## 🔴 ValueError: invalid literal for int() with base 10

### What it means:
Trying to convert something to a number that isn't a number.

### Common causes:

**1. Converting text to number**
```python
num = int("hello")  # ❌ ERROR: "hello" isn't a number
num = int("42")     # ✅ Works!
```

**2. Input confusion in terminal**
```python
# When it prompts "What is your age?", you typed code instead of a number
age = int(input("What is your age? "))
# Prompt appears: What is your age?
# You type: 35  # ✅ Correct
# NOT: age = 35  # ❌ Wrong - that's code, not your answer!
```

**3. Empty input**
```python
num = int(input("Number: "))
# User presses Enter without typing → ERROR!
```

---

## 🔴 SyntaxError: invalid syntax

### What it means:
Python doesn't understand your code structure.

### Common causes:

**1. Missing quotes**
```python
name = Connor  # ❌ ERROR: Missing quotes
name = "Connor"  # ✅ Works!
```

**2. Wrong operator**
```python
b - int(input())  # ❌ Should be = not -
b = int(input())  # ✅ Correct
```

**3. Missing closing quote/parenthesis**
```python
print("Hello)      # ❌ Missing closing quote
print("Hello")     # ✅ Correct

print(f"{name}, {age}")  # ❌ Missing closing quote
print(f"{name}, {age}")  # ✅ Correct
```

**4. Using @ without quotes**
```python
email = name + @ + domain  # ❌ @ needs quotes
email = name + "@" + domain  # ✅ Works
```

---

## 🔴 IndexError: string index out of range

### What it means:
Trying to access a position that doesn't exist.

### Examples:

```python
name = "Bob"
print(name[5])  # ❌ ERROR: Only 3 characters (0,1,2)
print(name[2])  # ✅ Works! (last character)

# Wrong slice
word = "hi"
print(word[0:10])  # ✅ Actually works! Python handles it
print(word[10])    # ❌ ERROR: No character at position 10
```

---

## 🔴 IndentationError: expected an indented block

### What it means:
Python needs indentation after `if`, `for`, `while`, `def`, etc.

### Examples:

```python
# Wrong
if age >= 18:
print("Adult")  # ❌ ERROR: Needs indentation

# Correct
if age >= 18:
    print("Adult")  # ✅ Indented with 4 spaces or Tab
```

---

## 🔴 Running Input() Issues in VSCode Terminal

### Problem:
When you run code with `input()` using `Shift + Return`, the next line of code gets sent as your answer!

### Example of what goes wrong:
```python
# You highlight these 3 lines and press Shift + Return:
age = int(input("What is your age? "))
result = age + 10
print(result)

# Terminal shows:
What is your age? result = age + 10  # ❌ Code became the answer!
```

### Solutions:

**Option 1: Run input line separately**
1. Run just the `input()` line
2. Type your answer in terminal
3. Then run the rest of the lines

**Option 2: Use the play button ▶️**
- But only if that's the only exercise in the file

**Option 3: Close and restart Python terminal**
- Click trash icon on Python terminal
- Run code fresh

---

## 🔴 Slice Returns Nothing or Wrong Characters

### Common slice mistakes:

```python
name = "Connor"

# Wrong slices
name[:0]     # ❌ Returns "" (empty) - goes from start to 0
name[0:0]    # ❌ Returns "" (empty) - start equals end
name[-3:-1]  # ⚠️ Returns "no" (only 2 chars, not 3!)

# Correct slices
name[0]      # ✅ "C" (first character)
name[0:1]    # ✅ "C" (alternative for first char)
name[0:3]    # ✅ "Con" (first 3 characters)
name[-3:]    # ✅ "nor" (last 3 characters)
name[-1]     # ✅ "r" (last character)
```

**Remember:** `[start:end]` does NOT include the end index!

---

## 🔴 AttributeError: 'str' object has no attribute 'len'

### What it means:
Using the wrong syntax for a function.

### Examples:

```python
name = "Connor"

# Wrong - len is a function, not a method
name.len()     # ❌ ERROR
len(name)      # ✅ Correct - pass string TO len()

# Wrong - forgot parentheses on method
name.upper     # ❌ Doesn't call the method
name.upper()   # ✅ Correct - parentheses needed
```

---

## 🔴 Terminal Shows Zsh: Command Not Found

### What it means:
You're typing Python code into the Zsh terminal instead of running it properly.

### Example:

```terminal
cro@Connors-MacBook-Air Python Study % wage = 26.50
zsh: command not found: wage
```

### Fix:
Don't type Python code into the terminal!

**Correct way:**
1. Write code in the `.py` file
2. Highlight the code
3. Press `Shift + Return` to run it

---

## 🔴 Code Works Once But Fails Second Time

### What it means:
Variables from previous runs are still in Python's memory.

### Example:

```python
# First run
x = 10
print(x + 5)  # ✅ Works! Prints 15

# Second run - you only run this line:
print(x + 5)  # ✅ Still works because x is in memory!

# Third run - after closing terminal:
print(x + 5)  # ❌ ERROR: x is not defined anymore
```

### Fix:
**Close the Python terminal** between exercises to clear memory:
- Click trash icon on Python terminal tab
- Run code fresh

Or make sure to run ALL the lines you need, every time.

---

## 🔴 Tuple Appears in Output Instead of Text

### Problem:
```python
first = "Connor"
last = "O'Malley"

print(f"{first, last}")  # ❌ Prints: ('Connor', "O'Malley")
```

### Fix:
```python
# Separate variables with space, not comma
print(f"{first} {last}")  # ✅ Prints: Connor O'Malley
```

**Why:** Commas inside `{}` create a tuple (a data structure), not formatted text.

---

## 🐛 Debugging Checklist

When code doesn't work, check:

1. ✅ Did I run all the necessary lines together?
2. ✅ Did I convert `input()` to the right type?
3. ✅ Are all my quotes/parentheses matched?
4. ✅ Did I spell variable names correctly?
5. ✅ Is my indentation correct?
6. ✅ Did I type my answer (not code) when prompted?
7. ✅ Do I need to close the Python terminal and start fresh?

---

## 💡 General Debugging Tips

**1. Read the error message!**
- It tells you the line number
- It tells you what went wrong
- The last line is usually most important

**2. Close Python terminal between exercises**
- Prevents variable conflicts
- Gives you a clean slate

**3. Print everything!**
```python
# Not sure what a variable contains?
print(x)
print(type(x))  # Shows if it's str, int, float, etc.
```

**4. Run code step by step**
- Run one line at a time
- See where it breaks

**5. Check the basics first**
- Typos in variable names
- Missing quotes
- Forgot to convert input to int/float

---

**Keep this handy - you'll reference it often!**
