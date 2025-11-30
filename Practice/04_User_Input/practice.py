# ===================================
# PRACTICE: User Input
# ===================================

# Practice 1: Ask for the user's name and greet them
user_name = input("What's your name? ")
print("Hello ", user_name)

# Practice 2: Ask for the user's favorite color and print it back
fav_color = input("What's your favorite color? ")
print(fav_color)

# Practice 3: Ask for a number and print that number
x = int(input("Give me a number. "))
print(x)

# Practice 4: Ask for a number, convert to int, add 10 to it, print result
y = int(input("Give me a number. "))
print(y + 10)

# Practice 5: Ask for two numbers, convert both to int, multiply them
a = int(input("Give me a number. "))
b = int(input("Give me another number. "))
print(a * b)

# Practice 6: Ask for price and quantity, calculate total cost
price = float(input("Give me a price. "))
quantity = int(input("Give me a quantity. "))
total_cost = float(price * quantity)
print(total_cost)

# Practice 7: Ask for temperature in Celsius, convert to Fahrenheit
# Formula: F = C * 9/5 + 32
tempc = int(input("Give me a temperature in celsius. "))
print("That is ", tempc * 9 / 5 + 32, "degrees in fahrenheit")

# Challenge: Create a simple calculator
# Ask for two numbers and add them together
z = int(input("Give me a number. "))
c = int(input(" Give me another number. "))
print(z + c)