# Build Projects: While Loops

**Create interactive programs that keep running**

---

## Project 1: Number Guessing Game (20 min)

**Goal:** Computer picks number, user guesses until correct

**Requirements:**
- Computer picks random number (1-100)
- User keeps guessing
- Give hints: "Too high!" or "Too low!"
- Count number of guesses
- Celebrate when correct

**Example Output:**
```
I'm thinking of a number between 1 and 100...

Your guess: 50
Too high!

Your guess: 25
Too low!

Your guess: 37
Too high!

Your guess: 31
🎉 Correct! You got it in 4 guesses!
```

**Bonus challenges:**
- Add difficulty levels (easy/medium/hard ranges)
- Track best score
- Let user play multiple rounds

**Hint:** `import random` then `random.randint(1, 100)`

---

## Project 2: Password Entry System (15 min)

**Goal:** Give user 3 attempts to enter correct password

**Requirements:**
- Set password in code
- Allow 3 attempts maximum
- Count attempts
- Lock account after 3 failed attempts
- Exit loop when correct password entered

**Example Output:**
```
Enter password: wrong1
Incorrect! 2 attempts remaining.

Enter password: wrong2
Incorrect! 1 attempt remaining.

Enter password: secret123
✓ Access granted! Welcome!

--- OR ---

Enter password: wrong3
❌ Account locked! No attempts remaining.
```

**Bonus:** Add username check too

---

## Project 3: Menu System (20 min)

**Goal:** Interactive menu that keeps running

**Requirements:**
- Display menu options
- Get user choice
- Perform action
- Loop back to menu
- Exit when user chooses quit

**Example Output:**
```
=== MAIN MENU ===
1. Calculate area
2. Convert temperature
3. Check even/odd
4. Quit

Enter choice: 1
Enter length: 5
Enter width: 3
Area: 15

=== MAIN MENU ===
1. Calculate area
2. Convert temperature
3. Check even/odd
4. Quit

Enter choice: 4
Goodbye!
```

**Bonus:** Add more menu options, handle invalid input

---

## Project 4: Input Validation Loop (15 min)

**Goal:** Keep asking until user gives valid input

**Requirements:**
- Ask for age (must be 1-120)
- Keep asking if invalid
- Don't accept negative, 0, or > 120
- Don't accept text
- Handle all errors gracefully

**Example Output:**
```
Enter your age: -5
Invalid! Age must be between 1 and 120.

Enter your age: abc
Invalid! Please enter a number.

Enter your age: 150
Invalid! Age must be between 1 and 120.

Enter your age: 25
✓ Valid! You are 25 years old.
```

**Bonus:** Create validation for other inputs (email, phone, etc)

---

## Project 5: ATM Withdrawal System (25 min)

**Goal:** Simulate ATM with balance tracking

**Requirements:**
- Starting balance: $1000
- Keep letting user withdraw
- Check if sufficient funds
- Update balance after each withdrawal
- Show balance after each transaction
- Continue until balance low or user quits

**Example Output:**
```
Balance: $1000

Enter withdrawal amount (or 0 to quit): $100
✓ Withdrawal successful!
New balance: $900

Enter withdrawal amount (or 0 to quit): $1500
❌ Insufficient funds!
Balance: $900

Enter withdrawal amount (or 0 to quit): $800
✓ Withdrawal successful!
New balance: $100

⚠️ Balance low! ($100 remaining)

Enter withdrawal amount (or 0 to quit): 0
Thank you for banking with us!
```

**Bonus:** Add deposit option, minimum balance warning

---

## Project 6: Sum Until Zero (15 min)

**Goal:** Keep adding numbers until user enters 0

**Requirements:**
- Ask for numbers one at a time
- Add each to running total
- Stop when user enters 0
- Show final sum
- Count how many numbers entered

**Example Output:**
```
Enter numbers (0 to stop):

Number: 10
Running total: 10

Number: 25
Running total: 35

Number: -5
Running total: 30

Number: 15
Running total: 45

Number: 0

Final sum: 45
Numbers entered: 4
Average: 11.25
```

**Bonus:** Calculate average, find min/max

---

## Project 7: Countdown with User Control (20 min)

**Goal:** Flexible countdown timer

**Requirements:**
- Ask user for starting number
- Count down to 1
- Ask if they want to continue or stop at each number
- User can quit anytime
- Show "Blast off!" at end

