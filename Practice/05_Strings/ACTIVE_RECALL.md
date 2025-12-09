# Active Recall Cards: Strings

**Test yourself BEFORE looking at answers**

---

## Card 1: String Methods

**Q: What will each of these print?**

```python
text = "Hello World"
print(text.upper())
print(text.lower())
print(text)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
HELLO WORLD
hello world
Hello World
```

**Key points:**
- `.upper()` converts to uppercase
- `.lower()` converts to lowercase
- Original string is UNCHANGED
- Methods create NEW strings
</details>

---

## Card 2: Strip Method

**Q: What does strip() do?**

```python
name = "   Connor   "
clean = name.strip()
print(clean)
```

<details>
<summary>Click to reveal answer</summary>

**Output:** `Connor` (no spaces)

**What strip() does:**
- Removes spaces from beginning and end
- Does NOT remove spaces in the middle
- Very useful for cleaning user input!

**Examples:**
```python
"  hello  ".strip()    # "hello"
"  hi there  ".strip() # "hi there" (middle space stays)
"\ntest\n".strip()     # "test" (removes newlines too)
```
</details>

---

## Card 3: Replace Method

**Q: What will this print?**

```python
sentence = "I love cats"
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)
print(sentence)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
I love dogs
I love cats
```

**Key points:**
- `.replace(old, new)` replaces text
- Original string is unchanged
- Must store result in variable to keep it
</details>

---

## Card 4: String Concatenation

**Q: What will this print?**

```python
first = "Hello"
last = "World"
print(first + " " + last)
print(first * 3)
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
Hello World
HelloHelloHello
```

**String operations:**
- `+` joins strings (concatenation)
- `*` repeats strings
- Remember to add spaces manually!
</details>

---

## Card 5: F-Strings

**Q: Rewrite using f-strings:**

```python
name = "Connor"
age = 35
print("My name is " + name + " and I am " + str(age) + " years old")
```

<details>
<summary>Click to reveal answer</summary>

```python
name = "Connor"
age = 35
print(f"My name is {name} and I am {age} years old")
```

**Why f-strings are better:**
- Cleaner and more readable
- No need to convert numbers with str()
- Can put any expression in {}
- Much easier to write!
</details>

---

## Card 6: String Indexing

**Q: What will these print?**

```python
word = "Python"
print(word[0])
print(word[3])
print(word[-1])
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
P
h
n
```

**Indexing rules:**
- First character is [0]
- Negative numbers count from end
- -1 is last character

**Full breakdown:**
```
P  y  t  h  o  n
0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```
</details>

---

## Card 7: String Slicing

**Q: What will this print?**

```python
text = "Hello World"
print(text[0:5])
print(text[6:])
print(text[:5])
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
Hello
World
Hello
```

**Slicing syntax:** `[start:end]`
- Start is included
- End is NOT included
- Empty start means "from beginning"
- Empty end means "to end"

**More examples:**
```python
text[0:5]   # "Hello" (characters 0-4)
text[6:11]  # "World"
text[6:]    # "World" (from 6 to end)
text[:5]    # "Hello" (from start to 5)
text[:]     # "Hello World" (entire string)
```
</details>

---

## Card 8: Fix the Bug

**Q: Why doesn't this work?**

```python
text = "hello"
text[0] = "H"  # Try to change first letter
print(text)
```

<details>
<summary>Click to reveal answer</summary>

**Error:** `TypeError: 'str' object does not support item assignment`

**Why:** Strings are IMMUTABLE (can't be changed)

**Fix:** Create a new string
```python
text = "hello"
text = "H" + text[1:]  # Create new string
print(text)  # "Hello"

# Or use replace
text = "hello"
text = text.replace("h", "H")
print(text)  # "Hello"

# Or use .capitalize()
text = "hello"
text = text.capitalize()
print(text)  # "Hello"
```
</details>

---

## Card 9: String in String

**Q: Check if "cat" is in a sentence**

```python
sentence = "I have a cat"
```

<details>
<summary>Click to reveal answer</summary>

```python
sentence = "I have a cat"

if "cat" in sentence:
    print("Found cat!")
else:
    print("No cat found")
```

**Output:** `Found cat!`

**The `in` keyword:**
```python
"cat" in "I have a cat"    # True
"dog" in "I have a cat"    # False
"CAT" in "I have a cat"    # False (case-sensitive!)
```
</details>

---

## Card 10: Build From Memory

**Q: Write a program that:**
- Asks for user's full name
- Converts to uppercase
- Removes extra spaces
- Prints formatted result

<details>
<summary>Click to reveal answer</summary>

```python
name = input("Enter your full name: ")
name = name.strip()
name = name.upper()
print(f"Name: {name}")
```

**Or combined:**
```python
name = input("Enter your full name: ").strip().upper()
print(f"Name: {name}")
```

**Example:**
```
Enter your full name:   connor o'malley
Name: CONNOR O'MALLEY
```
</details>

---

## Challenge Cards

### Challenge 1: Text Formatter

**Q: Create a program that formats text in multiple ways**

Get a sentence from user and show it:
- All uppercase
- All lowercase
- Title case
- With no extra spaces

<details>
<summary>Click to reveal answer</summary>

```python
text = input("Enter a sentence: ")

print("\n--- FORMATTED TEXT ---")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")
print(f"Cleaned: {text.strip()}")
```

**Example:**
```
Enter a sentence:   hello WORLD

--- FORMATTED TEXT ---
Uppercase: HELLO WORLD
Lowercase: hello world
Title Case: Hello World
Cleaned: hello WORLD
```
</details>

---

### Challenge 2: Word Replacer

**Q: Replace all occurrences of a word in a sentence**

<details>
<summary>Click to reveal answer</summary>

```python
sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("Replace with: ")

new_sentence = sentence.replace(old_word, new_word)

print(f"\nOriginal: {sentence}")
print(f"New: {new_sentence}")
```

**Example:**
```
Enter a sentence: I love cats and cats are great
Word to replace: cats
Replace with: dogs

Original: I love cats and cats are great
New: I love dogs and dogs are great
```
</details>

---

### Challenge 3: String Info

**Q: Display information about a string**

Show:
- Length
- First character
- Last character
- Middle character
- Uppercase version
- Lowercase version

<details>
<summary>Click to reveal answer</summary>

```python
text = input("Enter a word: ")

length = len(text)
first = text[0]
last = text[-1]
middle = text[length // 2]

print(f"\n--- STRING INFO ---")
print(f"Text: {text}")
print(f"Length: {length}")
print(f"First: {first}")
print(f"Last: {last}")
print(f"Middle: {middle}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
```
</details>

---

## Self-Check

**Can you:**
- [ ] Use .upper(), .lower(), .strip(), .replace()?
- [ ] Concatenate strings with +?
- [ ] Use f-strings to format output?
- [ ] Access characters with indexing [0]?
- [ ] Slice strings with [start:end]?
- [ ] Check if substring is in string with `in`?
- [ ] Use len() to get string length?
- [ ] Chain multiple string methods?

**All YES?** You've mastered strings!
