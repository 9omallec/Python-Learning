# Build Projects: List Methods

**Modify and manipulate lists dynamically**

---

## Project 1: Dynamic To-Do List (12 min)

**Goal:** Create a to-do list that can add and remove tasks

**Requirements:**
- Start with 3 tasks in a list
- Add 2 more tasks using append()
- Remove a completed task using remove()
- Remove the last task using pop()
- Display the final list with numbers

**Example Output:**
```
Initial Tasks:
1. Buy groceries
2. Clean room
3. Study Python

Adding tasks...
✓ Added: Call mom
✓ Added: Do laundry

Completed task: Buy groceries
Removed last task: Do laundry

Final To-Do List:
1. Clean room
2. Study Python
3. Call mom
```

**Bonus challenges:**
- Let user add tasks with input()
- Let user mark tasks complete by number
- Show how many tasks remaining

---

## Project 2: Playlist Manager (15 min)

**Goal:** Manage a music playlist (add, remove, reorder)

**Requirements:**
- Start with 5 songs in a playlist
- Add a new song to the end
- Insert a song at position 2
- Remove a song the user doesn't like
- Sort the playlist alphabetically
- Reverse the playlist
- Display playlist with numbers each time

**Example Output:**
```
🎵 Original Playlist:
1. Thunder
2. Believer
3. Radioactive
4. Demons
5. Warriors

Added "Natural" to end
Inserted "Whatever It Takes" at position 2
Removed "Demons"

Alphabetical order:
1. Believer
2. Natural
3. Radioactive
4. Thunder
5. Warriors
6. Whatever It Takes

Reversed:
1. Whatever It Takes
2. Warriors
3. Thunder
...
```

**Bonus challenges:**
- Shuffle the playlist (random.shuffle)
- Let user swap two songs
- Create a "recently played" list using pop and insert

---

## Project 3: Inventory System (12 min)

**Goal:** Track store inventory (add/remove items)

**Requirements:**
- Start with 5-7 items in stock
- "Sell" 3 items (remove them)
- Restock 2 items (add them back)
- Add a new item to inventory
- Sort items alphabetically
- Show item count

**Example Output:**
```
📦 Starting Inventory:
- apples
- bananas
- oranges
- milk
- bread
- eggs
Total items: 6

SOLD: oranges
SOLD: milk
SOLD: eggs

RESTOCKED: milk
RESTOCKED: eggs

NEW ITEM: cheese

Final Inventory (sorted):
- apples
- bananas
- bread
- cheese
- eggs
- milk
Total items: 6
```

**Bonus challenges:**
- Track quantities (use parallel lists or dictionaries later)
- Check if item exists before removing
- Prevent negative inventory

---

## Project 4: Leaderboard (15 min)

**Goal:** Game leaderboard that auto-sorts scores

**Requirements:**
- Start with 5 player scores in a list
- Add 3 new scores
- Sort scores from highest to lowest
- Display top 3 players
- Display bottom 3 players
- Show the median score

**Example Output:**
```
🏆 LEADERBOARD 🏆

Initial Scores:
[450, 320, 580, 410, 290]

New scores added: 510, 380, 625

All Scores (high to low):
1. 625 ⭐
2. 580 ⭐
3. 510 ⭐
4. 450
5. 410
6. 380
7. 320
8. 290

Top 3: [625, 580, 510]
Bottom 3: [320, 290]
Median Score: 430
```

**Bonus challenges:**
- Add player names (use two parallel lists)
- Calculate average of top 3
- Remove lowest score

---

## Project 5: Contact List Manager (15 min)

**Goal:** Manage a contact list (add, remove, search, sort)

**Requirements:**
- Start with 5 contacts (names)
- Add 2 new contacts
- Remove a contact
- Sort contacts alphabetically
- Search for a contact (check if exists)
- Display total contacts
- Show first and last alphabetically

**Example Output:**
```
📇 CONTACTS

Starting contacts:
- Alice
- Charlie
- Bob
- Diana
- Ethan

Added: Frank
Added: Grace
Removed: Charlie

Sorted contacts:
1. Alice
2. Bob
3. Diana
4. Ethan
5. Frank
6. Grace

Search for "Bob": ✓ Found!
Search for "Charlie": ✗ Not found

Total contacts: 6
First: Alice
Last: Grace
```

**Bonus challenges:**
- Add phone numbers (parallel list)
- Find contacts starting with a letter
- Reverse alphabetical display

---

## 🔄 Bonus Projects

### Bonus 1: Stack/Queue Simulator
Use append() and pop(0) to simulate data structures

### Bonus 2: Undo Feature
Store history of changes, pop to undo

### Bonus 3: List Merger
Combine two lists, remove duplicates, sort

### Bonus 4: Priority Task List
Sort tasks by priority number

### Bonus 5: Card Deck
Create deck, shuffle, deal cards (pop from deck)

---

## 📊 Track Your Progress

```
Project 1: Dynamic To-Do List (12 min) ☐
Project 2: Playlist Manager (15 min) ☐
Project 3: Inventory System (12 min) ☐
Project 4: Leaderboard (15 min) ☐
Project 5: Contact List Manager (15 min) ☐

Total: 5 projects, ~69 min
```

---

## ✅ Ready to Move On When:

- [ ] Built at least 3 of the core projects
- [ ] Can add items (append, insert)
- [ ] Can remove items (remove, pop)
- [ ] Can sort and reverse lists
- [ ] Understand in-place vs. returning new lists

---

**Remember:** These methods are what make lists so powerful for real programs!
