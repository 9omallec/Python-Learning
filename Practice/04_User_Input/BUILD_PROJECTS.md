# Build Projects: User Input

**Stop reading, start interacting**

---

## Project 1: Personal Info Collector (15 min)

**Goal:** Ask user questions and create a profile

**Requirements:**
- Ask for at least 5 pieces of info (name, age, city, job, hobby)
- Store in variables
- Print a nicely formatted profile
- Use both string and number inputs

**Example Interaction:**
```
What is your name? Connor
How old are you? 35
What city do you live in? New York
What do you do? Developer
Favorite hobby? Coding

========== YOUR PROFILE ==========
Name: Connor
Age: 35 years old
Location: New York
Job: Developer
Hobby: Coding
==================================
```

**Challenge:** Calculate and show birth year

---

## Project 2: Interactive Calculator (20 min)

**Goal:** Build a calculator that asks for numbers

**Requirements:**
- Ask user for two numbers
- Perform all basic operations (+, -, *, /)
- Show all results
- Handle decimals properly

**Example Interaction:**
```
Enter first number: 24
Enter second number: 6

======= RESULTS =======
24.0 + 6.0 = 30.0
24.0 - 6.0 = 18.0
24.0 * 6.0 = 144.0
24.0 / 6.0 = 4.0
=======================
```

**Challenge:** Add //, %, and ** operations

---

## Project 3: Restaurant Bill Splitter (20 min)

**Goal:** Calculate how to split a restaurant bill

**Requirements:**
- Ask for bill amount
- Ask for tip percentage
- Ask for number of people
- Calculate tip
- Calculate total
- Calculate per-person amount
- Display itemized results

**Example Interaction:**
```
Enter bill amount: $85.50
Enter tip percentage: 18
How many people? 4

====== BILL SPLIT ======
Bill: $85.50
Tip (18%): $15.39
Total: $100.89

Splitting between 4 people:
Each person pays: $25.22
========================
```

**Challenge:** Add tax calculation

---

## Project 4: Temperature Converter (15 min)

**Goal:** Interactive temperature converter

**Requirements:**
- Ask if converting C to F or F to C
- Ask for temperature value
- Calculate conversion
- Display result clearly
- Use proper formulas

**Example Interaction:**
```
Convert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius?
Enter 1 or 2: 1
Enter temperature in Celsius: 25

25.0°C = 77.0°F
```

**Challenge:** Add Kelvin conversions

---

## Project 5: Simple Quiz Game (20 min)

**Goal:** Create an interactive quiz

**Requirements:**
- Ask at least 5 questions
- Mix different types (math, trivia, etc.)
- Keep score
- Tell user if each answer is right or wrong
- Show final score at end

**Example Interaction:**
```
=== QUIZ TIME ===

Question 1: What is 5 + 3?
Your answer: 8
Correct!

Question 2: What is the capital of France?
Your answer: Paris
Correct!

Question 3: What is 10 / 2?
Your answer: 5
Correct!

Final Score: 3/3 - Perfect!
```

**Challenge:** Give personalized feedback based on score

---

## Project 6: Mad Libs Story (20 min)

**Goal:** Interactive story generator

**Requirements:**
- Ask for at least 8 words (nouns, verbs, adjectives, etc.)
- Create a funny story using their words
- Format nicely
- Make it entertaining!

**Example Interaction:**
```
Let's create a story!

Enter a name: Bob
Enter an adjective: sparkly
Enter a place: cafeteria
Enter a verb: dancing
Enter an animal: penguin
Enter a food: pizza
Enter a number: 42
Enter a color: purple

=== YOUR STORY ===
One day, Bob went to the cafeteria.
They were dancing when suddenly a sparkly penguin appeared!
The penguin was eating pizza and wore 42 purple hats.
It was the strangest day ever!
==================
```

**Challenge:** Create multiple story templates

---

## Project 7: Unit Converter (25 min)

**Goal:** Multi-purpose unit converter

**Requirements:**
- Ask what type of conversion (distance, weight, volume)
- Ask for value to convert
- Ask for from/to units
- Calculate conversion
- Show result

**Example Interaction:**
```
=== UNIT CONVERTER ===
What to convert?
1. Distance (miles/km)
2. Weight (lbs/kg)
3. Temperature (F/C)

Choose: 1

Enter miles: 10
10.0 miles = 16.09 kilometers
```

**Challenge:** Add more conversion types

---

## Bonus Projects

### Bonus 1: BMI Calculator
Ask for height and weight, calculate BMI, give health category

### Bonus 2: Age Calculator
Ask for birth year, calculate age, show in years/months/days

### Bonus 3: Password Strength Checker
Ask for password, check length and give strength rating

### Bonus 4: Grade Calculator
Ask for multiple test scores, calculate average, show letter grade

### Bonus 5: Loan Calculator
Ask for loan amount, rate, term - calculate monthly payment

### Bonus 6: Shipping Cost Calculator
Ask for weight and distance, calculate shipping cost

### Bonus 7: Movie Ticket System
Ask for tickets, apply discounts, calculate total

---

## Track Your Progress

```
Project 1: Personal Info (14 min) ✓ - 2025-12-08
Project 2: Calculator (18 min) ✓ - 2025-12-08
Project 3: Bill Splitter (22 min) ✓ - 2025-12-08
Project 4: Temperature (15 min) ✓ - 2025-12-08
Project 5: Quiz Game (25 min) ✓ - 2025-12-08

Total: 5 projects, 94 min
```

---

## Ready to Move On When:

- [ ] Built at least 4 interactive programs
- [ ] Comfortable using input()
- [ ] Can convert strings to int/float
- [ ] Programs work with different user inputs
- [ ] Each project took under 25 minutes
- [ ] Your programs are actually interactive!

---

## Common Mistakes to Avoid:

**Forgetting to convert:**
```python
# WRONG
age = input("Age: ")
next_year = age + 1  # Error!

# RIGHT
age = int(input("Age: "))
next_year = age + 1
```

**Wrong conversion type:**
```python
# WRONG - using int for decimals
price = int(input("Price: "))  # Loses cents!

# RIGHT - use float for money
price = float(input("Price: "))
```

**Not testing:**
```python
# Test your program with:
# - Normal inputs
# - Decimal numbers
# - Large numbers
# - Different user responses
```

---

**Pro tip:** Every great app is interactive. You just learned how to get user input - that's HUGE!
