"""
===================================
PRACTICE: File Input/Output (I/O)
===================================
Complete these exercises to practice reading and writing files
"""

import json
import csv
import os

# ===================================
# WARM-UP EXERCISES
# ===================================

# Practice 1: Write to a text file
# Create a file called 'hello.txt' and write "Hello, World!" to it
# Your code here:
with open('hello.txt', 'w') as file:
    file.write("Hello, World!")



# Practice 2: Read from a text file
# Read the content from 'hello.txt' and print it
# Your code here:
with open('hello.txt', 'r')as file:
    print(file.read())




# Practice 3: Append to a file
# Append "This is line 2" to 'hello.txt'
# Your code here:
with open('hello.txt', 'a') as file:
    file.write("\nThis is Line 2\n")


# Practice 4: Read line by line
# Read 'hello.txt' line by line and print each line
# Your code here:
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip())


# ===================================
# JSON EXERCISES
# ===================================

# Practice 5: Save a dictionary to JSON
# Save this dictionary to 'person.json':
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'hobbies': ['reading', 'gaming']
}
# Your code here:
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# Practice 6: Load dictionary from JSON
# Load the data from 'person.json' and print the person's name
# Your code here:
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person['name'])


# Practice 7: Save a list to JSON
# Save this list to 'shopping_list.json':
shopping_list = ['milk', 'eggs', 'bread', 'butter']
# Your code here:
with open('shopping_list.json', 'w') as file:
    json.dump(shopping_list, file, indent=4)


# ===================================
# INTERMEDIATE EXERCISES
# ===================================

# Practice 8: Create a simple note-taking system
# Write functions to:
# - save_note(filename, note) - saves note to a text file
# - load_note(filename) - returns the note content
# - append_note(filename, additional_text) - adds text to existing note

def save_note(filename, note):
    with open(filename, 'w') as file:
        file.write(note)


def load_note(filename):
    with open(filename, 'r') as file:
        return file.read()

def append_note(filename, additional_text):
    with open(filename, 'a') as file:
        file.write(additional_text)


# Test your functions:
save_note('my_note.txt', 'This is my first note!')
print(load_note('my_note.txt'))
append_note('my_note.txt', '\nThis is an addition.')
print(load_note('my_note.txt'))


# Practice 9: Create a contacts manager
# Write functions to:
# - save_contacts(contacts_dict) - saves contacts to 'contacts.json'
# - load_contacts() - loads contacts from 'contacts.json'
# - add_contact(name, phone) - adds a contact and saves

def save_contacts(contacts_dict):
    pass  # Your code here


def load_contacts():
    pass  # Your code here


def add_contact(name, phone):
    # Load existing contacts, add new one, save
    pass  # Your code here


# Test your functions:
# contacts = {
#     'Alice': '555-1234',
#     'Bob': '555-5678'
# }
# save_contacts(contacts)
# add_contact('Charlie', '555-9999')
# print(load_contacts())


# ===================================
# CHALLENGES
# ===================================

# Challenge 1: Upgrade your Inventory System
# Modify your inventory system to save/load from JSON
# Create an Inventory class with:
# - load_inventory() - loads from 'inventory.json' or starts with empty dict
# - save_inventory() - saves current inventory
# - add_item(name, quantity) - adds item and saves
# - remove_item(name) - removes item and saves
# - update_quantity(name, new_quantity) - updates and saves
# - display() - shows all items

class Inventory:
    def __init__(self):
        self.items = self.load_inventory()

    def load_inventory(self):
        pass  # Your code here

    def save_inventory(self):
        pass  # Your code here

    def add_item(self, name, quantity):
        pass  # Your code here

    def remove_item(self, name):
        pass  # Your code here

    def update_quantity(self, name, new_quantity):
        pass  # Your code here

    def display(self):
        pass  # Your code here


# Test your Inventory:
# inv = Inventory()
# inv.add_item('mouse', 5)
# inv.add_item('keyboard', 10)
# inv.display()
# inv.update_quantity('mouse', 8)
# inv.display()
# # Now close and restart your program - inventory should persist!


# Challenge 2: Create a Todo List with Persistence
# Build a TodoList class that saves to/loads from JSON
# Each todo should be a dictionary: {'task': 'text', 'completed': False}
# Methods:
# - load_todos() - loads from 'todos.json'
# - save_todos() - saves to 'todos.json'
# - add_task(task_text) - adds task and saves
# - complete_task(index) - marks complete and saves
# - delete_task(index) - removes task and saves
# - display() - shows all tasks with status

class TodoList:
    def __init__(self):
        self.todos = self.load_todos()

    def load_todos(self):
        pass  # Your code here

    def save_todos(self):
        pass  # Your code here

    def add_task(self, task_text):
        pass  # Your code here

    def complete_task(self, index):
        pass  # Your code here

    def delete_task(self, index):
        pass  # Your code here

    def display(self):
        pass  # Your code here


