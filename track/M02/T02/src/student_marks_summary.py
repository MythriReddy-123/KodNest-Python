n = int(input())

pass_count = 0
fail_count = 0
total = 0

for i in range(1, n+1):
    marks = int(input())
    total += marks
    if marks >= 50:
        pass_count += 1
    else:
        fail_count += 1

print(f"Pass Count: {pass_count}")
print(f"Fail Count: {fail_count}")
print(f"Total: {total}")

if n == pass_count:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")
