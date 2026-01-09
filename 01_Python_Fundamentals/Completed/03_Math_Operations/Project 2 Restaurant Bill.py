food_cost = 650
tax_rate = .08
tip_percentage = .2
people = 3

tax_amount = food_cost * tax_rate
tip_amount = food_cost * tip_percentage
total = food_cost + tax_amount + tip_amount
per_total = total / people


print("-" * 25)
print(" *** Restaurant Bill *** ")
print("-" * 25)
print(f"Food:             ${round(food_cost)}")
print(f"Tax (8%):         ${round(tax_amount)}")
print(f"Subtotal:         ${round(food_cost + tax_amount)}")
print(f"Tip (20%):        ${round(tip_amount)}")
print(f"-" * 25)
print(f"TOTAL:            ${round(total)}")
print(f"People:            {people}")
print(f"Total Per Person: ${round(per_total, 2)}")
print("-" * 25)