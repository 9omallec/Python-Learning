# Mini-Projects: Apply What You've Learned

**Build real programs to solidify your skills!**

---

## 🎯 How to Use This File

Each mini-project combines concepts from multiple lessons. They're designed to:
- **Reinforce learning** through practical application
- **Build confidence** by creating complete programs
- **Show progress** with working software

**When to do these:**
- After completing the related lessons
- When you want a break from exercises
- To test your understanding

---

## 🌟 Project 1: Temperature Converter

**Prerequisites:** Lessons 1-4 (Print, Variables, Math, Input)
**Difficulty:** ⭐ Beginner
**Time:** 15-20 minutes

### What You'll Build:
A program that converts between Fahrenheit and Celsius in both directions.

### Features:
1. Ask user which conversion they want (F→C or C→F)
2. Get the temperature value
3. Perform calculation
4. Display result with proper formatting

### Starter Code:
```python
# Temperature Converter

print("=" * 40)
print("Temperature Converter")
print("=" * 40)

# Your code here!
# 1. Ask user: Convert from F to C, or C to F?
# 2. Get temperature value
# 3. Perform conversion
# 4. Display result

# Formulas:
# C = (F - 32) * 5/9
# F = C * 9/5 + 32
```

### Sample Output:
```
========================================
Temperature Converter
========================================
Convert from (F)ahrenheit or (C)elsius? F
Enter temperature: 100
100.0°F = 37.78°C
```

### Extension Ideas:
- Add Kelvin conversions
- Handle invalid input
- Allow multiple conversions in one run

---

## 🌟 Project 2: Simple Calculator

**Prerequisites:** Lessons 1-4 (Print, Variables, Math, Input)
**Difficulty:** ⭐ Beginner
**Time:** 20-25 minutes

### What You'll Build:
A calculator that performs basic operations (+, -, *, /).

### Features:
1. Display a menu of operations
2. Get two numbers from user
3. Perform the selected operation
4. Show the result

### Starter Code:
```python
# Simple Calculator

print("=" * 40)
print("Simple Calculator")
print("=" * 40)
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("=" * 40)

# Your code here!
```

### Sample Output:
```
========================================
Simple Calculator
========================================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
========================================
Choose operation (1-4): 1
Enter first number: 15
Enter second number: 7
Result: 15 + 7 = 22
```

### Extension Ideas:
- Add more operations (power, modulo, square root)
- Handle division by zero
- Allow chaining calculations

---

## 🌟 Project 3: Mad Libs Generator

**Prerequisites:** Lessons 1-5 (Print, Variables, Math, Input, Strings)
**Difficulty:** ⭐ Beginner
**Time:** 20-30 minutes

### What You'll Build:
A fun story generator that asks for different types of words and creates a silly story.

### Features:
1. Ask user for various words (nouns, verbs, adjectives, etc.)
2. Store them in variables
3. Insert them into a pre-written story template
4. Display the completed story

### Starter Code:
```python
# Mad Libs Story Generator

print("=" * 50)
print("Mad Libs Story Generator")
print("=" * 50)
print("Fill in the blanks to create a silly story!")
print()

# Your code here!
# Collect words from user
# Create story using f-strings
# Display final story
```

### Sample Story Template:
```
Once upon a time, there was a [adjective] [noun] named [name].
[Name] loved to [verb] in the [place].
One day, [name] found a [adjective] [object] that could [verb]!
[Name] decided to [verb] all the way to [place].
The end!
```

### Extension Ideas:
- Create multiple story templates
- Let user choose which story
- Save stories to a file (later lesson)

---

## 🌟 Project 4: Grade Calculator

**Prerequisites:** Lessons 1-6 (Print, Variables, Math, Input, Strings, If/Else)
**Difficulty:** ⭐⭐ Intermediate
**Time:** 25-35 minutes

### What You'll Build:
A program that calculates final grades and assigns letter grades.

### Features:
1. Get multiple assignment scores from user
2. Calculate average
3. Determine letter grade (A, B, C, D, F)
4. Show if they passed or failed
5. Display formatted results

### Starter Code:
```python
# Grade Calculator

print("=" * 40)
print("Grade Calculator")
print("=" * 40)

# Your code here!
# Get assignment scores
# Calculate average
# Determine letter grade using if/elif/else
# Display results

# Grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
```

### Sample Output:
```
========================================
Grade Calculator
========================================
Enter assignment 1 score: 85
Enter assignment 2 score: 92
Enter assignment 3 score: 88
Enter assignment 4 score: 90

Results:
--------
Average: 88.75%
Letter Grade: B
Status: PASSED

Great work!
```

### Extension Ideas:
- Add weighted assignments (tests worth more than homework)
- Calculate GPA (4.0 scale)
- Show how many points needed for next letter grade

---

## 🌟 Project 5: Number Guessing Game

**Prerequisites:** Lessons 1-7 (All above + Loops)
**Difficulty:** ⭐⭐ Intermediate
**Time:** 30-40 minutes

### What You'll Build:
A game where the computer picks a random number and the user tries to guess it.

### Features:
1. Computer picks a random number (1-100)
2. User guesses
3. Give hints: "too high" or "too low"
4. Count number of guesses
5. Loop until correct
6. Show final results

### Starter Code:
```python
import random

# Number Guessing Game

print("=" * 40)
print("Number Guessing Game")
print("=" * 40)
print("I'm thinking of a number between 1 and 100...")
print()

secret_number = random.randint(1, 100)
guess_count = 0

# Your code here!
# Use a while loop to keep asking for guesses
# Give hints
# Count guesses
# Congratulate when correct
```

