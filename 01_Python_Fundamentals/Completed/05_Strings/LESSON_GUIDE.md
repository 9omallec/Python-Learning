# Lesson 5: Strings (Build-First Approach)

**Total time: 60 minutes**

---

## What You'll Learn

By the end of this lesson, you'll be able to:
- Manipulate text with string methods
- Format output beautifully with f-strings
- Slice and index strings
- Clean and validate user input
- Build text-processing tools

**Most importantly:** You'll BUILD 4-5 text-manipulation programs today!

---

## The Build-First Method

**DON'T:**
- Read about 20 string methods for 30 minutes
- Memorize method names
- Do boring string exercises

**DO:**
- Learn 3 essential methods (5 min)
- Build a text tool immediately (15 min)
- Learn more methods as needed
- Build more text projects!

---

## Step 1: Micro-Lesson (5 minutes)

### Essential String Methods:

**Case conversion:**
```python
name = "connor"
print(name.upper())      # CONNOR
print(name.capitalize()) # Connor
```

**Cleaning input:**
```python
text = "  hello  "
print(text.strip())  # "hello" (removes spaces)
```

**F-strings (best way to format):**
```python
name = "Connor"
age = 35
print(f"My name is {name} and I'm {age} years old")
```

**That's enough to start!** Close this file and build your first text tool.

---

## Step 2: Build Your First Project (15 minutes)

**Open:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build:** Project 1 - Text Formatter

**Rules:**
- Close this guide
- Build from scratch
- Test with different inputs
- Struggle 10 min if stuck, then look up methods

**START FORMATTING TEXT NOW!**

---

## Step 3: Learn More (As Needed)

**Come back here ONLY if stuck after trying for 10+ minutes**

### More String Methods:

**Replace text:**
```python
sentence = "I love cats"
new = sentence.replace("cats", "dogs")
print(new)  # "I love dogs"
```

**Case methods:**
```python
text = "Hello World"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
```

**Important:** String methods DON'T change the original!
```python
text = "hello"
text.upper()        # Creates "HELLO" but doesn't save it
print(text)         # Still "hello"

# To keep the change:
text = text.upper()
print(text)         # Now "HELLO"
```

### String Slicing and Indexing:

**Access characters:**
```python
word = "Python"
print(word[0])      # P (first character)
print(word[-1])     # n (last character)
```

**Slice strings:**
```python
text = "Hello World"
print(text[0:5])    # "Hello" (chars 0-4)
print(text[6:])     # "World" (from 6 to end)
print(text[:5])     # "Hello" (from start to 5)
```

### Checking Strings:

**Check if substring exists:**
```python
if "cat" in "I have a cat":
    print("Found cat!")
```

**String properties:**
```python
text = "Hello123"
print(len(text))         # 8 (length)
print(text.isdigit())    # False (not all numbers)
print(text.isalpha())    # False (contains numbers)
```

### F-Strings (Use These Always!):

**Basic usage:**
```python
name = "Connor"
age = 35
print(f"Hi, I'm {name} and I'm {age} years old")
```

**With expressions:**
```python
price = 19.99
print(f"Total with tax: ${price * 1.08}")
```

**Formatting numbers:**
```python
price = 19.99453
print(f"Price: ${price:.2f}")  # $19.99 (2 decimals)
```

### Common Patterns:

**Clean user input:**
```python
name = input("Name: ").strip().title()
email = input("Email: ").strip().lower()
```

**Chain methods:**
```python
text = "  HELLO world  "
result = text.strip().lower()  # "hello world"
```

**Concatenation:**
```python
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# But f-strings are better!
full = f"{first} {last}"
```

### Common Errors:

```python
# WRONG - Can't change strings directly
text = "hello"
text[0] = "H"  # Error! Strings are immutable

# RIGHT - Create new string
text = "H" + text[1:]  # "Hello"

# Or use methods
text = text.capitalize()  # "Hello"
```

**Now go back to building!**

---

## Step 4: Build More Projects (40 minutes)

**From:** [BUILD_PROJECTS.md](BUILD_PROJECTS.md)

**Build at least 3 of these:**
- Project 2: Username Generator (20 min)
- Project 3: Email Validator (20 min)
- Project 4: Mad Libs Generator (25 min)
- Project 5: Password Checker (25 min)

