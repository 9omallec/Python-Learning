


cost = int(input("How much does it cost? "))
tax = int(input("what percentage is tax? "))
tip = int(input("What percentage for a tip? "))

total_tax = tax / 100 * cost
total_tip = tip / 100 * cost
total_cost = total_tax + total_tip + cost

print(f"{total_tax} is the tax")
print(f"{total_tip} is the tip")
print(f"{total_cost} is your final total")
