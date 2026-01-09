# ===================================
# PRACTICE: Dictionaries
# ===================================

# Practice 1: Create a dictionary with your personal info (name, age, city)
personal_info = {
    'Name': 'Connor',
    'Age': '35',
    'City': 'Omaha'
}

# Practice 2: Print just your name from the dictionary
print(personal_info['Name'])

# Practice 3: Add a new key "favorite_color" to your dictionary
personal_info['favorite color'] = 'Purple'

# Practice 4: Update your age in the dictionary
personal_info['Age'] = 36

# Practice 5: Create a dictionary of 3 fruits and their prices
fruits = {
    'Apple': 1.00,
    'Pineapple': 5.00,
    'Avocado': 3.50
}

# Practice 6: Print all the keys in your fruits dictionary
print(fruits.keys())

# Practice 7: Print all the values in your fruits dictionary
print(fruits.values())

# Practice 8: Loop through your fruits dictionary and print each fruit and price
for key, value in fruits.items():
    print(f"Fruit: {key} - ${value}")

# Practice 9: Check if "apple" exists in your fruits dictionary
for 'Apple' in fruits:
    print("Apples are included")

# Practice 10: Create a phonebook dictionary with 3 contacts
# Then ask user for a name and print their phone number
phonebook = {
    'connor': '111-1111',
    'mom': '222-2222',
    'dad': '333-3333'
}

name = input("Who are you looking for? ")
if name in phonebook:
    print(phonebook[name])

# Challenge 1: Create a simple inventory system
# Dictionary with items and quantities
# Allow user to:
# - View all items
# - Add an item
# - Remove an item
# - Update quantity

dic = {
    'mouse': 1,
    'keyboard': 3,
    'monitor': 4,
    'microphone': 1
}

def inventory():
    while True:
        choice = input("""What would you like to do?
                       1. View all items?
                       2. Add and item?
                       3. remove an item?
                       4. Update quantity?
                       5. Exit.
                       Please choose a number 1-5: """)
        if choice == '1':
            for item, quantity in dic.items():
                print(f"{item}:  #{quantity}")
        if choice == '2':
            item = input("What item would you like to add? ")
            amount = input("And how many are you adding? ")
            dic[item] = int(amount)
        if choice == '3':
            remove = input("What item do you want to remove? ")
            del dic[remove]
        if choice == '4':
            update = input("What item would you like to update? ")
            number = input("What is the new inventory? ")
            dic[update] = int(number)
        if choice == '5':
            break
        if not choice.isdigit() or choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice!\nPlease make a choice from 1-5: ")

inventory()


# Challenge 2: Create a grade book
# Dictionary where keys are student names, values are lists of grades
# Calculate and print the average grade for each student
grade_book = {
    'bob': [90, 90, 60],
    'dave': [80, 75, 76],
    'ronald': [65, 65, 65],
    'cody': [100, 99, 98],
    'connor': [99, 75, 80]
}

for name, grade in grade_book.items():
    print(f"{name}:  avg grade  - {sum(grade) / len(grade):.2f}")

