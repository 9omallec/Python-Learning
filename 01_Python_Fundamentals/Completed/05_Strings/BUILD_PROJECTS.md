# Build Projects: Strings

**Stop reading, start manipulating text**

---

## Available Tools for These Projects

**Concepts Available:** print(), variables, math, input(), strings, string methods, slicing

**NOT Available Yet:** if/else (Lesson 6)

---

## Project 1: Text Formatter (15 min)

**Goal:** Create a text formatting tool

**Requirements:**
- Ask user for text input
- Show text in multiple formats:
  - All uppercase
  - All lowercase
  - Title case
  - With extra spaces removed
- Display all versions nicely

**Example Interaction:**
```
Enter text:   hello WORLD from python

======= FORMATTED TEXT =======
Original: hello WORLD from python
Uppercase: HELLO WORLD FROM PYTHON
Lowercase: hello world from python
Title Case: Hello World From Python
Cleaned: hello WORLD from python
==============================
```

**Challenge:** Add word count and character count

---

## Project 2: Username Generator (20 min)

**Goal:** Generate username from full name

**Requirements:**
- Ask for first and last name
- Generate username (first initial + last name, lowercase)
- Remove spaces
- Show result

**Example Interaction:**
```
Enter first name: Connor
Enter last name: O'Malley

Suggested username: comalley
```

**Challenge:** Add numbers or allow user to choose format

---

## Project 3: Email Analyzer (20 min)

**Goal:** Analyze email address structure

**Requirements:**
- Ask for email address
- Show properties (don't validate as valid/invalid):
  - Count of @ symbols
  - Count of . symbols
  - Position of @ symbol (what character number)
  - Position of . symbol (what character number)
  - Show cleaned version (lowercase, no extra spaces)
- Display findings clearly

**Example Interaction:**
```
Enter email: Connor@EMAIL.COM

======= EMAIL ANALYSIS =======
Original: Connor@EMAIL.COM
Cleaned: connor@email.com

@ symbol count: 1
. symbol count: 1

@ position: character 7
. position: character 12

Cleaned email: connor@email.com
================================
```

**Challenge:** Show what comes before and after the @ symbol

---

## Project 4: Mad Libs Generator (25 min)

**Goal:** Interactive story with word replacement

**Requirements:**
- Ask for 8-10 words (nouns, verbs, adjectives)
- Create entertaining story using those words
- Format story nicely
- Use f-strings for clean formatting

**Example Interaction:**
```
Let's create a story!

Adjective: sparkly
Noun: computer
Verb: dancing
Animal: penguin
Food: pizza
Place: library
Name: Steve
Color: purple

======= YOUR STORY =======
One day, Steve went to the library
and found a sparkly computer.
While dancing, a purple penguin
appeared eating pizza!
It was the most amazing day ever!
==========================
```

**Challenge:** Create 3 different story templates, let user choose

---

## Project 5: Password Analyzer (25 min)

**Goal:** Analyze password properties

**Requirements:**
- Ask for password
- Show properties (don't judge as strong/weak):
  - Length in characters
  - Count of uppercase letters
  - Count of lowercase letters
  - Count of numbers (0-9)
  - Count of special characters (!@#$% etc)
- Display all findings clearly

**Example Interaction:**
```
Enter password: Hello123!

======= PASSWORD ANALYSIS =======
Length: 9 characters

Character counts:
- Uppercase letters: 1 (H)
- Lowercase letters: 4 (e, l, l, o)
- Numbers: 3 (1, 2, 3)
- Special characters: 1 (!)

==================================
```

**Challenge:** Show which special characters are present

---

## Project 6: Text Replacer Tool (20 min)

**Goal:** Find and replace words in text

**Requirements:**
- Ask for a sentence or paragraph
- Ask what word to replace
- Ask what to replace it with
- Show before and after
- Count how many replacements made

**Example Interaction:**
```
Enter text: I love Python and Python is great

Word to replace: Python
Replace with: JavaScript

Before: I love Python and Python is great
After: I love JavaScript and JavaScript is great

Replacements made: 2
```

**Challenge:** Make it case-insensitive

---

## Project 7: Name Badge Generator (20 min)

**Goal:** Create formatted name badges

**Requirements:**
- Ask for full name
- Ask for company
- Ask for job title
- Create nicely formatted badge
- Use proper capitalization
- Remove extra spaces

**Example Interaction:**
```
Full name: connor o'malley
Company: Tech Corp
Job title: developer

╔══════════════════════════╗
║      NAME BADGE          ║
╠══════════════════════════╣
║                          ║
║   Connor O'Malley        ║
║   Developer              ║
║   Tech Corp              ║
║                          ║
╚══════════════════════════╝
```

**Challenge:** Center-align the text

---

## Bonus Projects

### Bonus 1: Initials Extractor
Get full name, extract and display initials (C.O. for Connor O'Malley)

### Bonus 2: Word Counter
Count words, characters, sentences in text

### Bonus 3: Text Reverser
Reverse text or reverse each word

### Bonus 4: Vowel Remover
Remove all vowels from text

### Bonus 5: Case Inverter
Swap uppercase to lowercase and vice versa

### Bonus 6: Acronym Generator
Generate acronym from phrase (Be Right Back → BRB)

### Bonus 7: Email Privacy
Hide part of email (connor@email.com → c*****@email.com)

---

## Track Your Progress

```
Project 1: Text Formatter (14 min) ✓ - 2025-12-08
Project 2: Username Generator (18 min) ✓ - 2025-12-08
Project 3: Email Analyzer (22 min) ✓ - 2025-12-08
Project 4: Mad Libs (25 min) ✓ - 2025-12-08
Project 5: Password Analyzer (28 min) ✓ - 2025-12-08
```

Total: 5 projects, 107 min

---

## Ready to Move On When:

- [ ] Built at least 4 string manipulation projects
- [ ] Comfortable with string methods
- [ ] Can use f-strings naturally
- [ ] Understand slicing and indexing
- [ ] Can clean and format user input
- [ ] Projects took under 30 minutes each

---

## Common String Operations Cheat Sheet

**Changing case:**
```python
text.upper()        # UPPERCASE
text.lower()        # lowercase
text.title()        # Title Case
text.capitalize()   # First letter only
```

**Cleaning:**
```python
text.strip()        # Remove spaces from ends
text.replace(old, new)  # Replace text
```

**Checking:**
```python
"cat" in text       # Contains substring
text.startswith("H")  # Starts with
text.endswith("!")    # Ends with
text.isdigit()      # All numbers
text.isalpha()      # All letters
```

**Formatting:**
```python
f"Hello {name}"     # F-strings
len(text)           # Length
text[0]             # First character
text[-1]            # Last character
text[0:5]           # Slice
```

---

## Pro Tips

**Clean user input:**
```python
name = input("Name: ").strip().title()
email = input("Email: ").strip().lower()
```

**Chain methods:**
```python
text = "  HELLO  ".strip().lower()  # "hello"
```

**Use f-strings always:**
```python
# OLD way (don't do this)
print("Hello " + name + ", you are " + str(age))

# NEW way (do this)
print(f"Hello {name}, you are {age}")
```

---

## Projects Requiring if/else (Available in Lesson 6)

These projects were removed because they need conditional logic:

- **Email Validator** - Required if/else to check validity conditions
- **Password Checker** - Required if/else to evaluate strength ratings

Once you complete Lesson 6 (if/else statements), return to these projects to add validation and rating features!

---

**Remember:** Every app manipulates text. Master strings and you can build anything!
