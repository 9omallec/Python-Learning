celsius = 0
fahrenheit = 0

c = round((fahrenheit - 32) * 5 / 9)
f = round((celsius* 9 / 5) + 32)

print("\n*** Temperature Converter ***\n")
print(f"        {celsius}°C = {f}°F")
celsius = 50
f = round((celsius* 9 / 5) + 32)
print(f"        {celsius}°C = {f}°F")
celsius = 100
f = round((celsius* 9 / 5) + 32)
print(f"        {celsius}°C = {f}°F\n")
print(f"        {fahrenheit}°F = {c}°C")
fahrenheit = 50
c = round((fahrenheit - 32) * 5 / 9)
print(f"        {fahrenheit}°F = {c}°C")
fahrenheit = 100
c = round((fahrenheit - 32) * 5 / 9)
print(f"        {fahrenheit}°F = {c}°C")
print("*" * 28)







