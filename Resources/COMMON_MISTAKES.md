# Common Mistakes to Watch For

These are patterns I've noticed in your learning. Review this before starting new exercises!

---

## Range() Mistakes

### ❌ Using minus instead of comma
```python
for i in range(1-10):  # This calculates 1 - 10 = -9
```

### ✅ Correct way
```python
for i in range(1, 10)  # From 1 to 9 (stops before 10)
```

---

## Off-by-One Errors

### ❌ Forgetting range stops BEFORE the end
```python
for i in range(1, 10):  # Prints 1-9, not 1-10!
```

### ✅ Remember: Add 1 to include the last number
```python
for i in range(1, 11):  # Prints 1-10
```

---

## Variable vs String

### ❌ Printing the word instead of the variable
```python
i = 5
print("i")  # Prints: i
```

### ✅ Print the variable (no quotes)
```python
i = 5
print(i)  # Prints: 5
```

---

## Extra Parentheses

### ❌ Unnecessary parentheses around strings/numbers
```python
name = ("Connor")  # Works, but unnecessary
age = (35)
```

### ✅ Just use quotes for strings, nothing for numbers
```python
name = "Connor"
age = 35
```

---

## Modifying Loop Variables

### ❌ Changing the loop variable inside the loop
```python
for i in range(0, 5):
    i += 1  # Don't do this!
    print(i)
```

### ✅ Start the range where you need it
```python
for i in range(1, 6):
    print(i)
```

---

## Type Conversion

### ❌ Forgetting to convert input to int/float
```python
age = input("Age: ")  # This is a string!
next_year = age + 1   # Error!
```

### ✅ Convert when you need a number
```python
age = int(input("Age: "))
next_year = age + 1  # Works!
```

---

## Input vs Print

### ❌ Using print() when you need input()
```python
license = print("Do you have a license? ")  # Wrong function!
```

### ✅ Use input() to get user input
```python
license = input("Do you have a license? ")
```

---

## Extra Spaces

### ❌ Adding spaces at the end of strings
```python
print("Hello. ")  # Space after period
```

### ✅ Only add spaces where needed
```python
print("Hello.")  # Clean!
print("Hello", name)  # Space automatically added between
```

---

## Quick Reference: When to Use What

**int()** - Whole numbers: age, count, year
**float()** - Decimals: price, temperature, measurements
**str()** - Text: names, words, anything with letters

**input()** - Get information FROM the user
**print()** - Show information TO the user

**= (one equal)** - Assign a value to a variable
**== (two equals)** - Check if two things are equal

---

## Tips to Avoid These Mistakes

1. **Read error messages carefully** - They tell you what's wrong!
2. **Test with simple values first** - Use small numbers to verify logic
3. **Run your code often** - Don't write 10 lines before testing
4. **Print variables to debug** - Add `print(variable)` to see what's inside
5. **Double-check your range()** - Most common mistake!

---

**Remember:** Everyone makes these mistakes! They're part of learning. The key is recognizing the patterns so you catch them faster next time.
