class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        data = {self.name, self.grade}
        return f"{self.name, self.grade}"


student = Student("BHUPENDRA", "A")
print("student name And Grade is:-", student)
