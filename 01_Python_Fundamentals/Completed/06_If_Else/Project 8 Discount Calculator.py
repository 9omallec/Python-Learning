

amount = int(input("what is the purchase price? "))

if amount >= 0 and amount <= 50:
    discount = 0
if amount >=51 and amount <= 100:
    discount = .1
if amount >= 101 and amount <= 200:
    discount = .15
if amount >= 201:
    discount = .2

print(f"Purchase amount: ${amount}")
print()
print(f"Discount ({discount * 100}%): ${discount * amount}")
print (f"Final price: ${amount - discount * amount}")