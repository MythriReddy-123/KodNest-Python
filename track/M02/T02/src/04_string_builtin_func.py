sentence = input()
sentence = sentence.lstrip()
lower = sentence.lower()
s = lower.replace(".", "")
s = s.rstrip()

print("Cleaned:", sentence)
print("Normalized:", s)

print("Words:", s.split())
print("Slug:", s.replace(" ", "-"))

print("Uppercase:", s.upper())
print("Python Position:", lower.find("python"))
