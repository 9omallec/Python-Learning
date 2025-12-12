num = int(input("What is the number?"))


for num in range(1, num + 1):
    fizz = (num % 3) == 0
    buzz = (num % 5) == 0
    if fizz and buzz:
        print("FizzBuzz")
    elif fizz and not buzz:
        print("Fizz")
    elif buzz and not fizz:
        print("Buzz")
    else:
        print(num)