**Goal:** Have 4 text-manipulation programs by end of lesson

---

## Step 5: Active Recall (10 minutes)

**Open:** [ACTIVE_RECALL.md](ACTIVE_RECALL.md)

**Test yourself:**
- Answer cards WITHOUT looking first
- Focus on method names and usage
- Practice slicing syntax

**Solidify your string knowledge!**

---

## Step 6: Practice Exercises (Optional)

**If you have extra time:**

**Open:** [practice.py](practice.py)

**Do:** As many exercises as you want (max 20 min)

**Remember:** Text tools > exercises for learning!

---

## Lesson Complete When:

- [ ] Built at least 4 text-manipulation projects
- [ ] Completed Active Recall cards
- [ ] Comfortable with .upper(), .lower(), .strip(), .replace()
- [ ] Can use f-strings fluently
- [ ] Understand string slicing [start:end]
- [ ] Can clean and validate text input

**Time invested:** 60-75 minutes
**Projects built:** 4-5 text tools
**Concepts mastered:** String methods, f-strings, slicing, indexing

---

## Review Schedule

**Follow spaced repetition:**

- **Day 2:** Add features to your text tools
- **Day 8:** Build a new text formatter from memory
- **Day 17:** Combine strings with loops for more power
- **Day 36:** Quick review - should be second nature now

---

## Real-World Applications

**You now know how to build:**
- Text formatters and validators
- Username/password tools
- Email processors
- Data cleaners
- Content generators
- Form validators
- Text analyzers

**Every application processes text. This is fundamental!**

---

## Next Steps

**You're ready for Lesson 6 when:**
- Built 4+ text-manipulation tools
- String methods feel natural
- F-strings are your default
- Can slice and clean text confidently
- Ready to add decision-making logic

**Move to:** [Practice/06_If_Else/LESSON_GUIDE.md](../06_If_Else/LESSON_GUIDE.md)

---

## Quick Reference

### Essential Methods:
```python
text.upper()          # UPPERCASE
text.lower()          # lowercase
text.title()          # Title Case
text.capitalize()     # First letter only
text.strip()          # Remove end spaces
text.replace(old, new)  # Replace text
```

### Indexing and Slicing:
```python
text[0]        # First character
text[-1]       # Last character
text[0:5]      # Characters 0-4
text[2:]       # From index 2 to end
text[:5]       # From start to index 5
text[:]        # Entire string
```

### Checking:
```python
len(text)           # Length
"cat" in text       # Contains
text.startswith()   # Starts with
text.endswith()     # Ends with
text.isdigit()      # All numbers
text.isalpha()      # All letters
```

### F-Strings:
```python
f"Text with {variable}"
f"Math: {2 + 2}"
f"Price: ${price:.2f}"  # 2 decimals
```

---

## Tips for Success

**DO:**
- ✅ Use f-strings for all formatting
- ✅ Always .strip() user input
- ✅ Chain methods when it makes sense
- ✅ Test with edge cases (empty strings, spaces)
- ✅ Remember strings are immutable

**DON'T:**
- ❌ Use + for complex string formatting
- ❌ Forget that methods create new strings
- ❌ Try to modify strings in place
- ❌ Forget to save method results
- ❌ Mix up .strip() and .split()

---

## String Method Cheat Sheet

**Case:**
```python
.upper()        .lower()        .title()        .capitalize()
```

**Cleaning:**
```python
.strip()        .lstrip()       .rstrip()       .replace()
```

**Checking:**
```python
.startswith()   .endswith()     .isdigit()      .isalpha()
```

**Splitting/Joining:**
```python
.split()        # "a b c".split() → ["a", "b", "c"]
" ".join(list)  # ["a","b"] → "a b"
```

---

## Common Use Cases

**Clean user input:**
```python
name = input("Name: ").strip().title()
```

**Format display:**
```python
print(f"{name.upper()}: ${price:.2f}")
```

**Validate data:**
```python
if "@" in email and "." in email:
    print("Valid email format")
```

**Extract info:**
```python
first_name = full_name.split()[0]
last_name = full_name.split()[-1]
```

---

**Remember:** Text manipulation is everywhere. Master strings and build powerful tools!

**Stop reading. Start manipulating text. Build now!**
