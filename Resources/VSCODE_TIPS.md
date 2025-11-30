# VSCode Tips for Testing Code

## Problem: Testing Individual Exercises

You've been copying exercises to Test.py. Here's a better way!

---

## Method 1: Run Selected Code (BEST!)

**How to do it:**
1. Highlight the code you want to test
2. Right-click → "Run Selection/Line in Python Terminal"
3. Or press: `Shift + Enter`

**Example:**
```python
# In practice.py, highlight just these 2 lines:
for i in range(5):
    print("Connor")

# Press Shift + Enter
# Only those lines run!
```

**Pro:** No need to copy/paste to another file
**Con:** Terminal stays open with previous output

---

## Method 2: Use the Sandbox Folder

I've created a `Sandbox/` folder for you with:
- **scratch.py** - For testing code snippets
- **Test.py** - Your existing test file
- **new.py** - Your other test file

**Use scratch.py for quick tests:**
1. Copy exercise to scratch.py
2. Run the file
3. Clear it when done

---

## Method 3: Comment Out Everything Else

```python
# Practice 1: Print your name 5 times
# for i in range(5):
#     print("Connor")

# Practice 2: Print numbers from 0 to 9
for i in range(10):  # Only this runs
    print(i)

# Practice 3: Print numbers from 1 to 10
# for i in range(1, 11):
#     print(i)
```

**To comment multiple lines fast:**
1. Select the lines
2. Press `Ctrl + /`
3. They all get commented!

---

## Method 4: Run to Cursor (Advanced)

1. Right-click on a line
2. Select "Run to Cursor"
3. Only code up to that line executes

---

## My Recommendation

**For practice files:**
Use **Method 1** (Shift + Enter with selected code)

**For testing new ideas:**
Use **Sandbox/scratch.py**

**For bigger experiments:**
Create a new file in Projects/ folder

---

## Keyboard Shortcuts Reminder

- `Shift + Enter` - Run selected code
- `Ctrl + /` - Comment/uncomment lines
- `Ctrl + F5` - Run entire file
- **Ctrl + `** - Open/close terminal
- `Ctrl + S` - Save file

---

## New Folder Structure

```
Python Projects/
├── Practice/           ← All your lessons
├── Projects/           ← Your actual projects
├── Sandbox/            ← For testing/experimenting
│   ├── scratch.py      ← Quick tests
│   ├── Test.py
│   └── new.py
└── Resources/          ← Guides and trackers
    ├── PROGRESS.md
    ├── COMMON_MISTAKES.md
    ├── PROJECT_IDEAS.md
    ├── VSCODE_SHORTCUTS.md
    ├── VSCODE_TIPS.md (this file!)
    └── Weekly Challenges/
```

---

## Terminal Tips

**Clear the terminal:**
- Windows: `cls`
- Mac/Linux: `clear`
- Or click the trash icon in terminal

**Stop a running program:**
- Press `Ctrl + C`

**Run a specific file:**
```bash
python Sandbox/scratch.py
python Practice/07A_Basic_For_Loops/practice.py
```

---

**Try it now!** Open any practice file, highlight just one exercise, and press `Shift + Enter`!
