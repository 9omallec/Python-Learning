# ===================================
# LESSON 8A: List Basics
# ===================================

# Lists store multiple values in one variable
# Think of it as a container that holds multiple items in order

# ===================================
# CREATING LISTS
# ===================================

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a list of strings
fruits = ["apple", "banana", "orange"]
print(fruits)

# Mixed types (not common, but possible)
mixed = [1, "hello", 3.14, True]
print(mixed)

# Empty list
empty_list = []
print(empty_list)

# ===================================
# ACCESSING LIST ITEMS
# ===================================

fruits = ["apple", "banana", "orange", "grape"]

# Access by index (starts at 0!)
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[3])   # grape

# Negative indexing (from the end)
print(fruits[-1])  # grape (last item)
print(fruits[-2])  # orange (second to last)

# ===================================
# LIST LENGTH
# ===================================

# Get number of items
print(len(fruits))  # 4

# Common pattern: access last item safely
last_index = len(fruits) - 1
print(fruits[last_index])  # grape

# ===================================
# CHECKING IF ITEM EXISTS
# ===================================

fruits = ["apple", "banana", "orange"]

# Check if item is in list
if "apple" in fruits:
    print("We have apples!")

if "mango" not in fruits:
    print("No mangos available")

# ===================================
# LOOPING THROUGH LISTS
# ===================================

fruits = ["apple", "banana", "orange"]

# Loop through each item
for fruit in fruits:
    print(fruit)

# Loop with index using range
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# ===================================
# LIST SLICING (Getting Portions)
# ===================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get items from index 2 to 5 (not including 5)
print(numbers[2:5])   # [2, 3, 4]

# Get first 3 items
print(numbers[:3])    # [0, 1, 2]

# Get items from index 5 to end
print(numbers[5:])    # [5, 6, 7, 8, 9]

# Get last 3 items
print(numbers[-3:])   # [7, 8, 9]

# Get every other item
print(numbers[::2])   # [0, 2, 4, 6, 8]

# ===================================
# COMMON PATTERNS
# ===================================

# Find the index of an item
fruits = ["apple", "banana", "orange"]
banana_index = fruits.index("banana")
print(f"Banana is at index {banana_index}")

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4, 2]
count_of_twos = numbers.count(2)
print(f"Number of 2s: {count_of_twos}")

# Get max and min (for numbers)
scores = [85, 92, 78, 95, 88]
highest = max(scores)
lowest = min(scores)
print(f"Highest: {highest}, Lowest: {lowest}")

# Sum all numbers
total = sum(scores)
average = total / len(scores)
print(f"Total: {total}, Average: {average}")
