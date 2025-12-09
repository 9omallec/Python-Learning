# Active Recall Cards: If/Else Statements

**Test yourself BEFORE looking at answers**

---

## 📝 How to Use These Cards

1. **Read the question**
2. **Try to answer from memory** (write it down or say it out loud)
3. **Check the answer**
4. **If wrong:** Review the lesson, then try again later
5. **If right:** Move to next card

---

## Card 1: Basic Syntax

**Q: Write the basic syntax for an if statement.**

<details>
<summary>Click to reveal answer</summary>

```python
if condition:
    # code to run if True
```

**Key points:**
- Colon `:` at end of if line
- Indentation (4 spaces or 1 tab)
- Condition evaluates to True or False
</details>

---

## Card 2: If/Else Syntax

**Q: Write the syntax for if/else statement.**

<details>
<summary>Click to reveal answer</summary>

```python
if condition:
    # code if True
else:
    # code if False
```

**Key points:**
- else also needs colon
- else code runs only if condition is False
- One or the other runs, never both
</details>

---

## Card 3: Comparison Operators

**Q: List all comparison operators and what they do.**

<details>
<summary>Click to reveal answer</summary>

```python
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

**Common mistake:** Using `=` instead of `==` for comparison!
</details>

---

## Card 4: Predict the Output

**Q: What will this print?**

```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `Adult`

**Why:** 20 >= 18 is True, so if block runs
</details>

---

## Card 5: Predict the Output

**Q: What will this print?**

```python
password = "python"
if password == "Python":
    print("Correct")
else:
    print("Wrong")
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `Wrong`

**Why:** Strings are case-sensitive! `"python" != "Python"`
</details>

---

## Card 6: Elif Syntax

**Q: Write the syntax for if/elif/else with 3 conditions.**

<details>
<summary>Click to reveal answer</summary>

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False and condition2 is True
else:
    # runs if both are False
```

**Key points:**
- Can have multiple elif blocks
- Checks top to bottom, stops at first True
- else is optional
</details>

---

## Card 7: Fix the Bug

**Q: What's wrong with this code?**

```python
age = 15
if age >= 18
    print("Adult")
```

<details>
<summary>Click to reveal answer</summary>

**Missing colon!**

```python
age = 15
if age >= 18:  # ← Need colon here
    print("Adult")
```
</details>

---

## Card 8: Fix the Bug

**Q: What's wrong with this code?**

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
print("B")
```

<details>
<summary>Click to reveal answer</summary>

**Missing indentation!**

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")  # ← Must be indented
```
</details>

---

## Card 9: Logic Challenge

**Q: What will this print?**

```python
x = 10
if x > 5:
    if x < 15:
        print("Between 5 and 15")
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `Between 5 and 15`

**Why:** 10 > 5 is True, then 10 < 15 is also True (nested if)
</details>

---

## Card 10: Build From Memory

**Q: Without looking, write code that:**
- Asks user for a number
- If even, print "Even"
- If odd, print "Odd"

<details>
<summary>Click to reveal answer</summary>

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Key concept:** `%` (modulo) gives remainder, even numbers have no remainder when divided by 2
</details>

---

## 🎯 Challenge Cards (Harder)

### Challenge 1: Password Validator

**Q: Build a password validator that checks:**
- Must be at least 8 characters
- If yes: "Strong password"
- If no: "Too weak"

<details>
<summary>Click to reveal answer</summary>

```python
password = input("Create password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Too weak")
```

**Key function:** `len()` returns length of string
</details>

---

### Challenge 2: Grade Calculator

**Q: Build a grade calculator:**
- 90+: A
- 80-89: B
- 70-79: C
- Below 70: F

<details>
<summary>Click to reveal answer</summary>

```python
score = int(input("Enter score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**Why order matters:** Checks stop at first True condition
</details>

---

### Challenge 3: Age Categorizer

**Q: Categorize ages:**
- 0-12: Child
- 13-19: Teen
- 20-64: Adult
- 65+: Senior

<details>
<summary>Click to reveal answer</summary>

```python
age = int(input("Enter age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
```

**Alternative:** Could also use `age >= 13 and age <= 19`
</details>

---

## 🔄 Review Schedule

**Use spaced repetition:**

- **Day 1:** Answer all cards
- **Day 2:** Review cards you got wrong
- **Day 7:** Answer all cards again (from memory)
- **Day 16:** Quick review of challenge cards
- **Day 35:** Final check - should be automatic now

---

## ✅ Self-Check

**After completing these cards, can you:**

- [ ] Write basic if statement from memory?
- [ ] Explain when to use elif vs multiple ifs?
- [ ] List all comparison operators?
- [ ] Fix common if/else errors (colon, indentation)?
- [ ] Build a simple if/else program without references?

**If YES to all:** You're ready to move on!
**If NO to any:** Review that specific card, try building something using it

---

**Remember:** Active recall is 25-40% more effective than re-reading!
