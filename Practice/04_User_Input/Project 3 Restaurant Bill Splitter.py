bill = int(input("How much is the bill? "))
tip_percent = int(input("What percentage would you like to tip? "))
people = int(input("How many people do you have? "))

tip = tip_percent / 100 * bill
total = tip + bill
per_person = total / people

print("\n* * * Bill Splitter * * *")
print(f"Your Bill: ${bill}")
print(f"Your Tip: {tip_percent}%")
print(f"Your Total: ${total}")
print(f"Split between {people}")
print(f"Youre final total per person is: {per_person}")
print("--------------------------\n")
