# Week 2 Challenge: Number Pattern Generator

**Complete after:** Lessons 7A-7B (Basic loops)
**Estimated time:** 45-60 minutes
**Difficulty:** ⭐⭐⭐☆☆

---

## The Challenge

Create a program that generates various number patterns based on user input.

## Requirements

Create a menu system that keeps running until the user chooses to quit:

```
NUMBER PATTERN GENERATOR
========================
1. Count to N
2. Count down from N
3. Even numbers up to N
4. Odd numbers up to N
5. Multiplication table
6. Number pyramid
7. Quit

Choose an option:
```

### For each option:

**Option 1: Count to N**
- Ask for a number
- Print: 1, 2, 3, ... up to that number

**Option 2: Count down from N**
- Ask for a number
- Print: N, N-1, N-2, ... down to 1

**Option 3: Even numbers up to N**
- Ask for a number
- Print all even numbers from 0 to N

**Option 4: Odd numbers up to N**
- Ask for a number
- Print all odd numbers from 1 to N

**Option 5: Multiplication table**
- Ask which number (1-12)
- Print that number's times table (1x through 10x)

**Option 6: Number pyramid**
- Ask for number of rows
- Print pattern like:
  ```
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
  ```

**Option 7: Quit**
- Print goodbye message and exit

---

## Bonus Challenges (Optional)

- Add input validation (reject negative numbers)
- Add a "sum of numbers 1 to N" option
- Add a "factorial of N" option
- Add a reverse pyramid pattern
- Keep track of how many patterns they've generated

---

## Skills You'll Practice

- While loops (menu system)
- For loops (patterns)
- If/elif/else (menu choices)
- Range with different parameters
- String formatting

---

## Example Run

```
NUMBER PATTERN GENERATOR
========================
1. Count to N
2. Count down from N
3. Even numbers up to N
4. Odd numbers up to N
5. Multiplication table
6. Number pyramid
7. Quit

Choose an option: 3
Enter a number: 10

Even numbers up to 10:
0
2
4
6
8
10

Choose an option: 7
Thanks for using the pattern generator! Goodbye!
```

---

## Hints

- Use a while loop for the menu (while choice != "7")
- Use for loops inside each option
- For the pyramid, you'll need a nested loop (a loop inside a loop)
- Use `print(i, end=" ")` to print numbers on the same line

---

Create your solution in: `Projects/week2_challenge.py`

Good luck! 🚀
