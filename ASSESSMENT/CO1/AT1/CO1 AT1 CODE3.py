import re

# Get input
reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

# Register Number Validation (Example: 23IT101)
if re.fullmatch(r"\d{2}[A-Z]{2}\d{3}", reg_no):
    print("Register Number: Valid")
    reg_valid = True
else:
    print("Register Number: Invalid")
    reg_valid = False

# Email Validation (Example: student@university.edu)
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@university\.edu", email):
    print("Email: Valid")
    email_valid = True
else:
    print("Email: Invalid")
    email_valid = False

# Course Code Validation (Example: CS101)
if re.fullmatch(r"[A-Z]{2,3}\d{3}", course):
    print("Course Code: Valid")
    course_valid = True
else:
    print("Course Code: Invalid")
    course_valid = False

# Semester Validation (1 to 8)
if re.fullmatch(r"[1-8]", semester):
    print("Semester: Valid")
    sem_valid = True
else:
    print("Semester: Invalid")
    sem_valid = False

# Mobile Number Validation
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number: Valid")
    mobile_valid = True
else:
    print("Mobile Number: Invalid")
    mobile_valid = False

# Final Status
if reg_valid and email_valid and course_valid and sem_valid and mobile_valid:
    print("\nRegistration Status: Successful")
else:
    print("\nRegistration Status: Failed")
