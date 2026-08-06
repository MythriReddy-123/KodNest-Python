n = int(input())

positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for i in range(1, n+1):
    num = int(input())
    total += num
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")