# Active Recall Cards: While Loops

**Test yourself BEFORE looking at answers**

---

## Card 1: While Loop Syntax

**Q: Write the basic syntax for a while loop.**

<details>
<summary>Click to reveal answer</summary>

```python
while condition:
    # code to repeat
    # must eventually make condition False!
```

**Key points:**
- Colon after condition
- Indentation for body
- Must update condition inside loop
</details>

---

## Card 2: While vs For

**Q: When should you use while instead of for?**

<details>
<summary>Click to reveal answer</summary>

**Use WHILE when:**
- Don't know how many iterations needed
- Loop until condition changes
- Example: "Keep guessing until correct"

**Use FOR when:**
- Know exact number of iterations
- Example: "Repeat exactly 10 times"
</details>

---

## Card 3: Infinite Loop

**Q: What's wrong with this code?**

```python
count = 0
while count < 5:
    print("Hello")
```

<details>
<summary>Click to reveal answer</summary>

**Infinite loop!** count never changes

**Fixed version:**
```python
count = 0
while count < 5:
    print("Hello")
    count += 1  # ← Must update!
```

**Why:** count stays 0, so condition stays True forever
</details>

---

## Card 4: Predict the Output

**Q: What will this print?**

```python
x = 1
while x <= 3:
    print(x)
    x += 1
```

<details>
<summary>Click to reveal answer</summary>

**Output:**
```
1
2
3
```

**Why:** Starts at 1, adds 1 each time, stops when x=4
</details>

---

## Card 5: User Input Loop

**Q: How do you keep asking for input until user types "quit"?**

<details>
<summary>Click to reveal answer</summary>

```python
answer = ""
while answer != "quit":
    answer = input("Type 'quit' to exit: ")
```

**Or cleaner:**
```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
```

**Key:** Check condition each iteration
</details>

---

## Card 6: Break Statement

**Q: What does `break` do in a loop?**

<details>
<summary>Click to reveal answer</summary>

**Answer:** Immediately exits the loop

**Example:**
```python
while True:
    password = input("Enter password: ")
    if password == "secret":
        print("Correct!")
        break  # ← Exits loop here
    print("Wrong, try again")
```

**Use case:** Exit loop based on condition inside
</details>

---

## Card 7: Continue Statement

**Q: What does `continue` do in a loop?**

<details>
<summary>Click to reveal answer</summary>

**Answer:** Skip rest of current iteration, start next iteration

**Example:**
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # ← Skip printing 3
    print(count)
```

**Output:** 1, 2, 4, 5 (skips 3)
</details>

---

## Card 8: Fix the Bug

**Q: Why does this never print "Done"?**

```python
while True:
    print("Running...")
print("Done")
```

<details>
<summary>Click to reveal answer</summary>

**Infinite loop!** No way to exit

**Fixed:**
```python
count = 0
while count < 5:
    print("Running...")
    count += 1
print("Done")
```

**Or with break:**
```python
while True:
    print("Running...")
    break
print("Done")
```
</details>

---

## Card 9: Build From Memory

**Q: Write a countdown from 10 to 1 using while loop.**

<details>
<summary>Click to reveal answer</summary>

```python
count = 10
while count > 0:
    print(count)
    count -= 1
```

**Or:**
```python
count = 10
while count >= 1:
    print(count)
    count -= 1
```

**Both work!**
</details>

---

## Card 10: Validation Loop

**Q: Keep asking for a positive number until user enters one.**

<details>
<summary>Click to reveal answer</summary>

```python
number = -1
while number <= 0:
    number = int(input("Enter positive number: "))

print(f"You entered: {number}")
```

**Or with break:**
```python
while True:
    number = int(input("Enter positive number: "))
    if number > 0:
        break
    print("Must be positive!")
```
</details>

---

## 🎯 Challenge Cards

### Challenge 1: Number Guesser

**Q: Build a game that keeps asking until user guesses 7.**

<details>
<summary>Click to reveal answer</summary>

```python
guess = 0
while guess != 7:
    guess = int(input("Guess the number: "))
    if guess != 7:
        print("Wrong! Try again")

print("Correct!")
```

**Or with break:**
```python
while True:
    guess = int(input("Guess the number: "))
    if guess == 7:
        print("Correct!")
        break
    print("Wrong! Try again")
```
</details>

---

### Challenge 2: Sum Until Zero

**Q: Keep asking for numbers, add them up, stop when user enters 0.**

<details>
<summary>Click to reveal answer</summary>

```python
total = 0
number = 1  # Start with non-zero

while number != 0:
    number = int(input("Enter number (0 to stop): "))
    total += number

print(f"Total: {total}")
```

**Note:** Adds the 0 too (but 0 doesn't change total)
</details>

---

### Challenge 3: Menu System

**Q: Show menu until user chooses "exit".**

<details>
<summary>Click to reveal answer</summary>

```python
while True:
    print("\n=== MENU ===")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
```
</details>

---

## 🔄 Review Schedule

- **Day 1:** All cards
- **Day 2:** Wrong answers
- **Day 7:** From memory
- **Day 16:** Challenge cards
- **Day 35:** Should be automatic

---

## ✅ Self-Check

**Can you:**

- [ ] Write while loop from memory?
- [ ] Explain while vs for loops?
- [ ] Avoid infinite loops?
- [ ] Use break and continue correctly?
- [ ] Build input validation loops?
- [ ] Create menu systems with while?

**All YES?** You've got this!
**Any NO?** Build something using that concept!

---

**Remember:** While loops = "until something happens"
