

number = int(input("Please give me a number: "))

if number % 2 == 0:
    print(f"{number} is even. {number} mod 2 has a remainder of 0")
else:
    print(f"{number} is odd. {number} mod 2 has a remainder of 1")
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")