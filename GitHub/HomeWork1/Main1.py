from student1 import *


dvornikov = Student("Kirill", 16.8, "S2816", 0)

students = []

students.append(dvornikov)

for student in students:
    student.ShowInfo()


dvornikov.Work()
for student in students:
    student.ShowInfo()
