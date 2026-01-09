# Active Recall Cards: For Loops

**Test yourself BEFORE looking at answers**

---

## Card 1: Basic For Loop Syntax

**Q: Write the basic syntax for a for loop using range().**

<details>
<summary>Click to reveal answer</summary>

```python
for i in range(5):
    print(i)
```

**Key points:**
- `for variable in range(number):`
- Colon at end
- Indentation for loop body
- `i` is common variable name (but can be anything)
</details>

---

## Card 2: Range Function

**Q: What does `range(5)` produce?**

<details>
<summary>Click to reveal answer</summary>

**Answer:** Numbers 0, 1, 2, 3, 4

**Key points:**
- Starts at 0 (not 1!)
- Stops BEFORE the number (not including 5)
- Produces 5 total numbers (0-4)
</details>

---

## Card 3: Range with Start and Stop

**Q: What numbers does `range(2, 7)` produce?**

<details>
<summary>Click to reveal answer</summary>

**Answer:** 2, 3, 4, 5, 6

**Key points:**
- First number = start (included)
- Second number = stop (NOT included)
- Stops at 6, not 7
</details>

---

## Card 4: Range with Step

**Q: What does `range(0, 10, 2)` produce?**

<details>
<summary>Click to reveal answer</summary>

**Answer:** 0, 2, 4, 6, 8

**Key points:**
- First: start (0)
- Second: stop (10, not included)
- Third: step size (jump by 2)
- All even numbers from 0-8
</details>

---

## Card 5: Counting Backwards

**Q: How do you count from 10 down to 1 using range()?**

<details>
<summary>Click to reveal answer</summary>

```python
for i in range(10, 0, -1):
    print(i)
```

**Key points:**
- Start: 10
- Stop: 0 (not included, so stops at 1)
- Step: -1 (negative means backwards)
</details>

---

## Card 6: Predict the Output

**Q: What will this print?**

```python
for i in range(3):
    print("Hello")
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
Hello
Hello
Hello
```

**Why:** Repeats 3 times, doesn't use `i` value
</details>

---

## Card 7: Predict the Output

**Q: What will this print?**

```python
for num in range(1, 4):
    print(num * 2)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
2
4
6
```

**Why:** range(1, 4) gives 1,2,3; each multiplied by 2
</details>

---

## Card 8: Fix the Bug

**Q: What's wrong with this code?**

```python
for i in range(5)
    print(i)
```

<details>
<summary>Click to reveal answer</summary>

**Missing colon!**

```python
for i in range(5):  # ← Need colon
    print(i)
```
</details>

---

## Card 9: Fix the Bug

**Q: What's wrong with this code?**

```python
for i in range(3):
print(i)
```

<details>
<summary>Click to reveal answer</summary>

**Missing indentation!**

```python
for i in range(3):
    print(i)  # ← Must be indented
```
</details>

---

## Card 10: Build From Memory

**Q: Without looking, write code that prints numbers 1 to 10.**

<details>
<summary>Click to reveal answer</summary>

```python
for i in range(1, 11):
    print(i)
```

**Common mistake:** `range(1, 10)` only goes to 9!
**Remember:** Stop number is NOT included
</details>

---

## 🎯 Challenge Cards

### Challenge 1: Sum Calculator

**Q: Write code that adds up all numbers from 1 to 100.**

<details>
<summary>Click to reveal answer</summary>

```python
total = 0
for i in range(1, 101):
    total = total + i
print(total)

# Alternative shorter version:
# total += i
```

**Result:** 5050
</details>

---

### Challenge 2: Multiplication Table

**Q: Print the 7 times table from 7×1 to 7×10.**

<details>
<summary>Click to reveal answer</summary>

```python
for i in range(1, 11):
    print(f"7 × {i} = {7 * i}")
```

**Output:** 7×1=7, 7×2=14, etc.
</details>

---

### Challenge 3: Even Numbers

**Q: Print only even numbers from 0 to 20.**

<details>
<summary>Click to reveal answer</summary>

**Method 1: Using step**
```python
for i in range(0, 21, 2):
    print(i)
```

**Method 2: Using if**
```python
for i in range(21):
    if i % 2 == 0:
        print(i)
```

**Both work!** Method 1 is more efficient
</details>

---

## 🔄 Review Schedule

- **Day 1:** Complete all cards
- **Day 2:** Review wrong answers
- **Day 7:** Redo all cards from memory
- **Day 16:** Focus on challenge cards
- **Day 35:** Should feel automatic

---

## ✅ Self-Check

**Can you:**

- [ ] Write basic for loop from memory?
- [ ] Explain how range() works?
- [ ] Use range with start, stop, and step?
- [ ] Count backwards with range?
- [ ] Fix common loop errors (colon, indentation)?
- [ ] Build a loop that sums numbers?

**All YES?** Ready to move on!
**Any NO?** Practice that specific skill!

---

**Remember:** Building is better than reading!
