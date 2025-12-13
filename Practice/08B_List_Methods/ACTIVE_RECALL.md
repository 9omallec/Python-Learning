# Active Recall: List Methods

Test yourself! Answer from memory before checking.

---

## 📝 Adding Items

**1. How do you add an item to the end of a list?**
<details>
<summary>Answer</summary>

```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']
```
Use `.append(item)`
</details>

**2. How do you insert an item at a specific position?**
<details>
<summary>Answer</summary>

```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  # ['apple', 'orange', 'banana']
```
Use `.insert(index, item)`
</details>

**3. How do you add multiple items from another list?**
<details>
<summary>Answer</summary>

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
```
Use `.extend(other_list)` or `list1 = list1 + list2`
</details>

---

## 🗑️ Removing Items

**4. How do you remove a specific value from a list?**
<details>
<summary>Answer</summary>

```python
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)  # ['apple', 'orange']
```
Use `.remove(value)` - removes first occurrence
</details>

**5. How do you remove and return the last item?**
<details>
<summary>Answer</summary>

```python
numbers = [1, 2, 3, 4, 5]
last = numbers.pop()
print(last)     # 5
print(numbers)  # [1, 2, 3, 4]
```
Use `.pop()` with no arguments
</details>

**6. How do you remove an item at a specific index?**
<details>
<summary>Answer</summary>

```python
numbers = [10, 20, 30, 40]
removed = numbers.pop(1)  # Remove at index 1
print(removed)  # 20
print(numbers)  # [10, 30, 40]
```
Use `.pop(index)` or `del numbers[index]`
</details>

**7. How do you remove all items from a list?**
<details>
<summary>Answer</summary>

```python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # []
```
Use `.clear()`
</details>

---

## 🔄 Sorting & Reversing

**8. How do you sort a list in place?**
<details>
<summary>Answer</summary>

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]
```
Use `.sort()` - modifies the original list
</details>

**9. How do you sort in descending order?**
<details>
<summary>Answer</summary>

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]
```
Use `.sort(reverse=True)`
</details>

**10. What's the difference between sort() and sorted()?**
<details>
<summary>Answer</summary>

```python
original = [3, 1, 4, 1, 5]

# sort() - modifies original, returns None
original.sort()
print(original)  # [1, 1, 3, 4, 5]

# sorted() - returns new list, original unchanged
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
print(original)  # [3, 1, 4, 1, 5] (unchanged)
print(new_list)  # [1, 1, 3, 4, 5]
```
</details>

**11. How do you reverse a list?**
<details>
<summary>Answer</summary>

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```
Use `.reverse()` - modifies in place
</details>

---

## 📋 Copying Lists

**12. What's wrong with this code?**
```python
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
```
<details>
<summary>Answer</summary>

This doesn't create a copy! Both variables point to the same list.
```python
list1 = [1, 2, 3]
list2 = list1  # NOT a copy!
list2.append(4)
print(list1)  # [1, 2, 3, 4] - BOTH changed!
```

**Correct way:**
```python
list1 = [1, 2, 3]
list2 = list1.copy()  # Real copy
list2.append(4)
print(list1)  # [1, 2, 3] - Original unchanged
```
</details>

**13. Name two ways to copy a list properly:**
<details>
<summary>Answer</summary>

```python
original = [1, 2, 3]

# Method 1: .copy()
copy1 = original.copy()

# Method 2: slicing
copy2 = original[:]

# Method 3: list() constructor
copy3 = list(original)
```
</details>

---

## 🎯 Practical Scenarios

**14. Write code to build a list from 5 user inputs:**
<details>
<summary>Answer</summary>

```python
my_list = []
for i in range(5):
    item = input(f"Enter item {i + 1}: ")
    my_list.append(item)
print(my_list)
```
</details>

**15. Write code to remove duplicates from a list:**
<details>
<summary>Answer</summary>

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5]
```
Note: Order may not be preserved with set()
</details>

**16. Write code to get only even numbers from a list:**
<details>
<summary>Answer</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # [2, 4, 6, 8, 10]
```
</details>

**17. What happens if you try to remove an item that doesn't exist?**
```python
fruits = ["apple", "banana"]
fruits.remove("orange")
```
<details>
<summary>Answer</summary>

**ValueError!** The item must exist in the list.

**Safe approach:**
```python
if "orange" in fruits:
    fruits.remove("orange")
else:
    print("Item not found")
```
</details>

**18. How would you swap two items in a list?**
```python
# Swap items at index 0 and 2
my_list = ["a", "b", "c", "d"]
```
<details>
<summary>Answer</summary>

```python
my_list = ["a", "b", "c", "d"]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)  # ['c', 'b', 'a', 'd']
```
Python allows tuple unpacking for elegant swaps!
</details>

---

## 🎯 Scoring

- **15-18 correct**: Master! You know list methods cold!
- **11-14 correct**: Great! Just a few more concepts to nail down.
- **7-10 correct**: Getting there. Practice with BUILD_PROJECTS.md
- **Below 7**: Review lesson.py and rebuild projects.

---

**Key Takeaway:** Understanding which methods modify the list vs. return new values is crucial!
