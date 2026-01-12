"""
===================================
LESSON 12: Object-Oriented Programming (OOP) Basics
===================================

OOP is a way to organize code by grouping related data and functions together.
Instead of having separate variables and functions floating around, you create
"blueprints" (classes) that bundle them together.

WHY THIS MATTERS:
- Organize complex code better
- Reuse code more easily
- Most Python libraries use classes (Flask, requests, tkinter, etc.)
- Essential for building larger applications
"""

# ===================================
# PART 1: What is a Class?
# ===================================

# WITHOUT OOP - messy and repetitive:
pokemon1_name = "Pikachu"
pokemon1_type = "Electric"
pokemon1_hp = 100

pokemon2_name = "Charizard"
pokemon2_type = "Fire"
pokemon2_hp = 150

# What if you need 100 Pokemon? This doesn't scale!


# WITH OOP - organized and reusable:
class Pokemon:
    """A blueprint for creating Pokemon"""

    def __init__(self, name, poke_type, hp):
        """
        This runs automatically when you create a new Pokemon
        __init__ = "initialize" = "set up"
        self = refers to THIS specific Pokemon
        """
        self.name = name
        self.type = poke_type
        self.hp = hp

    def attack(self):
        """A method (function inside a class)"""
        print(f"{self.name} attacks!")

    def take_damage(self, damage):
        """Reduce HP when attacked"""
        self.hp -= damage
        print(f"{self.name} took {damage} damage! HP: {self.hp}")


# Creating Pokemon (called "instantiating"):
pikachu = Pokemon("Pikachu", "Electric", 100)
charizard = Pokemon("Charizard", "Fire", 150)

# Using the Pokemon:
print(f"{pikachu.name} has {pikachu.hp} HP")  # Pikachu has 100 HP
pikachu.attack()  # Pikachu attacks!
pikachu.take_damage(20)  # Pikachu took 20 damage! HP: 80

print(f"{charizard.name} has {charizard.hp} HP")  # Charizard has 150 HP


# ===================================
# PART 2: Breaking Down the Syntax
# ===================================

"""
class ClassName:           ← Define the blueprint (capitalize the name)
    def __init__(self, params):  ← Constructor (runs when creating object)
        self.attribute = value    ← Store data in the object

    def method(self):      ← Define behaviors (functions)
        # do something with self.attribute

CREATING AN OBJECT:
object_name = ClassName(arguments)  ← Make a specific instance

ACCESSING ATTRIBUTES:
object_name.attribute      ← Get stored data

CALLING METHODS:
object_name.method()       ← Execute behavior
"""


# ===================================
# PART 3: Real-World Example - Bank Account
# ===================================

class BankAccount:
    """Represents a bank account"""

    def __init__(self, owner, balance=0):
        """
        owner: name of account holder
        balance: starting balance (defaults to 0)
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to account"""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Remove money from account"""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        """Display current balance"""
        print(f"{self.owner}'s balance: ${self.balance}")


# Using the BankAccount class:
my_account = BankAccount("Connor", 1000)
my_account.check_balance()  # Connor's balance: $1000
my_account.deposit(500)     # Deposited $500. New balance: $1500
my_account.withdraw(200)    # Withdrew $200. New balance: $1300
my_account.withdraw(5000)   # Insufficient funds!


# ===================================
# PART 4: Multiple Objects from Same Class
# ===================================

# Each object is independent:
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob", 1000)

account1.deposit(100)  # Only affects account1
account2.deposit(200)  # Only affects account2

account1.check_balance()  # Alice's balance: $600
account2.check_balance()  # Bob's balance: $1200


# ===================================
# PART 5: Why Use self?
# ===================================

"""
'self' refers to the SPECIFIC object you're working with.

When you call:    pikachu.attack()
Python translates: Pokemon.attack(pikachu)

'self' is how the method knows which object it's working with.
"""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand  # THIS car's brand
        self.speed = speed  # THIS car's speed

    def accelerate(self):
        self.speed += 10  # Increase THIS car's speed
        print(f"{self.brand} is now going {self.speed} mph")


car1 = Car("Toyota", 50)
car2 = Car("Honda", 60)

car1.accelerate()  # Toyota is now going 60 mph
car2.accelerate()  # Honda is now going 70 mph
# Each car tracks its own speed!


# ===================================
# PART 6: Class Methods vs Regular Functions
# ===================================

# Regular function (not in a class):
def greet(name):
    return f"Hello, {name}!"

print(greet("Connor"))  # Hello, Connor!


# Method (function in a class):
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}!"


person = Person("Connor")
print(person.greet())  # Hello, I'm Connor!

# Methods have access to the object's data through 'self'
# Regular functions don't


# ===================================
# PART 7: Practical Example - Your Inventory System with OOP
# ===================================

class InventoryItem:
    """Represents an item in inventory"""

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_stock(self, amount):
        """Add to inventory"""
        self.quantity += amount
        print(f"Added {amount} {self.name}(s). Total: {self.quantity}")

    def remove_stock(self, amount):
        """Remove from inventory"""
        if amount > self.quantity:
            print(f"Not enough {self.name} in stock!")
        else:
            self.quantity -= amount
            print(f"Removed {amount} {self.name}(s). Remaining: {self.quantity}")

    def display(self):
        """Show item info"""
        print(f"{self.name}: {self.quantity} in stock")


# Using the inventory system:
mouse = InventoryItem("Mouse", 5)
keyboard = InventoryItem("Keyboard", 10)

mouse.display()        # Mouse: 5 in stock
mouse.add_stock(3)     # Added 3 Mouse(s). Total: 8
mouse.remove_stock(2)  # Removed 2 Mouse(s). Remaining: 6

keyboard.display()     # Keyboard: 10 in stock


# ===================================
# KEY TAKEAWAYS
# ===================================

"""
1. CLASSES are blueprints, OBJECTS are specific instances
   - Class: Pokemon (the blueprint)
   - Objects: pikachu, charizard (specific Pokemon)

2. __init__ runs automatically when creating an object
   - Sets up initial attributes
   - Like filling out a form when you create something

3. self refers to the specific object
   - pikachu.attack() → self = pikachu
   - charizard.attack() → self = charizard

4. Attributes store data (self.name, self.hp)
   - Like variables attached to an object

5. Methods define behaviors (def attack, def take_damage)
   - Like functions that work with the object's data

6. Each object is independent
   - Changing pikachu doesn't affect charizard
"""


# ===================================
# WHEN TO USE OOP
# ===================================

"""
USE CLASSES when you have:
- Related data that belongs together (name, HP, type)
- Actions that work with that data (attack, take_damage)
- Multiple similar things (many Pokemon, many accounts)

DON'T USE CLASSES when:
- Simple scripts with a few variables
- One-time calculations
- Simple utility functions

EXAMPLES:
✅ Good for OOP: Pokemon, Bank Accounts, Users, Products
❌ Overkill: Simple calculator, file rename script
"""
