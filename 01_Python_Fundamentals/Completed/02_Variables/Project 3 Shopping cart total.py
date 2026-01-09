
tortilla = 2.99
cheese = 4.99
beans = .98
salsa = 3.97
tax = .08

subtotal = tortilla + cheese + beans + salsa
subtotal = round(subtotal, 2)

total = subtotal * tax + subtotal
total = round(total, 2)

print("------------------")
print("===== RECIPT =====")
print("                  ")
print(f"Tortilla: ${tortilla}")
print(f"Cheese: ${cheese}")
print(f"Beans: ${beans}")
print(f"Salsa: ${salsa}")
print("---------------")
print(f"Subtotal: ${subtotal}")
print(f"Tax (8%): ${tax * total}")
print("-----------------")
print(f"TOTAL: ${total}")
print("=================")







