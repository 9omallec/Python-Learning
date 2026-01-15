"""
===================================
LESSON 13: File Input/Output (I/O)
===================================

File I/O lets you save and load data from files, making your programs remember
things between runs.

WHY THIS MATTERS:
- Save user data (settings, progress, favorites)
- Load configuration files
- Export data (reports, logs, exports)
- Build apps that persist data
- Essential for real-world applications

Remember your inventory system? Right now it forgets everything when you quit.
With File I/O, you can save it and load it back!
"""

# ===================================
# PART 1: Reading Text Files
# ===================================

# BASIC READ:
# Let's say you have a file called "data.txt" with this content:
# Hello, World!
# Python is awesome
# File I/O is useful

# Read entire file:
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# The 'with' statement automatically closes the file when done
# 'r' means "read mode"


# Read line by line:
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes extra newlines

# Read all lines into a list:
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # ['Hello, World!\n', 'Python is awesome\n', ...]


# ===================================
# PART 2: Writing Text Files
# ===================================

# WRITE MODE ('w') - creates new file or OVERWRITES existing:
with open('output.txt', 'w') as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# ⚠️ WARNING: 'w' mode erases the file first!


# APPEND MODE ('a') - adds to end of existing file:
with open('output.txt', 'a') as file:
    file.write("This line is appended\n")
    file.write("So is this one\n")


# Writing multiple lines at once:
lines_to_write = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open('output.txt', 'w') as file:
    file.writelines(lines_to_write)


# ===================================
# PART 3: File Modes Summary
# ===================================

"""
'r'  - Read only (file must exist)
'w'  - Write only (creates new or OVERWRITES)
'a'  - Append only (adds to end, creates if doesn't exist)
'r+' - Read and write (file must exist)
'w+' - Write and read (creates new or overwrites)
'a+' - Append and read (creates if doesn't exist)
"""


# ===================================
# PART 4: Handling File Errors
# ===================================

# What if file doesn't exist?
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Better approach - check if file exists first:
import os

if os.path.exists('data.txt'):
    with open('data.txt', 'r') as file:
        content = file.read()
else:
    print("File doesn't exist!")


# ===================================
# PART 5: Working with JSON Files
# ===================================

import json

# JSON is perfect for storing dictionaries and lists

# SAVING DATA TO JSON:
my_data = {
    'name': 'Connor',
    'age': 35,
    'city': 'Omaha',
    'hobbies': ['coding', 'gaming', 'pokemon']
}

with open('user_data.json', 'w') as file:
    json.dump(my_data, file, indent=4)  # indent=4 makes it pretty


# LOADING DATA FROM JSON:
with open('user_data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data['name'])  # Connor
    print(loaded_data['hobbies'])  # ['coding', 'gaming', 'pokemon']


# ===================================
# PART 6: Real Example - Saving Inventory System
# ===================================

import json

# Your inventory dictionary:
inventory = {
    'mouse': 5,
    'keyboard': 10,
    'monitor': 3
}

# SAVE inventory:
def save_inventory(inventory_dict, filename='inventory.json'):
    """Save inventory to file"""
    with open(filename, 'w') as file:
        json.dump(inventory_dict, file, indent=4)
    print("Inventory saved!")


# LOAD inventory:
def load_inventory(filename='inventory.json'):
    """Load inventory from file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved inventory found. Starting fresh.")
        return {}


# Using the functions:
save_inventory(inventory)  # Save it

# Later, when program starts:
loaded_inventory = load_inventory()  # Load it back
print(loaded_inventory)  # {'mouse': 5, 'keyboard': 10, 'monitor': 3}


# ===================================
# PART 7: CSV Files (Comma-Separated Values)
# ===================================

import csv

# CSV is great for spreadsheet-like data

# WRITING CSV:
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


# READING CSV:
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Alice', '25', 'New York']


# Using DictReader (easier to work with):
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")


# ===================================
# PART 8: File Paths
# ===================================

# ABSOLUTE PATH (full path from root):
# Windows: 'C:\\Users\\Connor\\Desktop\\data.txt'
# Mac/Linux: '/Users/connor/Desktop/data.txt'

# RELATIVE PATH (relative to current script):
# 'data.txt' - same folder as script
# '../data.txt' - one folder up
# 'files/data.txt' - in a subfolder called 'files'

# Get current working directory:
import os
print(os.getcwd())  # Where your script is running from

# Join paths properly (works on all operating systems):
file_path = os.path.join('data', 'files', 'info.txt')
# Automatically uses correct separator (/ or \)


# ===================================
# PART 9: Practical Example - Settings File
# ===================================

import json
import os

class AppSettings:
    """Manages application settings"""

    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings()

    def load_settings(self):
        """Load settings from file or return defaults"""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                return json.load(file)
        else:
            # Return default settings if file doesn't exist
            return {
                'theme': 'light',
                'notifications': True,
                'volume': 50
            }

    def save_settings(self):
        """Save settings to file"""
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file, indent=4)
        print("Settings saved!")

    def update_setting(self, key, value):
        """Update a setting and save"""
        self.settings[key] = value
        self.save_settings()

    def get_setting(self, key):
        """Get a setting value"""
        return self.settings.get(key)


# Using the settings manager:
settings = AppSettings()
print(settings.get_setting('theme'))  # light
settings.update_setting('theme', 'dark')  # Changes and saves automatically


# ===================================
# PART 10: Reading/Writing Lists
# ===================================

# Simple way to save a list to a text file:
my_list = ['apple', 'banana', 'cherry', 'date']

# Save:
with open('fruits.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

# Load:
with open('fruits.txt', 'r') as file:
    loaded_list = [line.strip() for line in file]
    print(loaded_list)  # ['apple', 'banana', 'cherry', 'date']


# Better way with JSON (preserves data types):
import json

my_list = ['apple', 'banana', 'cherry', 'date']

# Save:
with open('fruits.json', 'w') as file:
    json.dump(my_list, file)

# Load:
with open('fruits.json', 'r') as file:
    loaded_list = json.load(file)


# ===================================
# KEY TAKEAWAYS
# ===================================

"""
1. Always use 'with open()' - it closes files automatically
   ✅ with open('file.txt', 'r') as file:
   ❌ file = open('file.txt', 'r')  # Must remember to close!

2. File modes:
   'r' = read, 'w' = write (overwrites!), 'a' = append

3. JSON is best for dictionaries and lists:
   json.dump(data, file)  # Save
   data = json.load(file)  # Load

4. Handle errors with try/except or os.path.exists()

5. Use os.path.join() for file paths (cross-platform)

6. CSV for spreadsheet-like data (rows and columns)

7. Text files for simple line-by-line data
"""


# ===================================
# COMMON PATTERNS
# ===================================

# 1. Save and Load Dictionary:
import json

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist


# 2. Append to Log File:
def log_message(message):
    with open('app.log', 'a') as f:
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {message}\n")


# 3. Read Configuration:
def load_config():
    import json
    with open('config.json', 'r') as f:
        return json.load(f)


# ===================================
# WHEN TO USE EACH FILE TYPE
# ===================================

"""
TEXT FILES (.txt):
- Simple line-by-line data
- Log files
- Notes or messages

JSON FILES (.json):
- Dictionaries and lists
- Settings and configuration
- Structured data
- API responses

CSV FILES (.csv):
- Spreadsheet data
- Tables with rows/columns
- Data you'll open in Excel
- Large datasets
"""
