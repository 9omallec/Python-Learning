# Lesson 4: User Input (Build-First Approach)

**Total time: 60 minutes**

---

## What You'll Learn

By the end of this lesson, you'll be able to:
- Get input from users
- Convert input to numbers for calculations
- Build interactive programs
- Create real conversations with your code

**Most importantly:** You'll BUILD 4-5 interactive programs today!

---

## The Build-First Method

**DON'T:**
- Read about input() for 30 minutes
- Memorize type conversion functions
- Do non-interactive exercises

**DO:**
- Learn input() basics (5 min)
- Build interactive program immediately (15 min)
- Learn type conversion as needed
- Build more interactive projects!

---

## Step 1: Micro-Lesson (5 minutes)

### Getting User Input:

**Basic input:**
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

**Important:** input() ALWAYS returns text (string)

**For numbers, convert:**
```python
age = int(input("How old are you? "))  # Convert to integer
price = float(input("Enter price: "))  # Convert to decimal
```

**That's enough to start!** Close this file and build your first interactive program.

---

## Step 2: Build Your First Project (15 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Personal Info Collector

**Rules:**
- Close this guide
- Build from scratch
- Test with different inputs
- Struggle 10 min if stuck, then look up syntax

**GO MAKE IT INTERACTIVE NOW!**

---

## Step 3: Learn More (As Needed)

**Come back here ONLY if stuck after trying for 10+ minutes**

### Type Conversion:

**Why convert?**
```python
# Without conversion - WRONG!
age = input("Age: ")  # User types: 25
next = age + 1  # ERROR! Can't add string and number

# With conversion - RIGHT!
age = int(input("Age: "))  # Converts "25" to 25
next = age + 1  # Works! 25 + 1 = 26
```

**int() vs float():**
```python
# int() for whole numbers
age = int(input("Age: "))          # 25, 30, 42
people = int(input("How many? "))  # 1, 5, 10

# float() for decimals
price = float(input("Price: "))    # 19.99, 5.50
height = float(input("Height: "))  # 1.75, 1.82
```

### Multiple Inputs:

```python
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print(f"{name} is {age} years old and lives in {city}")
```

### Input with Calculation:

```python
radius = float(input("Enter radius: "))
area = 3.14159 * radius ** 2
print(f"Area: {area}")
```

### Common Errors:

```python
# WRONG - Forgetting to convert
age = input("Age: ")
print(age + 1)  # Error!

# RIGHT - Convert to int
age = int(input("Age: "))
print(age + 1)  # Works!

# WRONG - Using int for decimals
price = int(input("Price: "))  # User enters 19.99 - Error!

# RIGHT - Use float for decimals
price = float(input("Price: "))  # Works!
```

**Now go back to building!**

---

## Step 4: Build More Projects (40 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 3 of these:**
- Project 2: Interactive Calculator (20 min)
- Project 3: Bill Splitter (20 min)
- Project 4: Temperature Converter (15 min)
- Project 5: Quiz Game (20 min)

**Goal:** Have 4 interactive programs by end of lesson

**Test each program multiple times with different inputs!**

---

## Step 5: Active Recall (10 minutes)

**Open:** [ACTIVE_RECALL.md](ACTIVE_RECALL.md)

**Test yourself:**
- Answer cards WITHOUT looking first
- Focus on type conversion
- Practice int() vs float()

**This is crucial for retention!**

---

## Step 6: Practice Exercises (Optional)

**If you have extra time:**

**Open:** [practice.py](practice.py)

**Do:** As many exercises as you want (max 20 min)

**Priority:** Interactive projects > static exercises

---

## Lesson Complete When:

- [ ] Built at least 4 interactive programs
- [ ] Completed Active Recall cards
- [ ] Understand input() returns strings
- [ ] Can convert strings to int/float
- [ ] Know when to use int() vs float()
- [ ] Programs actually interact with users!

**Time invested:** 60-75 minutes
**Projects built:** 4-5 interactive programs
**Concepts mastered:** input(), type conversion, interactive programs

---

## Review Schedule

**Follow spaced repetition:**

- **Day 2:** Test your programs with unusual inputs
- **Day 8:** Build a new interactive calculator from memory
- **Day 17:** Combine input with string manipulation
- **Day 36:** Quick review - should feel natural now

---

## Real-World Applications

**You now know how to build:**
- Interactive calculators (any calculation + user input)
- Quiz and game systems
- Data collectors and forms
- Converters and tools
- Customer-facing applications

**Every app you use gets input from users. You can now do that!**

---

## Next Steps

**You're ready for Lesson 5 when:**
- Built 4+ interactive programs
- Comfortable with input() and type conversion
- Programs work reliably with user input
- Ready to manipulate and format text

**Move to:** [Practice/05_Strings/LESSON_GUIDE.md](../05_Strings/LESSON_GUIDE.md)

---

## Quick Reference

### Getting Input:
```python
# Text input
name = input("Prompt message: ")

# Number input
age = int(input("Enter age: "))         # Whole numbers
price = float(input("Enter price: "))   # Decimals
```

### Type Conversion:
```python
int()     # Convert to integer (whole number)
float()   # Convert to float (decimal)
str()     # Convert to string (text)
```

### Common Pattern:
```python
# Get input
value = float(input("Enter value: "))

# Do calculation
result = value * 1.08

# Show result
print(f"Result: {result}")
```

---

## Tips for Success

**DO:**
- ✅ Test with different inputs
- ✅ Convert before doing math
- ✅ Use clear prompts ("Enter age: " not just "Age")
- ✅ Use float() for money and measurements
- ✅ Make programs conversational

**DON'T:**
- ❌ Forget to convert strings to numbers
- ❌ Use int() for decimal values
- ❌ Skip testing your programs
- ❌ Make prompts confusing
- ❌ Assume input is always valid (we'll handle errors later)

---

## Debugging Tips

**Program not working?**

1. **Print the type:**
   ```python
   value = input("Number: ")
   print(type(value))  # Check if it's a string
   ```

2. **Test conversions:**
   ```python
   print(int("25"))    # Works
   print(int("25.5"))  # Error! Use float()
   print(int("hello")) # Error! Can't convert text
   ```

3. **Print intermediate values:**
   ```python
   num = int(input("Enter number: "))
   print(f"You entered: {num}, type: {type(num)}")
   ```

---

**Remember:** Interactive programs are WAY more interesting than static ones!

**Stop reading. Start asking questions. Build now!**
