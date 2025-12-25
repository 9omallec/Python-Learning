
game1 = [49, 50, 100, 132, 42, 56, 100, 666, 1000]
maxi = max(game1)
mini = min(game1)
average = sum(game1) / len(game1)
high = []


print(f"Highest Score: {maxi}")
print(f"Lowest Score: {mini}")
print(f"Average Scores: {round(average)}")
for score in game1:
    if score > 80:
        high.append(score)
print(f"Scores Above 80: {high}")