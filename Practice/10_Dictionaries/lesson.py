# ===================================
# LESSON 10: Dictionaries
# ===================================

# Dictionaries store key-value pairs
# Like a real dictionary: word (key) -> definition (value)

# ===================================
# CREATING DICTIONARIES
# ===================================

# Basic dictionary
person = {
    "name": "Connor",
    "age": 35,
    "city": "Omaha"
}
print(person)

# Different types of values
student = {
    "name": "Alice",
    "grades": [85, 90, 92],
    "passing": True,
    "gpa": 3.7
}

# Empty dictionary
empty_dict = {}

# ===================================
# ACCESSING VALUES
# ===================================

person = {"name": "Connor", "age": 35, "city": "Omaha"}

# Access by key
print(person["name"])   # Connor
print(person["age"])    # 35

# Using .get() (safer - doesn't crash if key doesn't exist)
print(person.get("name"))       # Connor
print(person.get("country"))    # None
print(person.get("country", "USA"))  # USA (default value)

# ===================================
# MODIFYING DICTIONARIES
# ===================================

person = {"name": "Connor", "age": 35}

# Add a new key-value pair
person["city"] = "Omaha"
print(person)

# Update existing value
person["age"] = 36
print(person)

# Remove a key-value pair
del person["city"]
print(person)

# Remove and return value
age = person.pop("age")
print(age)
print(person)

# ===================================
# DICTIONARY METHODS
# ===================================

person = {"name": "Connor", "age": 35, "city": "Omaha"}

# Get all keys
print(person.keys())     # dict_keys(['name', 'age', 'city'])

# Get all values
print(person.values())   # dict_values(['Connor', 35, 'Omaha'])

# Get all key-value pairs
print(person.items())    # dict_items([('name', 'Connor'), ...])

# Check if key exists
if "name" in person:
    print("Name exists!")

# Get number of items
print(len(person))  # 3

# Clear all items
person_copy = person.copy()
person_copy.clear()
print(person_copy)  # {}

# ===================================
# LOOPING THROUGH DICTIONARIES
# ===================================

person = {"name": "Connor", "age": 35, "city": "Omaha"}

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through both
for key, value in person.items():
    print(f"{key}: {value}")

# ===================================
# NESTED DICTIONARIES
# ===================================

# Dictionary containing dictionaries
users = {
    "user1": {
        "name": "Alice",
        "age": 25
    },
    "user2": {
        "name": "Bob",
        "age": 30
    }
}

print(users["user1"]["name"])  # Alice

# ===================================
# PRACTICAL EXAMPLES
# ===================================

# Phone book
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

# Look up a number
name = "Alice"
if name in phonebook:
    print(f"{name}'s number is {phonebook[name]}")

# Inventory system
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

# Update inventory
inventory["apples"] -= 5  # Sold 5 apples
print(f"Apples remaining: {inventory['apples']}")

# Word counter
text = "hello world hello"
word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'hello': 2, 'world': 1}

# Better way using get()
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

# ===================================
# DICTIONARY VS LIST
# ===================================

# List: Ordered, access by index
fruits_list = ["apple", "banana", "orange"]
print(fruits_list[0])  # apple

# Dictionary: Unordered, access by key
fruits_dict = {
    "a": "apple",
    "b": "banana",
    "o": "orange"
}
print(fruits_dict["a"])  # apple

# Use lists when: You need order, or just a collection of items
# Use dictionaries when: You need to look up values by meaningful keys
