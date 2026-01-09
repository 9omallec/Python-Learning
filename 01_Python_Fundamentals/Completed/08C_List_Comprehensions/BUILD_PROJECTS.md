# Build Projects: List Comprehensions (OPTIONAL)

**Learn to create lists in one line**

This is an advanced/optional lesson. All these projects can be done with regular loops too!

---

## Project 1: Data Transformer (12 min)

**Goal:** Transform data using list comprehensions

**Requirements:**
- Start with a list of temperatures in Celsius: [0, 10, 20, 30, 40]
- Convert to Fahrenheit using comprehension
- Start with prices in dollars: [10.50, 25.00, 8.75, 15.25]
- Add 20% tax using comprehension
- Start with words: ["hello", "world", "python"]
- Create uppercase version using comprehension
- Create lengths list using comprehension

**Example Output:**
```
Celsius: [0, 10, 20, 30, 40]
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]

Prices: [10.5, 25.0, 8.75, 15.25]
With Tax: [12.6, 30.0, 10.5, 18.3]

Words: ['hello', 'world', 'python']
Uppercase: ['HELLO', 'WORLD', 'PYTHON']
Lengths: [5, 5, 6]
```

**Compare:** Show both loop version and comprehension version

---

## Project 2: List Filter (12 min)

**Goal:** Filter lists using comprehensions with conditions

**Requirements:**
- List of ages: [12, 17, 25, 8, 30, 16, 45, 11]
- Get only adults (18+) using comprehension
- List of numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Get only evens using comprehension
- Get only odds using comprehension
- Get only numbers > 5 using comprehension
- List of words: ["cat", "elephant", "dog", "butterfly", "ant", "tiger"]
- Get only words longer than 4 letters

**Example Output:**
```
Ages: [12, 17, 25, 8, 30, 16, 45, 11]
Adults (18+): [25, 30, 45]

Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Evens: [2, 4, 6, 8, 10]
Odds: [1, 3, 5, 7, 9]
Greater than 5: [6, 7, 8, 9, 10]

Words: ['cat', 'elephant', 'dog', 'butterfly', 'ant', 'tiger']
Long words: ['elephant', 'butterfly', 'tiger']
```

---

## Project 3: String Processor (15 min)

**Goal:** Process strings using comprehensions

**Requirements:**
- List of emails: ["ALICE@EMAIL.COM", "bob@EMAIL.COM", "CHARLIE@email.com"]
- Convert all to lowercase using comprehension
- List of names: ["  alice  ", " bob", "charlie  "]
- Strip whitespace using comprehension
- List of filenames: ["doc.txt", "image.png", "data.csv", "script.py"]
- Extract just the extensions using comprehension
- List of sentences: ["Hello world", "Python is fun", "I love coding"]
- Get word count of each using comprehension

**Example Output:**
```
Original emails: ['ALICE@EMAIL.COM', 'bob@EMAIL.COM', 'CHARLIE@email.com']
Cleaned: ['alice@email.com', 'bob@email.com', 'charlie@email.com']

Names with spaces: ['  alice  ', ' bob', 'charlie  ']
Trimmed: ['alice', 'bob', 'charlie']

Files: ['doc.txt', 'image.png', 'data.csv', 'script.py']
Extensions: ['txt', 'png', 'csv', 'py']

Sentences: ['Hello world', 'Python is fun', 'I love coding']
Word counts: [2, 3, 3]
```

---

## 🔄 Bonus Projects

### Bonus 1: Grade Converter
List of scores, convert to letter grades using comprehension with if-else

### Bonus 2: Matrix Operations
2D list, flatten to 1D using nested comprehension

### Bonus 3: Password Validator
List of passwords, filter only valid ones (len >= 8)

---

## 📊 Track Your Progress

```
Project 1: Data Transformer (12 min) ☐
Project 2: List Filter (12 min) ☐
Project 3: String Processor (15 min) ☐

Total: 3 projects, ~39 min
```

---

## ✅ Ready to Move On When:

- [ ] You can write basic list comprehensions
- [ ] You can add simple conditions (if)
- [ ] You know when to use loops vs. comprehensions
- [ ] Built 2-3 projects

---

**Remember:** When in doubt, use a regular loop! Comprehensions should make code CLEARER, not more confusing.
