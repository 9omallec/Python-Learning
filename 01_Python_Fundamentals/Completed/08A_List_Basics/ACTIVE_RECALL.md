# Active Recall: List Basics

Test yourself! Answer these questions from memory before checking.

---

## 📝 Basic Concepts

**1. How do you create a list in Python?**
<details>
<summary>Click to reveal answer</summary>

```python
my_list = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
empty = []
```
Use square brackets `[]` with items separated by commas.
</details>

**2. What index is the first item in a list?**
<details>
<summary>Click to reveal answer</summary>

Index `0`. Python uses zero-based indexing.
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # apple
```
</details>

**3. How do you access the last item using negative indexing?**
<details>
<summary>Click to reveal answer</summary>

Use index `-1`:
```python
fruits = ["apple", "banana", "orange"]
print(fruits[-1])  # orange
```
- `-1` = last item
- `-2` = second to last
- `-3` = third to last, etc.
</details>

**4. How do you loop through all items in a list?**
<details>
<summary>Click to reveal answer</summary>

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```
Or with index:
```python
for i in range(len(fruits)):
    print(fruits[i])
```
</details>

**5. How do you check if "banana" is in a fruits list?**
<details>
<summary>Click to reveal answer</summary>

```python
if "banana" in fruits:
    print("We have bananas!")
```
Use the `in` keyword.
</details>

---

## 🔍 Functions & Methods

**6. What does len(my_list) return?**
<details>
<summary>Click to reveal answer</summary>

The number of items in the list:
```python
fruits = ["apple", "banana", "orange"]
print(len(fruits))  # 3
```
</details>

**7. How do you get the first 3 items from a list?**
<details>
<summary>Click to reveal answer</summary>

Use slicing:
```python
my_list = [0, 1, 2, 3, 4, 5]
first_three = my_list[:3]  # [0, 1, 2]
```
Syntax: `list[start:end]` (end is not included)
</details>

**8. How do you find the maximum value in a list of numbers?**
<details>
<summary>Click to reveal answer</summary>

```python
numbers = [23, 45, 12, 67, 34]
highest = max(numbers)  # 67
```
</details>

**9. How do you count how many times "apple" appears in a list?**
<details>
<summary>Click to reveal answer</summary>

```python
fruits = ["apple", "banana", "apple", "orange", "apple"]
count = fruits.count("apple")  # 3
```
</details>

**10. How do you find what index "banana" is at?**
<details>
<summary>Click to reveal answer</summary>

```python
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")  # 1
```
</details>

---

## 🎯 Practical Scenarios

**11. Write code to calculate the average of this list:**
```python
scores = [85, 92, 78, 90, 88]
```
<details>
<summary>Click to reveal answer</summary>

```python
scores = [85, 92, 78, 90, 88]
total = sum(scores)
average = total / len(scores)
print(average)  # 86.6
```
</details>

**12. Write code to get the last 3 items from a list:**
<details>
<summary>Click to reveal answer</summary>

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_three = my_list[-3:]  # [7, 8, 9]
```
</details>

**13. Write code to get every other item from a list:**
<details>
<summary>Click to reveal answer</summary>

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
every_other = numbers[::2]  # [0, 2, 4, 6, 8]
```
The third number in slicing is the step.
</details>

**14. Write code to print each name with its position number:**
```python
names = ["Alice", "Bob", "Charlie"]
# Output: "1. Alice", "2. Bob", "3. Charlie"
```
<details>
<summary>Click to reveal answer</summary>

```python
names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")
```
Or:
```python
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
```
</details>

**15. What's wrong with this code?**
```python
fruits = ["apple", "banana", "orange"]
print(fruits[3])
```
<details>
<summary>Click to reveal answer</summary>

**IndexError!** The list only has 3 items (indices 0, 1, 2).
- `fruits[0]` = "apple"
- `fruits[1]` = "banana"
- `fruits[2]` = "orange"
- `fruits[3]` = ERROR (doesn't exist)

To access the last item safely: `fruits[-1]` or `fruits[len(fruits) - 1]`
</details>

---

## 💪 Challenge Questions

**16. How would you find the range (difference between highest and lowest) of a list of numbers?**
<details>
<summary>Click to reveal answer</summary>

```python
numbers = [23, 45, 12, 67, 34]
range_value = max(numbers) - min(numbers)
print(range_value)  # 55 (67 - 12)
```
</details>

**17. How would you count how many even numbers are in a list?**
<details>
<summary>Click to reveal answer</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(even_count)  # 5
```
</details>

**18. How do you check if a list is empty?**
<details>
<summary>Click to reveal answer</summary>

```python
my_list = []

# Method 1: Check length
if len(my_list) == 0:
    print("List is empty")

# Method 2: Direct check (Pythonic way)
if not my_list:
    print("List is empty")
```
</details>

---

## 🎯 Scoring

- **15-18 correct**: Excellent! You've mastered list basics!
- **11-14 correct**: Good! Review the concepts you missed.
- **7-10 correct**: You're getting there. Practice more with BUILD_PROJECTS.md
- **Below 7**: Review lesson.py and rebuild the projects.

---

**Remember:** It's okay not to know everything! The goal is to identify what to practice more.