# Test your TodoList:
# todos = TodoList()
# todos.add_task("Learn File I/O")
# todos.add_task("Build a project")
# todos.display()
# todos.complete_task(0)
# todos.display()


# Challenge 3: Settings Manager
# Create an AppSettings class that manages user preferences
# Default settings: {'theme': 'light', 'notifications': True, 'volume': 50}
# Methods:
# - load_settings() - loads from 'settings.json' or returns defaults
# - save_settings() - saves to 'settings.json'
# - get(key) - returns value for a setting
# - set(key, value) - updates a setting and saves
# - reset_to_defaults() - resets all settings to defaults

class AppSettings:
    def __init__(self):
        self.defaults = {
            'theme': 'light',
            'notifications': True,
            'volume': 50
        }
        self.settings = self.load_settings()

    def load_settings(self):
        pass  # Your code here

    def save_settings(self):
        pass  # Your code here

    def get(self, key):
        pass  # Your code here

    def set(self, key, value):
        pass  # Your code here

    def reset_to_defaults(self):
        pass  # Your code here


# Test your AppSettings:
# settings = AppSettings()
# print(settings.get('theme'))  # light
# settings.set('theme', 'dark')
# print(settings.get('theme'))  # dark
# settings.reset_to_defaults()
# print(settings.get('theme'))  # light


# Challenge 4: Grade Book with CSV Export
# Create a GradeBook class that stores student grades and can export to CSV
# Methods:
# - add_student(name, grades_list) - adds a student
# - get_average(name) - returns student's average
# - save_to_json() - saves grade book to JSON
# - load_from_json() - loads grade book from JSON
# - export_to_csv(filename) - exports all students and averages to CSV

class GradeBook:
    def __init__(self):
        self.students = self.load_from_json()

    def add_student(self, name, grades_list):
        pass  # Your code here

    def get_average(self, name):
        pass  # Your code here

    def save_to_json(self):
        pass  # Your code here

    def load_from_json(self):
        pass  # Your code here

    def export_to_csv(self, filename):
        pass  # Your code here


# Test your GradeBook:
# gb = GradeBook()
# gb.add_student('Alice', [90, 85, 88])
# gb.add_student('Bob', [75, 80, 78])
# print(gb.get_average('Alice'))
# gb.export_to_csv('grades.csv')


# Challenge 5: Weather Data Logger
# Create a WeatherLogger that saves daily weather data
# Each entry: {'date': '2024-01-01', 'temp': 75, 'condition': 'sunny'}
# Methods:
# - log_weather(date, temp, condition) - adds entry and saves
# - get_all_data() - returns all weather data
# - get_average_temp() - calculates average of all temps
# - get_hottest_day() - returns entry with highest temp
# - search_by_condition(condition) - returns all days with that condition
# - export_to_csv() - exports all data to CSV

class WeatherLogger:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        pass  # Your code here

    def save_data(self):
        pass  # Your code here

    def log_weather(self, date, temp, condition):
        pass  # Your code here

    def get_all_data(self):
        pass  # Your code here

    def get_average_temp(self):
        pass  # Your code here

    def get_hottest_day(self):
        pass  # Your code here

    def search_by_condition(self, condition):
        pass  # Your code here

    def export_to_csv(self):
        pass  # Your code here


# Test your WeatherLogger:
# logger = WeatherLogger()
# logger.log_weather('2024-01-01', 75, 'sunny')
# logger.log_weather('2024-01-02', 68, 'rainy')
# logger.log_weather('2024-01-03', 82, 'sunny')
# print(f"Average temp: {logger.get_average_temp()}")
# print(f"Hottest day: {logger.get_hottest_day()}")
# sunny_days = logger.search_by_condition('sunny')
# print(f"Sunny days: {len(sunny_days)}")
# logger.export_to_csv()


"""
===================================
HINTS
===================================

Reading a file:
    with open('filename.txt', 'r') as file:
        content = file.read()

Writing to a file:
    with open('filename.txt', 'w') as file:
        file.write('content')

Appending to a file:
    with open('filename.txt', 'a') as file:
        file.write('more content')

Saving JSON:
    import json
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

Loading JSON:
    import json
    with open('data.json', 'r') as file:
        data = json.load(file)

Check if file exists:
    import os
    if os.path.exists('filename.txt'):
        # file exists

Handle missing files:
    try:
        with open('file.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}  # default value

Writing CSV:
    import csv
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['Alice', 25])

Remember:
- Always use 'with open()' - it closes files automatically
- Use JSON for dictionaries and lists
- Use CSV for spreadsheet-like data
- Handle FileNotFoundError for loading
"""
