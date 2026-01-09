
students = ["Connor", "Blair", "Branson", "Charles", "Kaleb", "Hunter", "Ryan"]
number = int(input("What is the number? "))

print(students)



if number in range(len(students)):
    student_name = students[number]
    student_number = students.index(student_name)
    print(f"Student #: {student_number}\nStudent Name: {student_name}")
else:
    print("Not on the list")


