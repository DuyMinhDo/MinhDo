students = []
courses = []
marks = {}

# Input number of students in a class
num_students = int(input("Enter number of students: "))

# Input student information: id, name, DoB
for i in range(num_students):
    id = input(f"Enter student {i+1} ID: ")
    name = input(f"Enter student {i+1} name: ")
    dob = input(f"Enter student {i+1} date of birth: ")
    student = (id, name, dob)
    students.append(student) #using tuple

# Input number of courses
num_courses = int(input("Enter number of courses: "))

# Input course information: id, name
for i in range(num_courses):
    id = input(f"Enter course {i+1} ID: ")
    name = input(f"Enter course {i+1} name: ")
    course = (id, name)
    courses.append(course) #using tuple

# Select a course, input marks for student in this course
while True: #loop until the input is q
    course_id = input("Enter course ID (or 'q' to quit): ")
    if course_id == 'q':
        break
    course = None
    for c in courses:
        if c[0] == course_id:
            course = c
            break
    if not course:
        print("Invalid course ID")
        continue
    for student in students:
        marks[(student[0], course_id)] = input(f"Enter marks for {student[1]}: ")

# List courses
print("Courses:")
for course in courses:
    print(f"{course[0]} {course[1]}")

# List students
print("Students:")
for student in students:
    print(f"{student[0]} {student[1]} {student[2]}")

# Show student marks for a given course using python
while True: #loop until the input is q
    student_id = input("Enter student ID (or 'q' to quit): ")
    if student_id == 'q':
        break
    student = None
    for s in students:
        if s[0] == student_id:
            student = s
            break
    if not student:
        print("Invalid student ID")
        continue
    course_id = input("Enter course ID: ")
    marks_for_student = marks.get((student_id, course_id))
    if not marks_for_student:
        print("No marks found")
    else:
        print(f"Marks for {student[1]} in {course_id}: {marks_for_student}")
