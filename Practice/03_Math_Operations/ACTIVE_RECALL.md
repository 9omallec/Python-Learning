# Active Recall Cards: Math Operations

**Test yourself BEFORE looking at answers**

---

## Card 1: Basic Operators

**Q: What will each of these print?**

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
```

<details>
<summary>Click to reveal answer</summary>

```
15
5
50
2.0
```

**Key points:**
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division (always gives decimal)
</details>

---

## Card 2: Integer Division

**Q: What's the difference?**

```python
print(17 / 5)
print(17 // 5)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
3.4
3
```

**Difference:**
- `/` = regular division (gives decimal)
- `//` = floor division (gives whole number, rounds down)

**Use `//` when you only want the whole number!**
</details>

---

## Card 3: Modulo Operator

**Q: What will this print?**

```python
print(17 % 5)
print(20 % 4)
print(15 % 3)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
2
0
0
```

**Why:**
- `17 % 5` = remainder when 17 is divided by 5 (17 = 3*5 + 2)
- `20 % 4` = 0 (divides evenly, no remainder)
- `15 % 3` = 0 (divides evenly)

**Use `%` to find remainders!**
</details>

---

## Card 4: Exponents

**Q: How do you calculate 2 to the power of 5?**

<details>
<summary>Click to reveal answer</summary>

```python
print(2 ** 5)  # Output: 32
```

**Key points:**
- `**` is the exponent operator
- `2 ** 5` means 2 × 2 × 2 × 2 × 2
- Not `^` (that's different in Python!)

**Examples:**
```python
print(3 ** 2)   # 9 (3 squared)
print(10 ** 3)  # 1000 (10 cubed)
print(5 ** 0)   # 1 (anything to power 0 is 1)
```
</details>

---

## Card 5: Order of Operations

**Q: What will this print?**

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
14
20
```

**Why:**
- First: `2 + 3 * 4` → multiplication first → `2 + 12` = 14
- Second: `(2 + 3) * 4` → parentheses first → `5 * 4` = 20

**Remember PEMDAS:**
- **P**arentheses
- **E**xponents
- **M**ultiplication/**D**ivision (left to right)
- **A**ddition/**S**ubtraction (left to right)
</details>

---

## Card 6: Fix the Bug

**Q: What's wrong with this code?**

```python
result = 10 / 0
print(result)
```

<details>
<summary>Click to reveal answer</summary>

**Error:** `ZeroDivisionError: division by zero`

**Can't divide by zero!** This is a mathematical impossibility.

**Fix:** Check before dividing
```python
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    print("Can't divide by zero!")
```
</details>

---

## Card 7: Predict Output

**Q: What will this print?**

```python
x = 10
x = x + 5
x = x * 2
print(x)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `30`

**Step by step:**
- Start: x = 10
- After x = x + 5: x = 15
- After x = x * 2: x = 30
</details>

---

## Card 8: Compound Operators

**Q: Rewrite using compound operators**

```python
score = 100
score = score + 10
score = score - 5
score = score * 2
score = score / 5
```

<details>
<summary>Click to reveal answer</summary>

```python
score = 100
score += 10   # Same as score = score + 10
score -= 5    # Same as score = score - 5
score *= 2    # Same as score = score * 2
score /= 5    # Same as score = score / 5
```

**Final value:** `42.0`
</details>

---

## Card 9: Build From Memory

**Q: Write a program that calculates the area of a circle (area = π × r²)**

Use radius = 5, and π = 3.14159

<details>
<summary>Click to reveal answer</summary>

```python
pi = 3.14159
radius = 5
area = pi * radius ** 2

print(f"Area: {area}")  # Output: Area: 78.53975
```

**Or more detailed:**
```python
pi = 3.14159
radius = 5
area = pi * (radius ** 2)

print(f"Circle with radius {radius}")
print(f"Area: {area}")
```
</details>

---

## Card 10: Mixed Operations

**Q: What will this print?**

```python
print(10 + 5 * 2 ** 2 - 8 / 4)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `28.0`

**Step by step (PEMDAS):**
1. Exponents: `2 ** 2` = 4
2. Multiplication/Division (left to right): `5 * 4` = 20, `8 / 4` = 2.0
3. Addition/Subtraction (left to right): `10 + 20` = 30, `30 - 2.0` = 28.0
</details>

---

## Challenge Cards

### Challenge 1: Temperature Converter

**Q: Convert Celsius to Fahrenheit**

Formula: F = (C × 9/5) + 32

Convert 25°C to Fahrenheit

<details>
<summary>Click to reveal answer</summary>

```python
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")  # Output: 25°C = 77.0°F
```

**Full program:**
```python
# Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit to Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius}°C")
```
</details>

---

### Challenge 2: Compound Interest

**Q: Calculate compound interest**

- Principal: $1000
- Rate: 5% per year
- Time: 3 years
- Formula: A = P(1 + r)^t

<details>
<summary>Click to reveal answer</summary>

```python
principal = 1000
rate = 0.05  # 5% as decimal
time = 3

amount = principal * (1 + rate) ** time
interest = amount - principal

print(f"Starting amount: ${principal}")
print(f"After {time} years: ${amount}")
print(f"Interest earned: ${interest}")
```

**Output:**
```
Starting amount: $1000
After 3 years: $1157.625
Interest earned: $157.625
```
</details>

---

### Challenge 3: Even or Odd

**Q: Use modulo to check if a number is even or odd**

<details>
<summary>Click to reveal answer</summary>

```python
number = 17

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

**Why it works:**
- Even numbers: divisible by 2, remainder is 0
- Odd numbers: not divisible by 2, remainder is 1
</details>

---

## Self-Check

**Can you:**
- [ ] Use all math operators (+, -, *, /, //, %, **)?
- [ ] Explain the difference between / and //?
- [ ] Use % to find remainders?
- [ ] Calculate exponents with **?
- [ ] Apply order of operations correctly?
- [ ] Use parentheses to control order?
- [ ] Use compound operators (+=, -=, etc.)?

**All YES?** You've mastered math operations!
