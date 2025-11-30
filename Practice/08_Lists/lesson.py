# ===================================
# LESSON 8: Lists
# ===================================

# Lists store multiple values in one variable
# Think of it as a container that holds multiple items

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

# Slicing (getting a portion)
print(fruits[1:3])   # ['banana', 'orange']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['orange', 'grape']

# ===================================
# MODIFYING LISTS
# ===================================

# Change an item
fruits[1] = "blueberry"
print(fruits)

# Add to the end
fruits.append("mango")
print(fruits)

# Insert at a specific position
fruits.insert(1, "kiwi")  # Insert at index 1
print(fruits)

# Remove an item
fruits.remove("orange")  # Remove by value
print(fruits)

# Remove by index
del fruits[0]
print(fruits)

# Remove and return last item
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# ===================================
# LIST OPERATIONS
# ===================================

numbers = [1, 2, 3, 4, 5]

# Length of list
print(len(numbers))  # 5

# Check if item exists
if 3 in numbers:
    print("3 is in the list!")

# Count occurrences
nums = [1, 2, 2, 3, 2, 4]
print(nums.count(2))  # 3

# Find index of an item
print(numbers.index(3))  # 2

# Sort a list
unsorted = [3, 1, 4, 1, 5, 9, 2]
unsorted.sort()
print(unsorted)  # [1, 1, 2, 3, 4, 5, 9]

# Reverse a list
numbers.reverse()
print(numbers)

# ===================================
# LOOPING THROUGH LISTS
# ===================================

fruits = ["apple", "banana", "orange"]

# Loop through items
for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Better way: enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ===================================
# LIST COMPREHENSION (Advanced but useful!)
# ===================================

# Create a list of squares
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Filter with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# ===================================
# COMMON LIST PATTERNS
# ===================================

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 15

# Find max and min
print(max(numbers))  # 5
print(min(numbers))  # 1

# Join strings
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # "Hello World"

# Split string into list
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'orange']
