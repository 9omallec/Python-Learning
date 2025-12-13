# Lesson 8B: List Methods (Build-First Approach)

**Total time: 60-75 minutes**

---

## 🎯 What You'll Learn

By the end of this lesson, you'll be able to:
- Add items to lists (append, insert, extend)
- Remove items from lists (remove, pop, del, clear)
- Change items in lists
- Sort and reverse lists
- Copy lists properly
- Combine lists
- Build dynamic lists with user input

**Most importantly:** You'll BUILD 5+ programs that modify lists!

---

## 🚀 Step 1: Micro-Lesson (5 minutes)

### The Basics:

**Add items:**
```python
fruits = ["apple"]
fruits.append("banana")      # Add to end
fruits.insert(0, "orange")   # Insert at position
```

**Remove items:**
```python
fruits.remove("banana")      # Remove by value
last = fruits.pop()          # Remove & return last
```

**Sort and reverse:**
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()               # Sort in place
numbers.reverse()            # Reverse in place
```

**Copy lists:**
```python
list2 = list1.copy()         # Make a real copy
```

---

## 🛠️ Step 2: Build 5 Quick Programs (35-45 min)

Open `BUILD_PROJECTS.md` and build:
1. **Dynamic To-Do List** (12 min) - Add/remove tasks
2. **Playlist Manager** (15 min) - Add songs, remove songs, reorder
3. **Inventory System** (12 min) - Track items, add/remove stock
4. **Leaderboard** (15 min) - Add scores and auto-sort
5. **Contact List** (15 min) - Add/remove/search contacts

**Don't read ahead!** Build each project yourself first.

---

## 📖 Step 3: Read lesson.py (10 minutes)

After building projects, read `lesson.py` to see:
- All the list methods (append, insert, extend, remove, pop, etc.)
- Difference between methods that modify vs. return new lists
- Common pitfalls (like copying lists incorrectly)
- Patterns you'll use constantly

---

## ✍️ Step 4: Experiment (10 minutes)

Open `practice.py` and try:

**Exercise 1: Building a List**
```python
# Start with empty list
numbers = []
# Add numbers 1-10 using a loop
# Print the list
```

**Exercise 2: Removing Items**
```python
fruits = ["apple", "banana", "orange", "grape", "mango"]
# Remove "orange"
# Remove the last item
# Remove the first item
# Print remaining list
```

**Exercise 3: Sorting**
```python
scores = [88, 92, 75, 95, 82]
# Sort scores lowest to highest
# Print sorted list
# Reverse to get highest to lowest
# Print reversed list
```

**Exercise 4: List Operations**
```python
# Create two lists of numbers
# Combine them into one list
# Sort the combined list
# Remove duplicates
# Print final list
```

---

## 🎯 Step 5: Active Recall (5 minutes)

Close everything and answer from memory - check `ACTIVE_RECALL.md`

---

## ✅ You're Done When:

- [ ] You built all 5 projects from BUILD_PROJECTS.md
- [ ] You can add items to lists (append, insert)
- [ ] You can remove items from lists (remove, pop)
- [ ] You can sort and reverse lists
- [ ] You understand the difference between sort() and sorted()
- [ ] You can copy lists properly

---

## 🎓 What's Next?

**Lesson 8C: List Comprehensions** - Learn advanced list techniques (optional but powerful!)

**Remember:** These methods give you full control over your lists!
