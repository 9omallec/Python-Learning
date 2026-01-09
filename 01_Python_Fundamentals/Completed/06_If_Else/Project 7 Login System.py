
user_name = "connor"
password = "cro123!"
attempts = 3


while attempts > 0:
    user_input = input("Username: ")
    user_pass = input("Password: ")
    if user_input == user_name and user_pass == password:
        print(f"Login Successful!\n Welcome, {user_name}.")
        break
    if user_input != user_name and user_pass != password:
        print("Username: Incorrect\nPassword: Incorrect\nTry again")
    if user_input == user_name and user_pass != password:
        print(f"Username: {user_name}\nPassword: Incorrect\nTry again")
    if user_input != user_name and user_pass == password:
        print("Username: Incorrect\nTry again")
    else:
        attempts -= 1
        print(f"You have {attempts} attempts left.")
if attempts == 0:
    print("You have been locked out due to too many failed attempts.")

