limit = int(input())
target = int(input())

count = 0
total = 0
found = False

for i in range(1, limit + 1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = True
            break

print(f"Total: {total}")
print(f"Count: {count}")
if found == True:
    print("Target Found")
else:
    print("Target Not Found")