**Example Output:**
```
Start countdown from: 5

5... Continue? (y/n): y
4... Continue? (y/n): y
3... Continue? (y/n): n
Countdown stopped at 3.

--- OR ---

5... Continue? (y/n): y
4... Continue? (y/n): y
3... Continue? (y/n): y
2... Continue? (y/n): y
1... Continue? (y/n): y
🚀 BLAST OFF!
```

**Bonus:** Add time delay, dramatic effects

---

## Project 8: Simple Game Loop (25 min)

**Goal:** Create basic game that keeps running

**Requirements:**
- Player has 100 health
- Each round, random event happens
- Player gains or loses health
- Continue until health reaches 0 or player quits
- Track rounds survived

**Example Output:**
```
=== SURVIVAL GAME ===
Health: 100

Round 1: You found food! +20 health
Health: 120

Round 2: You fell down! -30 health
Health: 90

Round 3: You rested well! +10 health
Health: 100

Round 4: Bear attack! -80 health
Health: 20

⚠️ Low health!

Round 5: Poisoned water! -25 health
Health: -5

💀 Game Over!
You survived 5 rounds.
```

**Bonus:** Add choices, inventory, save high score

---

## Project 9: Calculator Loop (20 min)

**Goal:** Calculator that keeps running

**Requirements:**
- Show menu of operations
- Perform calculation
- Show result
- Ask if want to continue
- Keep memory of last result (optional)

**Example Output:**
```
=== CALCULATOR ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choose operation: 1
First number: 15
Second number: 7
Result: 22

Calculate again? (y/n): y

=== CALCULATOR ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choose operation: 3
First number: 8
Second number: 5
Result: 40

Calculate again? (y/n): n
Thanks for calculating!
```

**Bonus:** Chain calculations, use previous result

---

## Project 10: Shopping List Builder (25 min)

**Goal:** Build shopping list interactively

**Requirements:**
- Keep asking for items
- Add to list
- Show current list
- Allow removal of items
- Count total items
- Quit when done

**Example Output:**
```
=== SHOPPING LIST ===
1. Add item
2. View list
3. Remove item
4. Done

Choice: 1
Item: Milk
Added: Milk

Choice: 1
Item: Bread
Added: Bread

Choice: 2
Shopping List:
1. Milk
2. Bread
Total items: 2

Choice: 1
Item: Eggs
Added: Eggs

Choice: 4
Final Shopping List:
1. Milk
2. Bread
3. Eggs

Total: 3 items. Happy shopping!
```

**Bonus:** Check for duplicates, quantities, prices

---

## 🔄 Bonus Projects

### Bonus 1: Rock Paper Scissors
Play until user quits, track wins/losses

### Bonus 2: Word Chain Game
Each word must start with last letter of previous word

### Bonus 3: Coin Flip Simulator
Keep flipping, track heads/tails, stop at user command

### Bonus 4: Study Timer
Pomodoro-style timer with breaks

### Bonus 5: Character Creator
RPG-style, keep customizing until satisfied

---

## 📊 Track Your Progress

```
Project 1: Number Guessing Game (22 min) ✓
Project 2: Password Entry System (15 min) ✓
Project 3: Menu System (25 min) ✓
Project 4: Input Validation Loop (18 min) ✓
Project 5: ATM Withdrawal System (28 min) ✓

Total: 5 projects, 108 min
```

**Format:**
```
Project #: Name (time) ✓
Notes: What you learned, challenges faced
Infinite loop accidents: 2 (that's normal!)
```

---

## ✅ Ready to Move On When:

- [ ] Built at least 5 while loop projects
- [ ] Comfortable with while loop syntax
- [ ] Can use break and continue effectively
- [ ] Know how to prevent infinite loops
- [ ] Can validate user input with loops
- [ ] Built at least one menu system
- [ ] Understand when to use while vs for

---

## ⚠️ Debugging Infinite Loops

**If your program won't stop:**
1. Press `Ctrl + C` (or Cmd + C on Mac)
2. Check: Are you updating the loop condition?
3. Check: Does your condition ever become False?
4. Add print statements to see what's happening

**Common causes:**
- Forgot to update counter
- Condition can never be False
- Wrong comparison operator
- Variable name typo

---

**Remember:** While loops run WHILE something is true. Always have an exit!
