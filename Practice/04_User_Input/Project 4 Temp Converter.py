convert = input("Are we converting C to F (enter 1) or F to C (enter 2)? ")
temp = int(input("What is the temperature? "))
f = (temp * 9 / 5) + 32
c = (temp - 32) * 5 / 9

if convert == 1:
    print(f"{round(temp)}°C = {round(f, 2)}°F")
else:
    print(f"{round(temp)}°F = {round(c, 2)}°C")
