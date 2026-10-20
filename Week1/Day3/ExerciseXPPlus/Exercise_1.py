# ===== Exercise_1.py =====
# Exercise 1: Student Grade Summary
#
# What you learn here:
#   - Looping through a dictionary with .items()
#   - Lists as dictionary values, sum() and len() for averages
#   - if/elif/else to assign letter grades
#   - Filling new dictionaries inside a loop, f-string formatting
#
# Instructions:
#   You are given a dictionary containing student names as keys and lists of
#   their grades as values. Your task is to create a summary report that
#   calculates the average grade for each student, assigns a letter grade,
#   and determines the class average.
#
# Initial Data:
#   student_grades = {
#       "Alice": [88, 92, 100],
#       "Bob": [75, 78, 80],
#       "Charlie": [92, 90, 85],
#       "Dana": [83, 88, 92],
#       "Eli": [78, 80, 72]
#   }
#
# Requirements:
#   1. Calculate the average grade for each student and store the results in
#      a new dictionary called student_averages.
#   2. Assign each student a letter grade (A, B, C, D, F) based on their
#      average grade according to the following scale, and store the results
#      in a dictionary called student_letter_grades:
#        A: 90 and above
#        B: 80 to 89
#        C: 70 to 79
#        D: 60 to 69
#        F: Below 60
#   3. Calculate the class average (the average of all students' averages)
#      and print it.
#   4. Print the name of each student, their average grade, and their
#      letter grade.
#
# Hints:
#   - Use loops to iterate through the student_grades dictionary.
#   - You may use sum() and len() functions to help calculate averages.
#   - Initialize empty dictionaries for student_averages and
#     student_letter_grades before filling them with data.

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Calculate the average grade for each student
student_averages = {}
for name, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[name] = average

# Assign each student a letter grade based on their average grade
student_letter_grades = {}
for name, avg in student_averages.items():
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    student_letter_grades[name] = grade

# Calculate the class average
total_average = sum(student_averages.values())
class_size = len(student_averages)
class_average = total_average / class_size

print(student_averages)
print(student_letter_grades)
print(class_average)

# Print each student's name, average and letter grade
max_name_length = max(len(name) for name in student_grades.keys())

for name in student_grades.keys():
    spaces = ' ' * (max_name_length - len(name))
    print(f"{name}:{spaces} Average Grade = {student_averages[name]:.2f}, Letter Grade = {student_letter_grades[name]}")
