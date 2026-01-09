# Lesson 3: Math Operations (Build-First Approach)

**Total time: 60 minutes**

---

## What You'll Learn

By the end of this lesson, you'll be able to:
- Use all Python math operators
- Apply order of operations correctly
- Build real-world calculators
- Solve calculation problems with code

**Most importantly:** You'll BUILD 4-5 working calculator programs today!

---

## The Build-First Method

**DON'T:**
- Read about math operators for 30 minutes
- Memorize operator precedence tables
- Do worksheet problems by hand

**DO:**
- Learn 3 operators (5 min)
- Build a calculator immediately (15 min)
- Learn more operators as needed
- Build more projects!

---

## Step 1: Micro-Lesson (5 minutes)

### The Essential Operators:

**Basic Math:**
```python
print(10 + 5)   # Addition: 15
print(10 - 5)   # Subtraction: 5
print(10 * 5)   # Multiplication: 50
print(10 / 5)   # Division: 2.0
```

**Variables:**
```python
price = 20
tax = price * 0.08  # 8% tax
total = price + tax
print(total)  # 21.6
```

**That's enough to start!** Close this file and build your first calculator.

---

## Step 2: Build Your First Project (15 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Basic Calculator

**Rules:**
- Close this guide
- Build from scratch
- Struggle for 10 min if stuck
- Then look up what you need

**START BUILDING NOW!**

---

## Step 3: Learn More (As Needed)

**Come back here ONLY if stuck after trying for 10+ minutes**

### More Operators:

**Floor Division (get whole number):**
```python
print(17 / 5)   # 3.4 (regular division)
print(17 // 5)  # 3 (floor division - drops decimal)
```

**Modulo (get remainder):**
```python
print(17 % 5)   # 2 (remainder when 17 divided by 5)
print(20 % 4)   # 0 (no remainder - divides evenly)
```

**Exponents (power):**
```python
print(2 ** 3)   # 8 (2 to the power of 3 = 2×2×2)
print(5 ** 2)   # 25 (5 squared)
```

### Order of Operations (PEMDAS):

```python
print(2 + 3 * 4)        # 14 (multiplication first)
print((2 + 3) * 4)      # 20 (parentheses first)
print(10 + 5 * 2 ** 2)  # 30 (2²=4, 5*4=20, 10+20=30)
```

### Compound Operators:

```python
score = 100
score += 10    # Same as: score = score + 10
score -= 5     # Same as: score = score - 5
score *= 2     # Same as: score = score * 2
score /= 4     # Same as: score = score / 4
```

### Common Errors:

```python
# WRONG - Division by zero
result = 10 / 0  # Error!

# WRONG - Using ^ for exponents
print(2 ^ 3)  # This is XOR, not power!

# RIGHT - Use ** for exponents
print(2 ** 3)  # 8
```

**Now go back to building!**

---

## Step 4: Build More Projects (40 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 3 of these:**
- Project 2: Restaurant Bill Calculator (20 min)
- Project 3: Temperature Converter (15 min)
- Project 4: Circle Calculator (20 min)
- Project 5: Time Converter (20 min)

**Goal:** Have 4 working calculator programs by end of lesson

---

## Step 5: Active Recall (10 minutes)

**Open:** [ACTIVE_RECALL.md](ACTIVE_RECALL.md)

**Test yourself:**
- Answer cards WITHOUT looking first
- Focus on operators you find tricky
- Check your understanding of //, %, **

**This locks in your learning!**

---

## Step 6: Practice Exercises (Optional)

**If you have extra time:**

**Open:** [practice.py](practice.py)

**Do:** As many exercises as you want (max 20 min)

**Remember:** Projects > exercises for learning!

---

## Lesson Complete When:

- [ ] Built at least 4 calculator projects
- [ ] Completed Active Recall cards
- [ ] Understand all 6 operators (+, -, *, /, //, %, **)
- [ ] Can apply order of operations
- [ ] Know when to use // vs / and what % does

**Time invested:** 60-75 minutes
**Projects built:** 4-5 calculators
**Concepts mastered:** All math operators, PEMDAS

---

## Review Schedule

**Follow spaced repetition:**

- **Day 2:** Modify one calculator to add new features
- **Day 8:** Build a new calculator from memory
- **Day 17:** Combine math operations with user input (next lesson!)
- **Day 36:** Quick review - should be automatic now

---

## Real-World Applications

**You now know how to build:**
- Financial calculators (bills, loans, budgets)
- Unit converters (temperature, distance, time)
- Scientific calculators (area, volume, physics)
- E-commerce tools (discounts, tax, shipping)
- Fitness trackers (BMI, calories, pace)

**Every app uses these math operations!**

---

## Next Steps

**You're ready for Lesson 4 when:**
- Built 4+ calculator programs
- Comfortable with all operators
- Can solve calculation problems quickly
- Ready to make calculators interactive

**Move to:** [Practice/04_User_Input/LESSON_GUIDE.md](../04_User_Input/LESSON_GUIDE.md)

---

## Quick Reference

### All Operators:
```python
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division (always decimal)
//  # Floor division (whole number)
%   # Modulo (remainder)
**  # Exponent (power)
```

### Order of Operations (PEMDAS):
1. **P**arentheses ()
2. **E**xponents **
3. **M**ultiplication * and **D**ivision / (left to right)
4. **A**ddition + and **S**ubtraction - (left to right)

### Compound Operators:
```python
+=  -=  *=  /=  //=  %=  **=
```

---

## Tips for Success

**DO:**
- ✅ Build calculators immediately
- ✅ Test with different numbers
- ✅ Use parentheses when in doubt
- ✅ Print intermediate results to debug
- ✅ Solve real problems (bills, conversions, etc.)

**DON'T:**
- ❌ Just read about operators
- ❌ Memorize without applying
- ❌ Skip the building projects
- ❌ Forget order of operations
- ❌ Use / when you need //

---

**Remember:** Math operations are the foundation of programming. Every app calculates something!

**Stop reading. Start calculating. Build now!**
