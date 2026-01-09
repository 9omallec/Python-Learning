# Lesson 7A: For Loops (Build-First Approach)

**Total time: 60-75 minutes**

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Repeat code automatically with for loops
- Use range() to control iterations
- Build countdown timers and number patterns
- Generate multiplication tables
- Create pattern printers
- Accumulate values (sum, product)

**Most importantly:** You'll BUILD 5+ programs that use repetition!

---

## 🚀 Step 1: Micro-Lesson (5 minutes)

### The Basics:

**Basic for loop:**
```python
for i in range(5):
    print(i)
# Prints: 0, 1, 2, 3, 4
```

**Different range patterns:**
```python
# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count by 2s
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Countdown
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

**Accumulating values:**
```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)  # 15 (sum of 1+2+3+4+5)
```

**range() syntax:**
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8
- `range(start, stop, step)`

**That's enough!** Close this and build.

---

## 🛠️ Step 2: Build Your First Project (20 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Countdown Timer

**This is the KEY to learning!**
- Close this file
- Build from scratch
- Get stuck? Try for 15 min
- Then check [SYNTAX_REFERENCE.md](../../Resources/SYNTAX_REFERENCE.md)

**GO BUILD NOW!**

---

## 🔄 Step 3: Learn More (As Needed)

**Return ONLY if stuck after 15 min of trying**

### Loop Variables:

```python
# You can use any variable name
for number in range(1, 6):
    print(number)

for count in range(10):
    print("Repeat this!")
```

### Nested Loops:

```python
# Loop inside a loop
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()  # New line after each row

# Output:
# *****
# *****
# *****
```

### Building Strings in Loops:

```python
result = ""
for i in range(1, 6):
    result = result + str(i) + " "
print(result)  # "1 2 3 4 5 "
```

### Common Patterns:

```python
# Sum of numbers
total = 0
for i in range(1, 101):
    total += i  # Same as: total = total + i
print(f"Sum: {total}")

# Count something
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")
```

### Common Mistakes:

```python
# WRONG - Forgetting the colon
for i in range(5)
    print(i)

# RIGHT
for i in range(5):
    print(i)
```

```python
# WRONG - Not indenting the loop body
for i in range(5):
print(i)

# RIGHT
for i in range(5):
    print(i)  # Must be indented!
```

```python
# WRONG - range(10, 1) won't count down
for i in range(10, 1):
    print(i)  # Prints nothing!

# RIGHT - Need negative step
for i in range(10, 0, -1):
    print(i)  # Counts down!
```

**Now go back to building!**

---

## 🛠️ Step 4: Build More Projects (60 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 4 more:**
- Project 2: Times Table Generator (15 min)
- Project 3: Sum Calculator (15 min)
- Project 4: Star Pattern Printer (20 min)
- Project 5 or higher: Your choice (25 min)

**Goal:** 5-6 loop programs completed

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

- [ ] Built 5+ projects with for loops
- [ ] Completed Active Recall cards
- [ ] Comfortable with range() function
- [ ] Can write loops that count up and down
- [ ] Can accumulate values (sum, count)
- [ ] Can print patterns with loops
- [ ] Fixed common errors (missing colon, indentation, range direction)

**Time invested:** 75-90 minutes
**Projects built:** 5-6
**Concepts mastered:** For loops, range(), accumulation, patterns

---

## 🔄 Review Schedule

**Spaced repetition:**

- **Tomorrow (Day 2):** Review projects, add complexity
- **Next week (Day 8):** Rebuild countdown timer from memory
- **2 weeks (Day 17):** Use for loops in complex program
- **1 month (Day 36):** Quick review - should be automatic

**See:** [REVIEW_SCHEDULE.md](../../Resources/REVIEW_SCHEDULE.md)

---

## 🎯 Next Steps

**Ready for Lesson 7B when:**
- You've built 5+ for loop programs
- You can write range() from memory
- You understand counting patterns
- You can use loops to accumulate values

**Move to:** [Practice/07B_While_Loops/LESSON_GUIDE.md](../07B_While_Loops/LESSON_GUIDE.md)

---

## 💡 Tips for Success

**DO:**
- ✅ Use descriptive loop variable names
- ✅ Test your range values
- ✅ Use end="" for printing on same line
- ✅ Remember the colon!
- ✅ Indent loop body

**DON'T:**
- ❌ Forget the colon after for statement
- ❌ Skip indentation
- ❌ Use range(10, 1) expecting countdown
- ❌ Modify loop variable inside loop (usually)
- ❌ Create infinite loops (use while for that!)

---

**You can now repeat actions automatically! Your code just got 10x more powerful!** 🎯

**Stop reading. Build something that repeats. Now!**
