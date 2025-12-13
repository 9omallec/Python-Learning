
attempt = input("What is the password? ")
has_digit = any(char.isdigit() for char in attempt)
has_uppercase = attempt != attempt.lower()

if len(attempt) >= 8 and has_digit and has_uppercase:
    print("Access Granted!")
else:
    if len(attempt) < 8:
        print("Password too short, must be at least 8 characters.")
    elif not has_uppercase:
        print("Password must contian an uppercase letter.")
    elif not has_digit:
        print("Password must contain a number.")