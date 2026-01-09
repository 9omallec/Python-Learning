# Active Recall Cards: User Input

**Test yourself BEFORE looking at answers**

---

## Card 1: Basic Input

**Q: Write code that asks for a user's name and prints it**

<details>
<summary>Click to reveal answer</summary>

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

**Key points:**
- `input()` gets text from user
- Always returns a string (text)
- Store result in a variable
- Prompt message goes inside quotes
</details>

---

## Card 2: Input Type

**Q: What type does input() return?**

```python
age = input("Enter your age: ")
```

<details>
<summary>Click to reveal answer</summary>

**Answer:** String (text) - ALWAYS!

Even if user types a number, input() returns it as text.

```python
age = input("Enter your age: ")  # User types: 25
print(type(age))  # Output: <class 'str'>
```

**You must convert it to use as a number!**
</details>

---

## Card 3: Type Conversion

**Q: Fix this code so math works:**

```python
age = input("Enter your age: ")
next_year = age + 1  # This causes an error!
```

<details>
<summary>Click to reveal answer</summary>

**Fixed:**
```python
age = input("Enter your age: ")
age = int(age)  # Convert string to integer
next_year = age + 1
print(f"Next year you'll be {next_year}")
```

**Or in one line:**
```python
age = int(input("Enter your age: "))
next_year = age + 1
```

**Remember:** Can't do math with strings!
</details>

---

## Card 4: Int vs Float

**Q: When should you use int() vs float()?**

<details>
<summary>Click to reveal answer</summary>

**Use int() for whole numbers:**
```python
age = int(input("Enter your age: "))  # 25, 30, 42
people = int(input("How many people? "))  # 3, 10, 1
```

**Use float() for decimals:**
```python
price = float(input("Enter price: "))  # 19.99, 5.50
height = float(input("Enter height in meters: "))  # 1.75, 1.82
```

**Rule:** If it can have decimals, use float()
</details>

---

## Card 5: Predict Output

**Q: What happens if user enters "hello" here?**

```python
number = int(input("Enter a number: "))
```

<details>
<summary>Click to reveal answer</summary>

**Error:** `ValueError: invalid literal for int() with base 10: 'hello'`

**Why:** Can't convert "hello" to an integer!

**Safe version (we'll learn this later):**
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```
</details>

---

## Card 6: Multiple Inputs

**Q: Get name and age from user, print both**

<details>
<summary>Click to reveal answer</summary>

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hi {name}, you are {age} years old!")
```

**Key points:**
- Each input() gets one piece of information
- Store each in its own variable
- Convert age to int for calculations
</details>

---

## Card 7: Fix the Bug

**Q: What's wrong with this code?**

```python
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
total = number1 + number2
print(total)
```

**User enters: 5 and 3**
**It prints: 53 (not 8!)**

<details>
<summary>Click to reveal answer</summary>

**Problem:** Adding strings, not numbers!

**Fixed:**
```python
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
total = number1 + number2
print(total)  # Now prints 8
```

**Remember:** Convert to int() or float() before math!
</details>

---

## Card 8: Build From Memory

**Q: Create an interactive calculator that:**
- Asks for two numbers
- Asks for operation (+, -, *, /)
- Prints the result

<details>
<summary>Click to reveal answer</summary>

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(f"Result: {result}")
```

**Simpler version:**
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
```
</details>

---

## Card 9: String Input

**Q: What will this print if user enters "python"?**

```python
word = input("Enter a word: ")
print(word.upper())
print(word)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
PYTHON
python
```

**Why:**
- `.upper()` creates a NEW uppercase string
- Original variable `word` is unchanged
- If you want to keep it: `word = word.upper()`
</details>

---

## Card 10: Interactive Program

**Q: Write a program that asks for radius and calculates circle area**

<details>
<summary>Click to reveal answer</summary>

```python
radius = float(input("Enter circle radius: "))
pi = 3.14159
area = pi * radius ** 2

print(f"A circle with radius {radius} has area {area}")
```

**Example interaction:**
```
Enter circle radius: 5
A circle with radius 5.0 has area 78.53975
```
</details>

---

## Challenge Cards

### Challenge 1: Mad Libs

**Q: Create a mad libs story that asks for:**
- A name
- An adjective
- A place
- An animal

Then prints a silly story using those words.

<details>
<summary>Click to reveal answer</summary>

```python
name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

print(f"\n--- STORY ---")
print(f"Once upon a time, {name} went to {place}.")
print(f"There they met a {adjective} {animal}!")
print(f"They became best friends and lived happily ever after.")
```
</details>

---

### Challenge 2: Tip Calculator

**Q: Create interactive tip calculator:**
- Ask for bill amount
- Ask for tip percentage
- Calculate and display tip and total

<details>
<summary>Click to reveal answer</summary>

```python
bill = float(input("Enter bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * (tip_percent / 100)
total = bill + tip

print(f"\n--- RECEIPT ---")
print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
```

**Note:** `.2f` formats to 2 decimal places
</details>

---

### Challenge 3: Age in Days

**Q: Ask for user's age in years, calculate and show:**
- Age in months
- Age in days
- Age in hours

<details>
<summary>Click to reveal answer</summary>

```python
age_years = int(input("Enter your age in years: "))

age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24

print(f"\nYou are approximately:")
print(f"- {age_months} months old")
print(f"- {age_days} days old")
print(f"- {age_hours} hours old!")
```
</details>

---

## Self-Check

**Can you:**
- [ ] Use input() to get user input?
- [ ] Store input in variables?
- [ ] Convert strings to numbers with int() and float()?
- [ ] Know when to use int() vs float()?
- [ ] Get multiple inputs from user?
- [ ] Create interactive programs?
- [ ] Understand that input() always returns strings?

**All YES?** You've mastered user input!