### Sample Output:
```
========================================
Number Guessing Game
========================================
I'm thinking of a number between 1 and 100...

Guess #1: 50
Too low! Try again.

Guess #2: 75
Too high! Try again.

Guess #3: 62
Too low! Try again.

Guess #4: 68
Correct! You got it in 4 guesses!
```

### Extension Ideas:
- Add difficulty levels (different ranges)
- Limit number of guesses
- Keep track of high scores
- Let user play multiple rounds

---

## 🌟 Project 6: Shopping List Manager

**Prerequisites:** Lessons 1-8 (All above + Lists)
**Difficulty:** ⭐⭐ Intermediate
**Time:** 35-45 minutes

### What You'll Build:
A program to manage a shopping list with add, remove, and view features.

### Features:
1. Show menu of options
2. Add items to list
3. Remove items from list
4. View all items
5. Clear entire list
6. Show item count
7. Loop until user quits

### Starter Code:
```python
# Shopping List Manager

shopping_list = []

def show_menu():
    print("\n" + "=" * 40)
    print("Shopping List Manager")
    print("=" * 40)
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Quit")
    print("=" * 40)

# Your code here!
# Create a loop for the menu
# Implement each feature
```

### Sample Output:
```
========================================
Shopping List Manager
========================================
1. Add item
2. Remove item
3. View list
4. Clear list
5. Quit
========================================
Choose an option (1-5): 1
Enter item to add: Milk
Added: Milk

Your shopping list (1 item):
- Milk
```

### Extension Ideas:
- Add quantities for each item
- Sort list alphabetically
- Save/load list from file (later lesson)
- Add item categories

---

## 🌟 Project 7: Contact Book

**Prerequisites:** Lessons 1-9 (All above + Functions)
**Difficulty:** ⭐⭐⭐ Advanced
**Time:** 45-60 minutes

### What You'll Build:
A contact management system using functions to organize code.

### Features:
1. Add new contacts (name, phone, email)
2. Search for contacts by name
3. Display all contacts
4. Delete contacts
5. Update contact information
6. Well-organized with functions

### Starter Code:
```python
# Contact Book

contacts = []

def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("Contact Book")
    print("=" * 40)
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Delete contact")
    print("5. Quit")
    print("=" * 40)

def add_contact():
    """Add a new contact to the list"""
    # Your code here
    pass

def search_contact():
    """Search for a contact by name"""
    # Your code here
    pass

def view_all_contacts():
    """Display all contacts"""
    # Your code here
    pass

def delete_contact():
    """Remove a contact from the list"""
    # Your code here
    pass

# Main program loop
# Your code here!
```

### Sample Output:
```
========================================
Contact Book
========================================
1. Add contact
2. Search contact
3. View all contacts
4. Delete contact
5. Quit
========================================
Choose an option (1-5): 1

Enter name: Connor O'Malley
Enter phone: 555-1234
Enter email: connor@example.com

Contact added successfully!

You have 1 contact(s) saved.
```

### Extension Ideas:
- Add more fields (address, birthday)
- Export contacts to CSV
- Import contacts from file
- Add categories/tags

---

## 🌟 Project 8: Quiz Game

**Prerequisites:** Lessons 1-10 (All lessons)
**Difficulty:** ⭐⭐⭐ Advanced
**Time:** 60-90 minutes

### What You'll Build:
A fully-featured quiz game with multiple questions, scoring, and feedback.

### Features:
1. Store questions in dictionaries
2. Ask multiple-choice questions
3. Track score
4. Give immediate feedback
5. Show final results
6. Calculate percentage

### Starter Code:
```python
# Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    # Add more questions!
]

def ask_question(question_dict):
    """Display a question and get user's answer"""
    # Your code here
    pass

def calculate_grade(score, total):
    """Calculate letter grade from score"""
    # Your code here
    pass

def display_results(score, total):
    """Show final quiz results"""
    # Your code here
    pass

# Main quiz logic
# Your code here!
```

### Sample Output:
```
========================================
Python Quiz Game
========================================
Answer all questions to test your knowledge!

Question 1 of 5:
What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid

Your answer: C
Correct! ✓

Question 2 of 5:
...

========================================
Quiz Complete!
========================================
You scored 4 out of 5 (80%)
Letter Grade: B

Good job!
```

### Extension Ideas:
- Load questions from a file
- Add difficulty levels
- Track high scores
- Add timer for each question
- Create categories of questions

---

## 🎓 Challenge Projects

### Super Challenge 1: Text Adventure Game
Combine ALL concepts to create an interactive story game.

### Super Challenge 2: Personal Budget Tracker
Track income and expenses with categories and reports.

### Super Challenge 3: Password Manager
Store and retrieve passwords securely (with encryption later).

### Super Challenge 4: Weather Data Analyzer
Process weather data and show trends (use mock data initially).

---

## 💡 Project Tips

**Before Starting:**
1. Read the entire project description
2. Plan your approach on paper
3. Break it into small steps
4. Start with the simplest version

**While Building:**
1. Test frequently - run code after small changes
2. Use print() to debug
3. Don't worry about perfection - get it working first
4. Add features incrementally

**After Completing:**
1. Test edge cases (empty inputs, large numbers, etc.)
2. Refactor - clean up your code
3. Add comments explaining tricky parts
4. Think of new features to add

**If You Get Stuck:**
1. Break the problem down smaller
2. Review relevant lessons
3. Print variables to see what's happening
4. Take a break and come back fresh

---

## 🏆 Track Your Projects

Keep a log of completed projects:
- [ ] Temperature Converter
- [ ] Simple Calculator
- [ ] Mad Libs Generator
- [ ] Grade Calculator
- [ ] Number Guessing Game
- [ ] Shopping List Manager
- [ ] Contact Book
- [ ] Quiz Game

---

**Remember:** These projects are YOUR code. Customize them, break them, rebuild them, and make them your own!

**Happy coding! 🚀**
