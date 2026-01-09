# Active Recall: List Comprehensions (OPTIONAL)

---

## 📝 Basic Syntax

**1. Convert this loop to a list comprehension:**
```python
squares = []
for x in range(5):
    squares.append(x ** 2)
```
<details>
<summary>Answer</summary>

```python
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]
```
</details>

**2. Convert this loop to a list comprehension:**
```python
doubles = []
for n in [1, 2, 3, 4, 5]:
    doubles.append(n * 2)
```
<details>
<summary>Answer</summary>

```python
doubles = [n * 2 for n in [1, 2, 3, 4, 5]]
# [2, 4, 6, 8, 10]
```
</details>

---

## 🔍 With Conditions

**3. Get only even numbers from 1-10 using list comprehension:**
<details>
<summary>Answer</summary>

```python
evens = [n for n in range(1, 11) if n % 2 == 0]
# [2, 4, 6, 8, 10]
```
</details>

**4. Get only words longer than 3 letters:**
```python
words = ["cat", "elephant", "dog", "ant"]
```
<details>
<summary>Answer</summary>

```python
long_words = [word for word in words if len(word) > 3]
# ['elephant']
```
</details>

---

## 🎯 Practical Uses

**5. Convert all strings to uppercase:**
```python
names = ["alice", "bob", "charlie"]
```
<details>
<summary>Answer</summary>

```python
upper = [name.upper() for name in names]
# ['ALICE', 'BOB', 'CHARLIE']
```
</details>

**6. Get lengths of all words:**
```python
words = ["hello", "world", "python"]
```
<details>
<summary>Answer</summary>

```python
lengths = [len(word) for word in words]
# [5, 5, 6]
```
</details>

**7. Convert Celsius to Fahrenheit:**
```python
celsius = [0, 10, 20, 30]
# Formula: F = C * 9/5 + 32
```
<details>
<summary>Answer</summary>

```python
fahrenheit = [c * 9/5 + 32 for c in celsius]
# [32.0, 50.0, 68.0, 86.0]
```
</details>

---

## 💪 With If-Else

**8. Label numbers as "even" or "odd":**
```python
numbers = [1, 2, 3, 4, 5]
```
<details>
<summary>Answer</summary>

```python
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']
```
</details>

**9. Cap all values at 100:**
```python
values = [85, 120, 95, 110, 75]
```
<details>
<summary>Answer</summary>

```python
capped = [v if v <= 100 else 100 for v in values]
# [85, 100, 95, 100, 75]
```
</details>

---

## 🎯 When to Use

**10. Should you use a comprehension for this?**
```python
result = [x**2 if x % 2 == 0 else x**3 if x % 3 == 0 else x*2 if x % 5 == 0 else x for x in range(50) if x % 7 != 0]
```
<details>
<summary>Answer</summary>

**NO!** This is way too complex. Use a regular loop:
```python
result = []
for x in range(50):
    if x % 7 == 0:
        continue
    if x % 2 == 0:
        result.append(x ** 2)
    elif x % 3 == 0:
        result.append(x ** 3)
    elif x % 5 == 0:
        result.append(x * 2)
    else:
        result.append(x)
```

**Rule:** If the comprehension is hard to read, use a loop!
</details>

---

**Remember:** List comprehensions are optional! They're a shortcut, not a requirement. Use them when they make code clearer, not just shorter.
