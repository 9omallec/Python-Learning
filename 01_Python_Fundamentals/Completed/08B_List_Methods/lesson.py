# ===================================
# LESSON 8B: List Methods
# ===================================

# Now that you can create and access lists,
# let's learn how to MODIFY them!

# ===================================
# ADDING ITEMS TO A LIST
# ===================================

# append() - Add to the end
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# insert() - Add at specific position
fruits.insert(1, "mango")  # Insert at index 1
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# extend() - Add multiple items
more_fruits = ["grape", "kiwi"]
fruits.extend(more_fruits)
print(fruits)  # ['apple', 'mango', 'banana', 'orange', 'grape', 'kiwi']

# ===================================
# REMOVING ITEMS FROM A LIST
# ===================================

numbers = [10, 20, 30, 40, 50]

# remove() - Remove by value (first occurrence)
numbers.remove(30)
print(numbers)  # [10, 20, 40, 50]

# pop() - Remove and return last item
last = numbers.pop()
print(last)     # 50
print(numbers)  # [10, 20, 40]

# pop(index) - Remove and return item at index
second = numbers.pop(1)
print(second)   # 20
print(numbers)  # [10, 40]

# del - Delete by index
del numbers[0]
print(numbers)  # [40]

# clear() - Remove all items
numbers.clear()
print(numbers)  # []

# ===================================
# CHANGING ITEMS
# ===================================

fruits = ["apple", "banana", "orange"]

# Change a single item
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'orange']

# Change multiple items with slicing
fruits[0:2] = ["grape", "mango"]
print(fruits)  # ['grape', 'mango', 'orange']

# ===================================
# SORTING LISTS
# ===================================

# sort() - Sort the list in place (modifies original)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Sort in reverse order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Alphabetical sorting
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']

# sorted() - Return new sorted list (keeps original)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)  # [1, 1, 3, 4, 5] (new list)

# ===================================
# REVERSING LISTS
# ===================================

numbers = [1, 2, 3, 4, 5]

# reverse() - Reverse the list in place
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed() - Return reversed iterator
original = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original))
print(original)       # [1, 2, 3, 4, 5] (unchanged)
print(reversed_list)  # [5, 4, 3, 2, 1] (new list)

# ===================================
# COPYING LISTS
# ===================================

# WRONG WAY - Creates reference, not copy!
list1 = [1, 2, 3]
list2 = list1  # NOT a copy!
list2.append(4)
print(list1)  # [1, 2, 3, 4] - BOTH changed!

# RIGHT WAY - Using copy()
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - Original unchanged
print(list2)  # [1, 2, 3, 4] - Copy changed

# Alternative: slicing
list3 = list1[:]  # Also makes a copy

# ===================================
# COMBINING LISTS
# ===================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Using extend() (modifies first list)
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# ===================================
# COMMON PATTERNS
# ===================================

# Build a list with user input
shopping_list = []
print("Enter 3 items:")
for i in range(3):
    item = input(f"Item {i + 1}: ")
    shopping_list.append(item)
print(f"Your list: {shopping_list}")

# Remove duplicates (using set and back to list)
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5] (order may vary)

# Filter items (keep only certain ones)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # [2, 4, 6, 8, 10]
