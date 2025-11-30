# Week 1 Challenge: Personal Information Quiz

**Complete after:** Lessons 1-6
**Estimated time:** 30-45 minutes
**Difficulty:** ⭐⭐☆☆☆

---

## The Challenge

Create a program that asks the user 10 personal questions, then creates a "profile" summary at the end.

## Requirements

1. **Ask for these 10 things:**
   - First name
   - Last name
   - Age
   - City
   - Favorite color
   - Favorite food
   - Favorite number
   - Birth year
   - Height (in feet, as a decimal like 5.9)
   - Whether they like Python (yes/no)

2. **Calculations to perform:**
   - Calculate birth year from age (use 2024 as current year)
   - Calculate how many years until they're 100
   - Double their favorite number

3. **Use if/else to add personality:**
   - If age < 18: "You're pretty young!"
   - If age 18-30: "You're in your prime!"
   - If age > 30: "You have great experience!"

   - If favorite color is "blue": "Blue is the most popular color!"
   - Otherwise: "That's a unique choice!"

4. **Print a formatted summary at the end** like this:
   ```
   ==========================================
   PROFILE SUMMARY
   ==========================================
   Name: Connor O'Malley
   Age: 35 years old
   Location: Omaha
   Born: 1989
   Years until 100: 65

   Favorites:
   - Color: Purple
   - Food: Pizza
   - Number: 3 (double: 6)

   Physical Stats:
   - Height: 5.9 feet

   Likes Python: Yes

   Fun fact: You have great experience!
   ==========================================
   ```

---

## Bonus Challenges (Optional)

- Add validation: If age is negative or over 150, ask them to enter again
- Convert height from feet to centimeters (1 foot = 30.48 cm)
- Create a "username" from their first initial + last name (all lowercase)
- Ask for their birth month and tell them their zodiac sign (just a few)

---

## Skills You'll Practice

- Variables (all types: strings, integers, floats, booleans)
- User input with type conversion
- Math operations
- If/else statements
- String formatting with f-strings
- Print formatting

---

## Hints

- Use f-strings for the summary to make it clean
- Store all the inputs in variables first, then do calculations
- Test one section at a time - don't write everything before running it!
- Pay attention to int() vs float() conversion

---

## Solution

Don't look until you've tried it yourself! Create your solution in:
`Projects/week1_challenge.py`

Good luck! 🚀
