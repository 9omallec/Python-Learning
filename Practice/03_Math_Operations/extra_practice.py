# ===================================
# EXTRA PRACTICE: Math Operations
# ===================================

# Exercise 1: Calculate the area of a circle with radius 5
# Formula: area = 3.14 * radius * radius
area = 3.14
radius = 5
print(area * radius * radius)

# Exercise 2: Convert 100 degrees Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9
fahr = 100
celsius = ((fahr - 32) * 5/9)
print(celsius)

# Exercise 3: You have $100. You buy 3 items at $12.50 each
# Calculate how much money you have left
total = 100
item = 12.50
print(total - (item * 3))

# Exercise 4: Calculate compound interest
# Start with $1000, 5% interest rate, after 1 year
# Formula: final = principal * (1 + rate)
money = 1000
rate = .05
print(money * (1 + rate))

# Exercise 5: Calculate the perimeter of a rectangle
# Length = 10, Width = 5
length = 10
width = 5
perimeter = (length * 2) + (width * 2)
print(perimeter)

# Exercise 6: Split a restaurant bill
# Total bill: $87.50
# Number of people: 4
# Include 20% tip
# How much does each person pay?
total = 87.50
num = 4
tip = .2
per_total = (total / num)
tip_amount = (per_total * tip)
print(per_total + tip_amount)

# Exercise 7: Calculate your age in days
# Assume you're 25 years old (365 days per year)
age = 35
day_in_year = 365
print(age * day_in_year)

# Exercise 8: Calculate the average of five numbers: 78, 92, 85, 88, 95
print((78 + 92 +85 + 88 + 92) / 5)

# Exercise 9: You're saving money. You have $50 and save $20 per week
# How much will you have after 10 weeks?
# Use += in a calculation
money = 50
save = 20
money += (save * 10)
print(money)

# Exercise 10: Calculate the volume of a box
# Length = 5, Width = 3, Height = 2
# Volume = length * width * height
length = 5
width = 3
height = 2
volume = length * width * height
print(volume)

# Exercise 11: You run 3 miles per day. How many miles in a year?
print(3 * 365)

# Exercise 12: Calculate sales tax
# Item costs $49.99, tax rate is 8% (0.08)
# What's the total price with tax?
cost = 49.99
tax = .08
tax_calc = (cost * tax)
total_cost = (cost + tax_calc)
print(total_cost)

# Challenge: Calculate BMI (Body Mass Index)
# BMI = weight_in_kg / (height_in_meters ** 2)
# Use weight = 70kg, height = 1.75m
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(bmi)