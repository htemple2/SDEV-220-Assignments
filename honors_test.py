"""
File: honors_test.py
Name: Honors Test
Author: Heidi Temple
Date: January 26, 2026
Description: This script determines if a student made the Dean's List or Honor Roll based on their GPA.
"""

while True:
    student_last_name = input("Enter student's last name or 'ZZZ' to quit: ")
    if student_last_name == 'ZZZ':
        break
    student_first_name = input("Enter student's first name: ")
    student_gpa = float(input("Enter student's GPA: "))
    if student_gpa >= 3.5:
        print(f"{student_first_name} {student_last_name} made the Dean's List.")
    elif student_gpa >= 3.25:   
        print(f"{student_first_name} {student_last_name} made the Honor Roll.")     
    else:
        print(f"{student_first_name} {student_last_name} did not make the Dean's List or Honor Roll.")
print("Goodbye!")
