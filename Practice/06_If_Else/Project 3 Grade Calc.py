score = int(input("What is your test score (0-100)? "))


if score in range (90, 101):
    print("You got an A!")
    if score == 100:
        print("Perfect Score!")
if score in range (80, 90):
    print("You got a B!")
if score in range (70, 80):
    print("You got a C!")
if score in range (61, 70):
    print("You got a D!")
if score <= 60:
    print("You got an F!")


