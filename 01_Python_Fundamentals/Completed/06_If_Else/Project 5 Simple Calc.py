x = int(input("Please give me the first number: "))
y = int(input("Please give me a second number: "))
op = input("What operation would you like to use? ")

print(f"First number: {x}")
print(f"Second number: {y}")

if y == 0 and (op == "/" or op == "%"):
        print("Cannot divide by zero.")
elif op == "+":
        print(f"{x} + {y} = {x + y}")
elif op == "-":
        print(f"{x} - {y} = {x - y}")
elif op == "*":
        print(f"{x} * {y} = {x * y}")
elif op == "/":
        print(f"{x} / {y} = {round(x / y)}")
elif op == "%":
        print(f"{x} mod {y} = {round(x % y, 2)}")
elif op == "**":
        print(f"{x} to the power of {y} = {round(x ** y, 2)}")
else:
    print("Try again")