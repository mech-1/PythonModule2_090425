# "Наивысшая оценка"
#
# Дан список кортежей, где каждый кортеж представляет собой пару (имя, оценка).
# Необходимо найти имя с наивысшей оценкой.
# Если наивысших оценок несколько, вывести имена

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 92)]
# max_student = max(students, key=lambda student: student[1])
max_student = students[0]
for student in students:
    if student[1] > max_student[1]:
        max_student = student
        
for student in students:
    if student[1] == max_student[1]:
        print(student[0])
# Ожидаемый результат: 'Bob' и 'David