# Build Projects: If/Else Statements

**Make decisions in your code**

---

## Project 1: Password Validator (20 min)

**Goal:** Check if password meets requirements

**Requirements:**
- Ask user for password
- Check if length >= 8 characters
- If valid: "Access granted!"
- If invalid: "Password too short"

**Bonus challenges:**
- Check if contains a number
- Check if contains uppercase letter
- Give specific error messages

**Example Output:**
```
Enter password: abc123
✗ Password too short (must be 8+ characters)

Enter password: secret1234
✓ Access granted!
```

---

## Project 2: Age Verifier (15 min)

**Goal:** Check if old enough for different activities

**Requirements:**
- Ask for age
- Check different age limits:
  - Under 13: "You're a kid"
  - 13-17: "You're a teen"
  - 18+: "You're an adult"
- Use if/elif/else

**Example:**
```
Enter your age: 16
You're a teen!
You can: Use social media, play teen-rated games
You cannot: Vote, drive (in most places)
```

---

## Project 3: Grade Calculator (20 min)

**Goal:** Convert numeric score to letter grade

**Requirements:**
- Ask for score (0-100)
- Calculate letter grade:
  - 90-100: A
  - 80-89: B
  - 70-79: C
  - 60-69: D
  - Below 60: F
- Print grade with message

**Example:**
```
Enter your score: 87
Your grade: B
Good job!
```

**Bonus:** Add + and - grades (B+, B, B-)

---

## Project 4: Even or Odd Checker (15 min)

**Goal:** Determine if number is even or odd

**Requirements:**
- Ask for a number
- Use modulo operator (%)
- Print "Even" or "Odd"
- Explain why

**Example:**
```
Enter a number: 17
17 is ODD
(17 ÷ 2 has a remainder of 1)
```

**Bonus:** Also check if positive/negative/zero

---

## Project 5: Simple Calculator with Validation (25 min)

**Goal:** Calculate but handle errors

**Requirements:**
- Ask for two numbers
- Ask for operation (+, -, *, /)
- Check if operation is valid
- If division, check for divide by zero
- Perform calculation and show result

**Example:**
```
First number: 10
Second number: 0
Operation (+, -, *, /): /

Error: Cannot divide by zero!
```

---

## Project 6: Temperature Warning System (20 min)

**Goal:** Give warnings based on temperature

**Requirements:**
- Ask for temperature in Fahrenheit
- Give appropriate warning:
  - Below 32°: "Freezing! Wear heavy coat"
  - 32-50°: "Cold. Wear jacket"
  - 51-70°: "Cool. Light jacket"
  - 71-85°: "Perfect weather!"
  - Above 85°: "Hot! Stay hydrated"

**Example:**
```
Temperature: 28
⚠️ Freezing! Wear heavy coat
Watch for ice!
```

---

## Project 7: Login System (25 min)

**Goal:** Simple username/password checker

**Requirements:**
- Set username and password in code
- Ask user to login
- Check both username AND password
- Give specific error messages
- Allow 3 attempts

**Example:**
```
Username: connor
Password: python123

✓ Login successful!
Welcome, Connor!

--- OR ---

Username: connor
Password: wrong
✗ Incorrect password. Try again.
```

---

## Project 8: Discount Calculator (20 min)

**Goal:** Calculate price with conditional discounts

**Requirements:**
- Ask for purchase amount
- Apply discounts:
  - $0-50: No discount
  - $51-100: 10% off
  - $101-200: 15% off
  - $201+: 20% off
- Show original, discount, and final price

**Example:**
```
Purchase amount: $125

Original: $125.00
Discount (15%): $18.75
Final Price: $106.25
```

---

## Project 9: BMI Calculator with Categories (25 min)

**Goal:** Calculate BMI and categorize

**Requirements:**
- Ask for weight (pounds) and height (inches)
- Calculate BMI: (weight / height²) × 703
- Categorize:
  - Below 18.5: Underweight
  - 18.5-24.9: Normal
  - 25-29.9: Overweight
  - 30+: Obese
- Show BMI and category

---

## Project 10: Quiz Game (30 min)

**Goal:** Multi-question quiz with scoring

**Requirements:**
- Ask 5 questions
- Track correct answers
- Give immediate feedback
- Calculate percentage
- Give final grade message

**Example:**
```
Question 1: What is 2 + 2?
> 4
✓ Correct!

Question 2: What is the capital of France?
> London
✗ Wrong! It's Paris.

... 3 more questions ...

Final Score: 3/5 (60%)
Grade: D - Keep studying!
```

---

## 🔄 Bonus Projects

### Bonus 1: Leap Year Checker
Check if year is a leap year (divisible by 4, except century years)

### Bonus 2: Triangle Validator
Check if 3 sides can make a valid triangle

### Bonus 3: Shipping Calculator
Calculate shipping cost based on weight and distance

### Bonus 4: Ticket Pricing
Different prices for kids, adults, seniors

### Bonus 5: Password Strength Meter
Weak, Medium, Strong, Very Strong

---

## 📊 Track Your Progress

```
Project 1: Password Validator (18 min) ✓
Project 2: Age Verifier (15 min) ✓
Project 3: Grade Calculator (22 min) ✓
Project 4: Even/Odd Checker (12 min) ✓
Project 5: Calculator with Validation (25 min) ✓

Total: 5 projects, 92 min
```

---

## ✅ Ready to Move On When:

- [ ] Built at least 5 if/else projects
- [ ] Comfortable with if/elif/else
- [ ] Can use comparison operators (==, !=, >, <, >=, <=)
- [ ] Can combine conditions with and/or
- [ ] Can handle user validation

---

**Remember:** Getting the logic right matters more than perfect code!
