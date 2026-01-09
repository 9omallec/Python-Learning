# Lesson 8A: List Basics (Build-First Approach)

**Total time: 60-75 minutes**

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Create lists to store multiple values
- Access items using index numbers (positive and negative)
- Use list slicing to get portions of lists
- Loop through lists
- Check if items exist in lists
- Use common list functions (len, max, min, sum, count, index)

**Most importantly:** You'll BUILD 5+ programs that use lists!

---

## 🚀 Step 1: Micro-Lesson (5 minutes)

### The Basics:

**Creating a list:**
```python
fruits = ["apple", "banana", "orange"]
numbers = [10, 20, 30, 40, 50]
empty = []
```

**Accessing items (indexing starts at 0!):**
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple (first item)
print(fruits[1])   # banana (second item)
print(fruits[-1])  # orange (last item)
```

**Loop through a list:**
```python
for fruit in fruits:
    print(fruit)
```

**Check if item exists:**
```python
if "apple" in fruits:
    print("We have apples!")
```

**That's it!** Those 4 concepts unlock hundreds of programs.

---

## 🛠️ Step 2: Build 5 Quick Programs (35-45 min)

Open `BUILD_PROJECTS.md` and build:
1. **Favorite Things List** (10 min) - Store and display your favorites
2. **Score Tracker** (12 min) - Track game scores and find highest/lowest
3. **Shopping List Checker** (12 min) - Check if items are on your list
4. **Class Roster** (12 min) - Store names and access by number
5. **Number Analyzer** (15 min) - Analyze a list of numbers (sum, average, max, min)

**Don't read ahead!** Build each project yourself first.

---

## 📖 Step 3: Read lesson.py (10 minutes)

After building projects, read `lesson.py` to see:
- Different ways to create lists
- All the indexing techniques (positive, negative)
- List slicing syntax
- Common patterns you'll use all the time

**Why read after building?**
- You'll recognize patterns you already used
- You'll discover shortcuts
- New techniques make sense because you need them

---

## ✍️ Step 4: Experiment (10 minutes)

Open `practice.py` and try:

**Exercise 1: Index Practice**
```python
colors = ["red", "blue", "green", "yellow", "purple"]
# Print the first color
# Print the last color
# Print the middle color
```

**Exercise 2: Slice Practice**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get first 5 numbers
# Get last 3 numbers
# Get every other number
```

**Exercise 3: Loop Practice**
```python
names = ["Alice", "Bob", "Charlie", "Diana"]
# Print each name with "Hello, NAME!"
# Print each name with its index number
```

**Exercise 4: Analysis**
```python
test_scores = [88, 92, 75, 95, 82, 90, 78]
# Find the highest score
# Find the lowest score
# Calculate the average
# Count how many scores are above 85
```

---

## 🎯 Step 5: Active Recall (5 minutes)

Close everything and answer from memory:

1. How do you create a list in Python?
2. What index is the first item in a list?
3. How do you access the last item using negative indexing?
4. How do you loop through all items in a list?
5. How do you check if "banana" is in a fruits list?
6. What does `len(my_list)` return?
7. How do you get the first 3 items from a list?

Check your answers in `ACTIVE_RECALL.md`

---

## ✅ You're Done When:

- [ ] You built all 5 projects from BUILD_PROJECTS.md
- [ ] You can create a list and access any item
- [ ] You can loop through a list
- [ ] You can slice a list to get portions
- [ ] You can use len(), max(), min(), sum(), count()
- [ ] You understand positive and negative indexing

---

## 🎓 What's Next?

**Lesson 8B: List Methods** - Learn to modify lists (add, remove, sort, reverse)

**Remember:** Lists are everywhere in programming. Master the basics now!
