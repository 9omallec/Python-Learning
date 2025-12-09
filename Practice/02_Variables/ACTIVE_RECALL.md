# Active Recall Cards: Variables

**Test yourself BEFORE looking at answers**

---

## Card 1: Creating Variables

**Q: Write code that stores your name in a variable and prints it**

<details>
<summary>Click to reveal answer</summary>

```python
name = "Connor"
print(name)
```

**Key points:**
- Variable name on left
- `=` assigns value
- Value on right
- No quotes around variable name when using it
</details>

---

## Card 2: Variable Types

**Q: What type is each variable?**

```python
age = 35
price = 19.99
name = "Connor"
is_active = True
```

<details>
<summary>Click to reveal answer</summary>

- `age = 35` → int (integer/whole number)
- `price = 19.99` → float (decimal number)
- `name = "Connor"` → str (string/text)
- `is_active = True` → bool (boolean True/False)
</details>

---

## Card 3: Using Variables

**Q: What will this print?**

```python
x = 10
y = 5
print(x + y)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `15`

**Why:** Variables hold values, so it's like printing 10 + 5
</details>

---

## Card 4: Updating Variables

**Q: What's the final value of count?**

```python
count = 0
count = count + 1
count = count + 1
print(count)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `2`

**Why:**
- Starts at 0
- First addition: 0 + 1 = 1
- Second addition: 1 + 1 = 2
</details>

---

## Card 5: Shorthand Operators

**Q: Rewrite using +=**

```python
score = 10
score = score + 5
```

<details>
<summary>Click to reveal answer</summary>

```python
score = 10
score += 5  # Same as score = score + 5
```

**Other shortcuts:**
- `score -= 5` (subtract)
- `score *= 2` (multiply)
- `score /= 2` (divide)
</details>

---

## Card 6: Variable Naming

**Q: Which variable names are valid?**

```python
user_name = "Connor"
userName = "Connor"
user-name = "Connor"
2user = "Connor"
user2 = "Connor"
```

<details>
<summary>Click to reveal answer</summary>

**Valid:**
- `user_name` ✓ (Python style - use this!)
- `userName` ✓ (works but not Python style)
- `user2` ✓

**Invalid:**
- `user-name` ✗ (can't use hyphens)
- `2user` ✗ (can't start with number)
</details>

---

## Card 7: Fix the Bug

**Q: What's wrong?**

```python
name = Connor
print(name)
```

<details>
<summary>Click to reveal answer</summary>

**Missing quotes!**

```python
name = "Connor"  # Text needs quotes
print(name)
```

**Without quotes, Python thinks Connor is a variable**
</details>

---

## Card 8: Predict Output

**Q: What will this print?**

```python
x = 5
x = 10
print(x)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `10`

**Why:** The second assignment REPLACES the first value
</details>

---

## Card 9: F-Strings

**Q: Print "I am 35 years old" using a variable**

```python
age = 35
```

<details>
<summary>Click to reveal answer</summary>

```python
age = 35
print(f"I am {age} years old")
```

**Key points:**
- `f` before the quotes
- Variable in curly braces `{age}`
- This is an f-string!
</details>

---

## Card 10: Build From Memory

**Q: Without looking, create 3 variables (name, age, city) and print them in a sentence**

<details>
<summary>Click to reveal answer</summary>

```python
name = "Connor"
age = 35
city = "New York"

print(f"My name is {name}, I'm {age} years old, and I live in {city}.")
```

**Or without f-strings:**
```python
print("My name is", name, ", I'm", age, "years old, and I live in", city)
```
</details>

---

## 🎯 Challenge Cards

### Challenge 1: Swap Variables

**Q: Swap values of two variables**

```python
a = 10
b = 20
# After swap: a should be 20, b should be 10
```

<details>
<summary>Click to reveal answer</summary>

```python
a = 10
b = 20

temp = a  # Store a in temporary variable
a = b     # Put b's value in a
b = temp  # Put old a value in b

print(a)  # 20
print(b)  # 10
```

**Python shortcut:**
```python
a, b = b, a  # Swap in one line!
```
</details>

---

### Challenge 2: Calculate Total

**Q: Use variables to calculate restaurant bill**
- Food: $25.50
- Tax: 8%
- Tip: 20%
- Calculate total

<details>
<summary>Click to reveal answer</summary>

```python
food = 25.50
tax = food * 0.08
tip = food * 0.20
total = food + tax + tip

print(f"Total: ${total}")
```

**Or in one calculation:**
```python
food = 25.50
total = food * 1.28  # 100% + 8% + 20% = 128%
```
</details>

---

## ✅ Self-Check

**Can you:**
- [ ] Create variables with =?
- [ ] Use variables in calculations?
- [ ] Update variables with += and similar?
- [ ] Use f-strings to print variables?
- [ ] Name variables correctly (snake_case)?
- [ ] Know the difference between int, float, str, bool?

**All YES?** You've got variables!
