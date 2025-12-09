# Lesson 6: If/Else Statements (Build-First Approach)

**Total time: 60-75 minutes**

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Make decisions in your code
- Use if/elif/else statements
- Compare values with operators
- Build programs that respond to different inputs
- Validate user input

**Most importantly:** You'll BUILD 5+ decision-making programs!

---

## 🚀 Step 1: Micro-Lesson (5 minutes)

### The Basics:

**Basic if statement:**
```python
age = 20
if age >= 18:
    print("You're an adult")
```

**If/else:**
```python
password = input("Enter password: ")
if password == "secret":
    print("Access granted!")
else:
    print("Access denied")
```

**If/elif/else:**
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C or below")
```

**Comparison operators:**
- `==` (equal to)
- `!=` (not equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater or equal)
- `<=` (less or equal)

**That's enough!** Close this and build.

---

## 🛠️ Step 2: Build Your First Project (20 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Password Validator

**This is the KEY to learning!**
- Close this file
- Build from scratch
- Get stuck? Try for 15 min
- Then check [SYNTAX_REFERENCE.md](../../Resources/SYNTAX_REFERENCE.md)

**GO BUILD NOW!**

---

## 🔄 Step 3: Learn More (As Needed)

**Return ONLY if stuck after 15 min of trying**

### Logical Operators:

```python
# AND - both must be True
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")
```

```python
# OR - at least one must be True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work!")
```

```python
# NOT - reverses True/False
is_banned = False
if not is_banned:
    print("Welcome!")
```

### Nested If Statements:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Come in!")
    else:
        print("Need ID")
else:
    print("Too young")
```

### Common Mistakes:

```python
# WRONG - Using = instead of ==
if age = 18:  # Assignment, not comparison!

# RIGHT
if age == 18:
```

```python
# WRONG - Missing colon
if age > 18
    print("Adult")

# RIGHT
if age > 18:
    print("Adult")
```

```python
# WRONG - No indentation
if age > 18:
print("Adult")

# RIGHT
if age > 18:
    print("Adult")  # Must be indented!
```

**Now go back to building!**

---

## 🛠️ Step 4: Build More Projects (60 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 4 more:**
- Project 2: Age Verifier (15 min)
- Project 3: Grade Calculator (20 min)
- Project 4: Even/Odd Checker (15 min)
- Project 5 or higher: Your choice (25 min)

**Goal:** 5-6 decision-making programs completed

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

- [ ] Built 5+ projects with if/else
- [ ] Completed Active Recall cards
- [ ] Comfortable with if/elif/else
- [ ] Can use comparison operators correctly
- [ ] Can validate user input
- [ ] Fixed common errors (missing colon, = vs ==, indentation)

**Time invested:** 75-90 minutes
**Projects built:** 5-6
**Concepts mastered:** Conditional logic, comparisons, validation

---

## 🔄 Review Schedule

**Spaced repetition:**

- **Tomorrow (Day 2):** Review projects, add complexity
- **Next week (Day 8):** Rebuild password validator from memory
- **2 weeks (Day 17):** Use if/else in complex program
- **1 month (Day 36):** Quick review - should be automatic

**See:** [REVIEW_SCHEDULE.md](../../Resources/REVIEW_SCHEDULE.md)

---

## 🎯 Next Steps

**Ready for Lesson 7 when:**
- You've built 5+ conditional programs
- You can write if/elif/else from memory
- You understand boolean logic (and/or/not)
- You can validate user input

**Move to:** [Practice/07A_Basic_For_Loops/LESSON_GUIDE.md](../07A_Basic_For_Loops/LESSON_GUIDE.md)

---

## 💡 Tips for Success

**DO:**
- ✅ Test multiple conditions
- ✅ Use meaningful condition checks
- ✅ Give clear error messages
- ✅ Remember the colon!
- ✅ Indent properly

**DON'T:**
- ❌ Use = when you mean ==
- ❌ Forget the colon after if/elif/else
- ❌ Skip indentation
- ❌ Make overly complex nested ifs
- ❌ Forget to test edge cases

---

**You can now make your programs smart! They can decide, validate, and respond!** 🎯

**Stop reading. Build something that makes decisions. Now!**
