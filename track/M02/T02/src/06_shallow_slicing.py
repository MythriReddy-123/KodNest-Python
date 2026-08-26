skills = []


for _ in range(5):
    skill = input()
    skills.append(skill)


skill_record = tuple(skills)


print("Skill Record:", skill_record)
print("First Three:", skill_record[:3])
print("Last Two:", skill_record[-2:])
print("Alternate Skills:", skill_record[::2])
print("Reversed Skills:", skill_record[::-1])