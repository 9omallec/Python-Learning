# Lesson 7B: While Loops (Build-First Approach)

**Total time: 60-75 minutes**

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Create loops that run until a condition is met
- Build interactive menus and games
- Validate user input with loops
- Use break and continue statements
- Prevent infinite loops
- Build programs that keep running until user quits

**Most importantly:** You'll BUILD 5+ programs with while loops!

---

## 🚀 Step 1: Micro-Lesson (5 minutes)

### The Basics:

**Basic while loop:**
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
# Prints: 1, 2, 3, 4, 5
```

**User-controlled loop:**
```python
answer = ""
while answer != "quit":
    answer = input("Type 'quit' to exit: ")
print("Goodbye!")
```

**Break statement (exit loop early):**
```python
while True:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break  # Exit loop
    print("Try again!")
```

**Continue statement (skip to next iteration):**
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip 3
    print(count)
# Prints: 1, 2, 4, 5 (skips 3)
```

**DANGER - Infinite loop:**
```python
# DON'T DO THIS!
while True:
    print("Forever!")  # Never stops!
# Always have a way to exit!
```

**That's enough!** Close this and build.

---

## 🛠️ Step 2: Build Your First Project (20 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Number Guessing Game

**This is the KEY to learning!**
- Close this file
- Build from scratch
- Get stuck? Try for 15 min
- Then check [SYNTAX_REFERENCE.md](../../Resources/SYNTAX_REFERENCE.md)

**GO BUILD NOW!**

---

## 🔄 Step 3: Learn More (As Needed)

**Return ONLY if stuck after 15 min of trying**

### While vs For Loops:

```python
# Use FOR when you know how many times
for i in range(10):
    print(i)

# Use WHILE when you don't know how many times
answer = ""
while answer != "done":
    answer = input("Enter 'done' to quit: ")
```

### Accumulating in While Loops:

```python
total = 0
number = 1
while number != 0:
    number = int(input("Enter number (0 to stop): "))
    total += number
print(f"Sum: {total}")
```

### Counters and Flags:

```python
# Counter
attempts = 0
while attempts < 3:
    password = input("Password: ")
    attempts += 1
    if password == "secret":
        print("Correct!")
        break

# Flag variable
running = True
while running:
    choice = input("Continue? (y/n): ")
    if choice == "n":
        running = False  # Exit loop
```

### Nested While Loops:

```python
# Outer loop
playing = True
while playing:
    # Inner loop
    guess = ""
    while guess != "correct":
        guess = input("Guess: ")

    again = input("Play again? (y/n): ")
    if again != "y":
        playing = False
```

### Common Mistakes:

```python
# WRONG - Forgetting to update condition
count = 1
while count <= 5:
    print(count)
    # Forgot: count += 1
# Infinite loop!

# RIGHT
count = 1
while count <= 5:
    print(count)
    count += 1  # Must update!
```

```python
# WRONG - Condition never becomes False
while 5 > 3:  # Always True!
    print("Forever")

# RIGHT
count = 0
while count < 5:  # Will eventually be False
    print(count)
    count += 1
```

```python
# WRONG - Off-by-one error
attempts = 0
while attempts < 3:
    print("Try")
    # Only runs 3 times, but attempts ends at 2!
    # If you want attempts to reach 3, need: attempts += 1

# RIGHT
attempts = 0
while attempts < 3:
    attempts += 1  # Increment first
    print(f"Attempt {attempts}")
```

**Now go back to building!**

---

## 🛠️ Step 4: Build More Projects (60 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 4 more:**
- Project 2: Password Entry System (15 min)
- Project 3: Menu System (20 min)
- Project 4: Input Validation Loop (15 min)
- Project 5 or higher: Your choice (25 min)

**Goal:** 5-6 while loop programs completed

---

## 🧠 Step 5: Active Recall (10 minutes)

**Open:** [ACTIVE_RECALL.md](ACTIVE_RECALL.md)

**Test yourself:**
- Answer questions WITHOUT looking first
- Check answers
- Identify gaps in knowledge
- Practice the ones you missed

**Critical step!** Active recall = long-term retention

---

## 📋 Step 6: Practice Exercises (Optional)

**If you have extra time:**

**Open:** [practice.py](practice.py)

**Time-box:** 20 minutes maximum

**Remember:** You learn more from projects!

---

## ✅ Lesson Complete When:

- [ ] Built 5+ projects with while loops
- [ ] Completed Active Recall cards
- [ ] Comfortable with while loop syntax
- [ ] Can use break and continue
- [ ] Understand how to avoid infinite loops
- [ ] Can validate user input with loops
- [ ] Built at least one menu system
- [ ] Fixed common errors (infinite loops, not updating condition)

**Time invested:** 75-90 minutes
**Projects built:** 5-6
**Concepts mastered:** While loops, break/continue, validation, menus

---

## 🔄 Review Schedule

**Spaced repetition:**

- **Tomorrow (Day 2):** Review projects, add complexity
- **Next week (Day 8):** Rebuild number guessing game from memory
- **2 weeks (Day 17):** Use while loops in complex program
- **1 month (Day 36):** Quick review - should be automatic

**See:** [REVIEW_SCHEDULE.md](../../Resources/REVIEW_SCHEDULE.md)

---

## 🎯 Next Steps

**Ready for Lesson 8 when:**
- You've built 5+ while loop programs
- You can write while loops from memory
- You understand break and continue
- You can validate input effectively
- You know when to use while vs for

**Move to:** [Practice/08_Lists/LESSON_GUIDE.md](../08_Lists/LESSON_GUIDE.md)

---

## 💡 Tips for Success

**DO:**
- ✅ Always update loop condition
- ✅ Use break for early exit
- ✅ Use continue to skip iterations
- ✅ Test for infinite loops (Ctrl+C to stop)
- ✅ Use while for unknown iterations

**DON'T:**
- ❌ Create infinite loops accidentally
- ❌ Forget to update counter/condition
- ❌ Use while when for is better
- ❌ Nest too many while loops
- ❌ Forget to give user way to exit

---

**You can now create interactive programs that keep running! Your code responds to users!** 🎯

**Stop reading. Build something interactive. Now!**
