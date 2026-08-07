n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(score)

print("Highest Score:", max(scores))
print("Lowest Scores:", min(score))
print("Total Score:", sum(score))

search_score = int(input())
if search_score in scores:
    print(f"{search_score} is present")
else:
    print(f"{search_score} is not present")