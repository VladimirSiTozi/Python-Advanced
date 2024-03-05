n = int(input())
students_data = ({})

for _ in range(n):
    student_name, grade = input().split()
    if student_name not in students_data:
        students_data[student_name] = []

    students_data[student_name].append(float(grade))

for student, his_grade in students_data.items():
    convert_grades = ' '.join(map(lambda grade: f'{grade:.2f}', his_grade))
    average_grade = (sum(his_grade) / len(his_grade))
    print(f'{student} -> {convert_grades} (avg: {average_grade:.2f})')

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00

# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66

# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30
