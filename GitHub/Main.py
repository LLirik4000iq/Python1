from student import Student
budnychenko = Student("Denys", 15.7, "S2816")
solop = Student("Illya", 16.1, "S2816")
oliynyk = Student("Kostya", 14.2, "S2816")
students = []
students.append(budnychenko)
students.append(solop)
students.append(oliynyk)
for student in students:
    print(f"Name:\t{student.Name}\n"
          f"Age:\t{student.Age}\n"
          f"Group:\t{student.Group}")
    from student import Student

    budnychenko = Student("Denys", 15.7, "S2816")
    solop = Student("Illya", 16.1, "S2816")
    oliynyk = Student("Kostya", 14.2, "S2816")
    students = []
    students.append(budnychenko)
    students.append(solop)
    students.append(oliynyk)
    for student in students:
        student.String()