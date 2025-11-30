# Week 3 Challenge: Text Analyzer

**Complete after:** Lessons 7C (Loop Patterns) + Lesson 8 (Lists)
**Estimated time:** 1-1.5 hours
**Difficulty:** ⭐⭐⭐⭐☆

---

## The Challenge

Create a program that analyzes text and provides statistics about it.

## Requirements

Ask the user to enter a sentence or paragraph, then analyze it and display:

### Basic Stats:
- Total number of characters (including spaces)
- Total number of characters (excluding spaces)
- Total number of words
- Total number of sentences (count periods, question marks, exclamation points)
- Average word length

### Letter Analysis:
- Most common letter
- Number of vowels
- Number of consonants
- How many times each vowel appears (a, e, i, o, u)

### Word Analysis:
- Longest word
- Shortest word
- List of all unique words (no duplicates)
- How many times each word appears

### Display Format:
```
TEXT ANALYZER
===========================================
Enter text to analyze: The quick brown fox jumps over the lazy dog.

BASIC STATISTICS
-------------------------------------------
Total characters (with spaces): 44
Total characters (no spaces): 35
Total words: 9
Total sentences: 1
Average word length: 3.89

LETTER ANALYSIS
-------------------------------------------
Total vowels: 12
Total consonants: 23
Vowel breakdown:
  a: 1
  e: 3
  i: 1
  o: 4
  u: 2

WORD ANALYSIS
-------------------------------------------
Longest word: "quick" (5 letters)
Shortest word: "the" (3 letters)
Unique words: 8

Would you like to analyze another text? (yes/no):
```

---

## Bonus Challenges (Optional)

- Find and count palindromes (words that read same forwards/backwards)
- Check if text is mostly uppercase or lowercase
- Count digits and special characters separately
- Calculate readability score (average words per sentence)
- Find all words that start with a specific letter

---

## Skills You'll Practice

- String methods (.lower(), .split(), .count(), etc.)
- Lists (storing words, counting, finding max/min)
- Loops (iterating through strings and lists)
- Dictionaries (counting word frequency) - if you've done Lesson 10
- Math operations (averages, totals)
- If/else statements

---

## Hints

- Use `.split()` to convert text into list of words
- Use `.lower()` to make counting case-insensitive
- Loop through the text character by character to count letters
- Use `len()` for lengths
- `.replace(" ", "")` removes all spaces
- Build a dictionary to count word frequency

---

## Starter Code Structure

```python
# Get input
text = input("Enter text to analyze: ")

# Basic stats
total_chars_with_spaces = len(text)
total_chars_no_spaces = len(text.replace(" ", ""))
words = text.split()
total_words = len(words)

# More analysis here...

# Print results
print("\nBASIC STATISTICS")
print("-" * 40)
print(f"Total characters (with spaces): {total_chars_with_spaces}")
# ... more output
```

---

Create your solution in: `Projects/week3_challenge.py`

This is a bigger challenge - take your time! 🚀
