
number = [1, 3, 6, 23, 19, 42, 42.1, 100, 101, 3333, 666]
total = sum(number)
avg = total / len(number)
hi = max(number)
low = min(number)
sort_number = sorted(number, reverse = True)
above_avg = []

print(f"Total Sum:     {total}")
print(f"Average Score: {avg}")
print(f"Highest Score: {hi}")
print(f"Lowest Score:  {low}")
print(f"The scores from highest to lowest:\n{sort_number}")

even_count = 0
odd_count = 0
avg_count = 0
for num in number:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if num > avg:
        above_avg.append(num)


print(f"The scores above average: {above_avg}")
print(f"There are {even_count} even scores.")
print(f"There are {odd_count} odd scores.")
