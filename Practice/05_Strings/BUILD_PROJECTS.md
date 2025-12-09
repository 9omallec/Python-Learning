# Build Projects: Strings

**Stop reading, start manipulating text**

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

## Project 3: Email Validator (20 min)

**Goal:** Basic email format checker

**Requirements:**
- Ask for email address
- Check if it contains @
- Check if it contains .
- Check if @ comes before .
- Tell user if format looks valid
- Convert to lowercase
- Remove extra spaces

**Example Interaction:**
```
Enter email: Connor@EMAIL.COM

Checking email...
✓ Contains @
✓ Contains .
✓ @ comes before .
✓ Format looks valid!

Cleaned email: connor@email.com
```

**Challenge:** Check for multiple @ symbols (invalid)

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

## Project 5: Password Checker (25 min)

**Goal:** Check if password meets requirements

**Requirements:**
- Ask for password
- Check length (minimum 8 characters)
- Check if contains numbers
- Check if contains uppercase letters
- Check if contains lowercase letters
- Give feedback on each requirement
- Show strength rating

**Example Interaction:**
```
Enter password: Hello123

Checking password strength...
✓ Length: 8 characters (minimum 8)
✓ Contains numbers
✓ Contains uppercase letters
✓ Contains lowercase letters

Password Strength: STRONG
```

**Challenge:** Check for special characters (!@#$%)

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
Project 3: Email Validator (22 min) ✓ - 2025-12-08
Project 4: Mad Libs (25 min) ✓ - 2025-12-08
Project 5: Password Checker (28 min) ✓ - 2025-12-08

Total: 5 projects, 107 min
```

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

**Remember:** Every app manipulates text. Master strings and you can build anything!
