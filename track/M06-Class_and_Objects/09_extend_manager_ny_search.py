class StudentProfile:
    def __init__(self, student_id, student_name, course_name):
        self.student_id = student_id
        self.student_name = student_name
        self.course_name = course_name

    def __str__(self):
        return f"{self.student_id} - {self.student_name} - {self.course_name}"


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student_profile(self, student):
        self.students.append(student)

    def filter_students_by_course(self, course_name):
        res = []
        for profile in self.students:
            if profile.course_name.lower() == course_name.lower():
                res.append(profile)
        return res


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

required_course = input().strip()

matching_students = manager.filter_students_by_course(required_course)

if matching_students:
    for student in matching_students:
        print(student)
else:
    print(f"No students found for course: {required_course}")