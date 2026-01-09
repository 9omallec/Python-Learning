# Build Projects: User Input

**Stop reading, start building**

**Concepts Available:** print(), variables, math, input(), type conversion
**NOT Available Yet:** if/else (Lesson 6), loops (Lesson 7)

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

**Challenge:** Calculate and show birth year (2025 - age)

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

## Project 4: Simple Survey (15 min)

**Goal:** Collect survey responses and display them

**Requirements:**
- Ask at least 5 survey questions
- Mix of text and number questions
- Store all responses
- Display a summary at the end
- Make it look organized

**Example Interaction:**
```
=== QUICK SURVEY ===

On a scale of 1-10, how happy are you? 8
What's your favorite food? Pizza
How many hours do you sleep? 7
What's your favorite color? Blue
How many books did you read this year? 12

=== SURVEY RESULTS ===
Happiness Level: 8/10
Favorite Food: Pizza
Sleep Hours: 7 hours
Favorite Color: Blue
Books Read: 12 books

Thanks for participating!
```

**Challenge:** Calculate some statistics (average of numbers)

---

## Project 5: Recipe Scaler (15 min)

**Goal:** Scale recipe ingredients based on servings

**Requirements:**
- Ask how many servings they want
- Show original recipe (serves 4)
- Calculate and show scaled amounts
- Include at least 5 ingredients

**Example Interaction:**
```
=== RECIPE SCALER ===

Original Recipe (serves 4):
- 2 cups flour
- 1 cup sugar
- 4 eggs
- 0.5 cup butter
- 2 tsp vanilla

How many servings do you want? 8

=== SCALED RECIPE (serves 8) ===
- 4.0 cups flour
- 2.0 cups sugar
- 8.0 eggs
- 1.0 cups butter
- 4.0 tsp vanilla
```

**Challenge:** Add metric conversions (cups to ml)

---

## Project 6: Travel Distance Calculator (15 min)

**Goal:** Calculate travel times and distances

**Requirements:**
- Ask for distance in miles
- Ask for speed in mph
- Calculate travel time
- Show distance in kilometers
- Show time in hours and minutes

**Example Interaction:**
```
Enter distance (miles): 150
Enter speed (mph): 60

=== TRAVEL INFO ===
Distance: 150 miles (241.4 km)
Speed: 60 mph
Travel Time: 2.5 hours (2 hours 30 minutes)
```

**Challenge:** Calculate fuel needed (ask for MPG)

---

## Project 7: Shopping List Price Total (15 min)

**Goal:** Calculate total cost of shopping items

**Requirements:**
- Ask for 5 item names and prices
- Calculate subtotal
- Calculate tax (ask for tax rate)
- Calculate final total
- Display itemized list

**Example Interaction:**
```
Enter item 1 name: Bread
Enter item 1 price: 2.99

Enter item 2 name: Milk
Enter item 2 price: 3.49

Enter item 3 name: Eggs
Enter item 3 price: 4.29

Enter item 4 name: Cheese
Enter item 4 price: 5.99

Enter item 5 name: Butter
Enter item 5 price: 4.49

Tax rate (%): 7

=== SHOPPING RECEIPT ===
Bread:        $2.99
Milk:         $3.49
Eggs:         $4.29
Cheese:       $5.99
Butter:       $4.49
-------------------
Subtotal:    $21.25
Tax (7%):     $1.49
-------------------
TOTAL:       $22.74
```

**Challenge:** Calculate change from $50

---

## Bonus Projects

### Bonus 1: Age Calculator
Ask for birth year, calculate age, show in years/months (estimate)

### Bonus 2: Loan Payment Display
Ask for loan amount, rate, term - display monthly payment (formula given)

### Bonus 3: Height Converter
Ask for height in inches, show in feet/inches and centimeters

### Bonus 4: Weight Tracker
Ask for start weight and current weight, calculate difference and percentage

### Bonus 5: Class Grade Average
Ask for 5 test scores, calculate and display average

### Bonus 6: Paycheck Calculator
Ask for hourly rate and hours worked, calculate gross pay and estimated take-home (70%)

### Bonus 7: Savings Goal Tracker
Ask for goal amount and monthly savings, calculate months needed

---

## Projects REMOVED (Require if/else - Coming in Lesson 6!)

These projects are GREAT but need conditional logic you haven't learned yet:

- ~~Quiz Game~~ → Moved to Lesson 6
- ~~Unit Converter with Menu~~ → Moved to Lesson 6
- ~~BMI with Categories~~ → Moved to Lesson 6
- ~~Password Strength Checker~~ → Moved to Lesson 6
- ~~Grade Calculator with Letter Grades~~ → Moved to Lesson 6

Don't worry - you'll build these soon after learning if/else!

---

## Track Your Progress

```
Project 1: Info Collector   ( __ min) □
Project 2: Calculator       ( __ min) □
Project 3: Bill Splitter    ( __ min) □
Project 4: Survey           ( __ min) □
Project 5: Recipe Scaler    ( __ min) □
Project 6: Travel Calc      ( __ min) □
Project 7: Shopping Total   ( __ min) □

Total: ___ projects, ___ minutes
```

---

## Ready to Move On When:

- [ ] Built at least 4 interactive programs
- [ ] Comfortable using input()
- [ ] Can convert strings to int/float
- [ ] Programs work with different user inputs
- [ ] Each project took under 25 minutes
- [ ] Your programs actually interact!

---

## Common Mistakes to Avoid:

**Forgetting to convert:**
```python
# WRONG
age = input("Age: ")
next_year = age + 1  # Error! Can't add to string

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

**Note:** This lesson ONLY uses concepts from Lessons 1-4. All projects can be completed without if/else or loops!
