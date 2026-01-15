"""
===================================
PRACTICE: Object-Oriented Programming (OOP)
===================================
Complete these exercises to practice classes and objects
"""

# ===================================
# WARM-UP EXERCISES
# ===================================

# Practice 1: Create a simple Dog class
# Attributes: name, breed, age
# Method: bark() - prints "{name} says Woof!"
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Axel", "Golden Retriever", 9)
dog2 = Dog("Bob", "Chiuaua", 1)
dog3 = Dog("Kida", "Great Piranese", 13)

dog1.bark()
dog2.bark()
dog3.bark()



# Test your Dog class:
# my_dog = Dog("Buddy", "Golden Retriever", 3)
# print(my_dog.name)  # Should print: Buddy
# my_dog.bark()       # Should print: Buddy says Woof!


# Practice 2: Create a Book class
# Attributes: title, author, pages
# Method: info() - prints book information
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f'"{self.title}" by {self.author} ({self.pages})')


# Test your Book class:
book1 = Book("1984", "George Orwell", 328)
book1.info()  # Should print: "1984" by George Orwell (328 pages)


# Practice 3: Create a Rectangle class
# Attributes: width, height
# Methods:
#   - area() - returns width * height
#   - perimeter() - returns 2 * (width + height)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)




# Test your Rectangle:
rect = Rectangle(5, 10)
print(rect.area())       # Should print: 50
print(rect.perimeter())  # Should print: 30


# ===================================
# INTERMEDIATE EXERCISES
# ===================================

# Practice 4: Create a Student class
# Attributes: name, grades (list of grades)
# Methods:
#   - add_grade(grade) - adds a grade to the list
#   - average() - returns the average of all grades
#   - is_passing() - returns True if average >= 60, else False
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def is_passing(self):
        return self.average() >= 60



# Test your Student class:
student = Student("Alice", [85, 90, 78])
student.add_grade(88)
print(student.average())     # Should print average of [85, 90, 78, 88]
print(student.is_passing())  # Should print True


# Practice 5: Create a ShoppingCart class
# Attributes: items (dictionary: item_name -> price)
# Methods:
#   - add_item(name, price) - adds item to cart
#   - remove_item(name) - removes item from cart
#   - total() - returns total price of all items
#   - display() - prints all items and their prices
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        self.items.pop(name)

    def total(self):
        return sum(self.items.values())

    def display(self):
        for name, price in self.items.items():
            print(f"{name}: ${price}")


# Test your ShoppingCart:
cart = ShoppingCart()
cart.add_item("Apple", 1.50)
cart.add_item("Bread", 2.99)
cart.display()
print(f"Total: ${cart.total()}")
cart.remove_item("Apple")
print(f"Total: ${cart.total()}")


# ===================================
# CHALLENGES
# ===================================

# Challenge 1: Create a TodoList class
# Attributes: tasks (list of dictionaries: {'task': 'text', 'completed': False})
# Methods:
#   - add_task(task_text) - adds a new task
#   - complete_task(index) - marks task at index as completed
#   - display() - shows all tasks with their status
#   - get_incomplete() - returns count of incomplete tasks
class TodoList:
    pass  # Your code here


# Test your TodoList:
# todos = TodoList()
# todos.add_task("Learn OOP")
# todos.add_task("Build a project")
# todos.display()
# todos.complete_task(0)
# todos.display()
# print(f"Incomplete tasks: {todos.get_incomplete()}")


# Challenge 2: Upgrade your Pokedex!
# Create a Pokemon class with:
# Attributes: name, type, hp, level
# Methods:
#   - attack(other_pokemon) - deals damage based on level
#   - heal(amount) - restores HP (can't exceed max HP)
#   - level_up() - increases level, increases max HP
#   - display_stats() - shows all Pokemon info
#
# Then create a Pokedex class with:
# Attributes: pokemon_list (list of Pokemon objects)
# Methods:
#   - catch_pokemon(pokemon) - adds Pokemon to list
#   - release_pokemon(name) - removes Pokemon by name
#   - display_all() - shows all Pokemon in Pokedex
#   - strongest() - returns Pokemon with highest level

class Pokemon:
    pass  # Your code here


class Pokedex:
    pass  # Your code here


# Test your Pokedex:
# pikachu = Pokemon("Pikachu", "Electric", 100, 5)
# charizard = Pokemon("Charizard", "Fire", 150, 8)
#
# my_pokedex = Pokedex()
# my_pokedex.catch_pokemon(pikachu)
# my_pokedex.catch_pokemon(charizard)
# my_pokedex.display_all()
# print(f"Strongest: {my_pokedex.strongest().name}")


# Challenge 3: Build a Weather Tracker
# Create a WeatherDay class:
# Attributes: date, temperature, condition (sunny/rainy/etc)
# Methods:
#   - is_hot() - returns True if temp > 80
#   - is_cold() - returns True if temp < 40
#   - display() - shows weather info
#
# Then create a WeatherTracker class:
# Attributes: days (list of WeatherDay objects)
# Methods:
#   - add_day(weather_day) - adds a day to tracker
#   - average_temp() - returns average temperature
#   - hottest_day() - returns WeatherDay with highest temp
#   - count_sunny_days() - returns count of sunny days

class WeatherDay:
    pass  # Your code here


class WeatherTracker:
    pass  # Your code here


# Test your WeatherTracker:
# tracker = WeatherTracker()
# tracker.add_day(WeatherDay("2024-01-01", 75, "sunny"))
# tracker.add_day(WeatherDay("2024-01-02", 82, "sunny"))
# tracker.add_day(WeatherDay("2024-01-03", 68, "rainy"))
# print(f"Average temp: {tracker.average_temp()}")
# print(f"Sunny days: {tracker.count_sunny_days()}")


"""
===================================
HINTS
===================================

General Structure:
    class ClassName:
        def __init__(self, param1, param2):
            self.attribute1 = param1
            self.attribute2 = param2

        def method_name(self):
            # Use self.attribute1 here
            pass

Creating Objects:
    object = ClassName(value1, value2)

Accessing Attributes:
    object.attribute1

Calling Methods:
    object.method_name()

Lists as Attributes:
    def __init__(self):
        self.items = []  # Empty list

    def add_item(self, item):
        self.items.append(item)

Dictionaries as Attributes:
    def __init__(self):
        self.data = {}  # Empty dict

    def add_data(self, key, value):
        self.data[key] = value

Remember:
- Use 'self' to access attributes inside methods
- __init__ sets up initial values
- Each object is independent
"""
