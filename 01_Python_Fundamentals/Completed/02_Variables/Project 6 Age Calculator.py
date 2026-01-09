birth_year = 1990
current_year = 2025

age_year = current_year - birth_year
age_month = age_year * 12
age_day = age_year * 365
age_hour = age_year * 8760
age_in_10 = age_year + 10
age_in_20 = age_year + 20


print(f"You are:\n{age_hour} hours")
print(f"{age_day} days")
print(f"{age_month} months")
print(f"{age_year} years old!")
print("\nIn 10 years you will be:")
print(f"{age_hour + (10 * 8760)} hours")
print(f"{age_day + (10 * 365)} days")
print(f"{age_month + (10 * 12)} months")
print(f"{age_year + 10} years old!")
print("\nIn 20 years you will be: ")
print(f"{age_hour + (20 * 8760)} hours")
print(f"{age_day + (20 * 365)} days")
print(f"{age_month + (20 * 12)} months")
print(f"{age_year + 20} years old!")

