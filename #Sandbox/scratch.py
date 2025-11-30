# ===================================
# SCRATCH PAD
# ===================================
# Use this file to test individual exercises!
# Copy an exercise here, test it, then paste back into the practice file.



count = 0
answer = 7

while True:
    count += 1
    guess = int(input("Pick a number from 1-10: "))
    if guess != 7:
        print("Try again! ")
    elif guess == 7:
        print(f"Correct! it took you {count} number of tries" )
        break
