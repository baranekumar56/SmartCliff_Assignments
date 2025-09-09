
class School:
    __total_students = 0
    __MAX_CAPACITY = 0

    def __init__(self):
        School.__MAX_CAPACITY = 500

    """enrolling a student in school increases the student count"""
    def enroll_student(self):
        if School.__MAX_CAPACITY == School.__total_students:
            return "Cannot enroll new students. School reached max cap"
        else:
            School.__total_students += 1
            return "Enrollment done successfully"

    """return the total no of students in the school"""
    def get_total_students(self):
        return School.__total_students


s1 = School()
s2 = School()

print(s1.enroll_student())
print(s2.enroll_student())

print(s1.get_total_students())
print(s2.get_total_students())