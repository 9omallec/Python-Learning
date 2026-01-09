# ===================================
# LESSON 2: Variables
# ===================================

# Variables store information
# Think of them as labeled boxes that hold values

# Different types of variables:
name = "Connor"        # String (text) - use quotes
age = 25              # Integer (whole number) - no quotes
height = 5.9          # Float (decimal number)
is_learning = True    # Boolean (True or False)

# Using variables in print
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "feet")
print("Am I learning Python?", is_learning)

# You can change variable values
age = 26
print("Now I am", age)

# Variable naming rules:
# ✓ Use lowercase with underscores: my_variable
# ✓ Start with a letter or underscore: _variable
# ✓ Can contain numbers: variable2
# ✗ Cannot start with a number: 2variable
# ✗ Cannot use spaces: my variable
# ✗ Cannot use special characters: my-variable

favorite_color = "blue"  # Good
fav_num = 7              # Good
# 1st_place = "me"       # Bad - starts with number

# ===================================
# Checking Variable Types
# ===================================

# Use type() to see what type a variable is
name = "Connor"
age = 25
height = 5.9
is_learning = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_learning)) # <class 'bool'>

# ===================================
# The None Value
# ===================================

# None represents "no value" or "nothing"
result = None  # No value yet
print(result)  # None
print(type(result))  # <class 'NoneType'>

# Useful when you want to create a variable but don't have a value yet
user_input = None  # Will be filled in later
