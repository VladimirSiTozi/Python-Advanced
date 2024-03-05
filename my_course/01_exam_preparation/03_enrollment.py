def gather_credits(number_of_credits, *args):
    courses_enrolled = 0
    courses = []
    for credit in args:
        course_name = credit[0]
        course_credits = int(credit[1])
        if courses_enrolled < number_of_credits:
            if course_name not in courses:
                courses_enrolled += course_credits
                courses.append(course_name)
        else:
            break

    result = ''

    if courses_enrolled >= number_of_credits:
        result += f'Enrollment finished! Maximum credits: {courses_enrolled}.'
        sorted_courses = sorted(courses, key=lambda kvp: kvp)
        result += f'\nCourses: '
        result += f', '.join(sorted_courses)

    else:
        result += f'You need to enroll in more courses! You have to gather {number_of_credits - courses_enrolled}' \
                  f' credits more.'

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
