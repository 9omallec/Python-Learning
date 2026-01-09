
shopping_list = ["Ceral", "Milk", "Tomatoes", "Beer", "Cheese", "Bread"]
item = input("What item are you checking for? ")
index = shopping_list.index(item)


print("*** Shopping List ***")

if item not in shopping_list:
    print("That item isn't on your list.")
if item in shopping_list:
    print("That item is on your list!")
    print(f"That item is index #{index}")

print(f"{shopping_list}")

