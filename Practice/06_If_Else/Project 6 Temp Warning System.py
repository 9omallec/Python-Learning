

temp = int(input("What is the temperature (°F)? "))

if temp < 32:
    print("Freezing! Wear heavy coat")
if temp >=32 and temp <= 50:
    print("Cold. Wear a jacket")
if temp >= 51 and temp <= 70:
    print("Cool. Light jacket")
if temp >= 71 and temp <= 85:
    print("Perfect Weather!")
if temp > 85:
    print("Hot! Stay hydrated")