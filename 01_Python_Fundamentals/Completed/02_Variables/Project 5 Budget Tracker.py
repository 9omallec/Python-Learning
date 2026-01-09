income = 4000
rent = 1000
car = 300
internet = 50
food = 250
gas = 30


total_expenses = rent + car + internet + food + gas
remaining = income - total_expenses

a = income - remaining


print("====== MONTHLY BUDGET ======")
print("Income: ", income)
print("                            ")
print("EXPENSES:                   ")
print("Rent:           $", rent)
print("Car:            $", car)
print("Internet:       $", internet)
print("Food:           $", food)
print("Gas:            $", gas)
print("----------------------------")
print("Total Expenses: $", total_expenses)
print("Remaining:      $", remaining)
print("                             ")
if remaining <= income:
    print("Status: Under Budget!  👍")
else:
    print("Status: Over Budget!   👎")
print("============================")


