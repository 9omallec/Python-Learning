# Week 4 Challenge: Student Grade Manager

**Complete after:** Lessons 9 (Functions) + Lesson 10 (Dictionaries)
**Estimated time:** 1.5-2 hours
**Difficulty:** ⭐⭐⭐⭐⭐

---

## The Challenge

Create a complete grade management system using functions and dictionaries.

## Requirements

Create a program that manages students and their grades with these features:

### Menu Options:
```
STUDENT GRADE MANAGER
===========================================
1. Add student
2. Add grade for student
3. View student grades
4. View class average
5. View top student
6. View all students
7. Remove student
8. Export report
9. Quit

Choose an option:
```

### Features to Implement:

**1. Add Student**
- Ask for student name
- Create entry in system
- Confirm addition

**2. Add Grade**
- Ask for student name
- Ask for subject
- Ask for grade (0-100)
- Add to that student's record

**3. View Student Grades**
- Ask for student name
- Display all their grades
- Show their average
- Show letter grade

**4. View Class Average**
- Calculate average of all students
- Show highest class average
- Show lowest class average

**5. View Top Student**
- Find student with highest average
- Display their name and average

**6. View All Students**
- List all students and their averages

**7. Remove Student**
- Ask for name
- Confirm deletion
- Remove from system

**8. Export Report**
- Print formatted report of all students
- Include: name, all grades, average, letter grade
- Save to text (print is fine for now)

---

## Data Structure

Use a dictionary like this:
```python
students = {
    "Connor": {
        "grades": [85, 90, 92, 88],
        "subjects": ["Math", "English", "Science", "History"]
    },
    "Alice": {
        "grades": [95, 93, 97, 96],
        "subjects": ["Math", "English", "Science", "History"]
    }
}
```

---

## Required Functions

Create at least these functions:

```python
def add_student(students, name):
    """Add a new student to the system"""
    pass

def add_grade(students, name, subject, grade):
    """Add a grade for a student"""
    pass

def calculate_average(grades):
    """Calculate average from list of grades"""
    pass

def get_letter_grade(average):
    """Convert number grade to letter (A, B, C, D, F)"""
    pass

def find_top_student(students):
    """Find student with highest average"""
    pass

def display_student(students, name):
    """Display all info for one student"""
    pass

def display_all_students(students):
    """Display summary of all students"""
    pass

def class_average(students):
    """Calculate average across all students"""
    pass
```

---

## Example Output

```
STUDENT GRADE MANAGER
===========================================
1. Add student
2. Add grade for student
3. View student grades
...

Choose an option: 1
Enter student name: Connor
Student 'Connor' added successfully!

Choose an option: 2
Enter student name: Connor
Enter subject: Math
Enter grade (0-100): 85
Grade added successfully!

Choose an option: 3
Enter student name: Connor

STUDENT REPORT: Connor
-------------------------------------------
Grades:
  Math: 85
  English: 90
  Science: 92
  History: 88

Average: 88.75
Letter Grade: B
-------------------------------------------

Choose an option: 8

CLASS REPORT
===========================================
Connor
  Average: 88.75 (B)
  Grades: Math(85), English(90), Science(92), History(88)

Alice
  Average: 95.25 (A)
  Grades: Math(95), English(93), Science(97), History(96)

Class Average: 92.0
Top Student: Alice (95.25)
===========================================
```

---

## Bonus Challenges (Optional)

- Add GPA calculation (A=4.0, B=3.0, etc.)
- Add grade weighting (exams worth more than homework)
- Track attendance
- Add student ID numbers
- Save data to a file (you'll need to research this!)
- Load data from a file
- Add password protection for the system
- Search students by grade range
- Drop lowest grade option

---

## Skills You'll Practice

- Functions (parameters, return values)
- Dictionaries (nested dictionaries)
- Lists (storing multiple grades)
- Loops (menu system, iterating through students)
- If/else (menu choices, validation)
- Math (averages, finding max/min)
- String formatting

---

## Tips

- Build one feature at a time and test it
- Start with just add/view students, then add complexity
- Use functions to keep code organized
- Test with sample data first
- Handle errors (what if student doesn't exist?)

---

Create your solution in: `Projects/week4_challenge.py`

This is the biggest challenge yet - you got this! 🚀
