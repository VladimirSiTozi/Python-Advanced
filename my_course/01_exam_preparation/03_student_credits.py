def students_credits(*args):
    diyan_courses = {}
    sum_of_courses = 0
    NEEDED_CREDITS = 240
    result = ''

    for data in args:
        course, his_credits, max_test_point, diyan_points = data.split('-')
        current_score = int(his_credits) * (int(diyan_points) / int(max_test_point))
        diyan_courses[course] = current_score
        sum_of_courses += current_score

    if sum_of_courses < NEEDED_CREDITS:
        credits_needed = NEEDED_CREDITS - sum_of_courses
        result += f'Diyan needs {credits_needed:.1f} credits more for a diploma.\n'
    else:
        result += f'Diyan gets a diploma with {sum_of_courses:.1f} credits.\n'

    sorted_diyan_courses = dict(sorted(diyan_courses.items(), key=lambda kvp: -kvp[1]))

    for course, points in sorted_diyan_courses.items():
        result += f'{course} - {points:.1f}\n'

    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
