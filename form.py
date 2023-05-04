name = input("Name: ")
age = int(input("Age: "))
qualification = input("Qualification: ")
contact_number = input("Contact Number: ")
address = input("Address: ")
email = input("Email: ")
interested_area = input("Interested Area: ")
description = input("Description: ")
salary_expectation = int(input("Salary Expectation: "))
experience = int(input("Experience (in years): "))

if salary_expectation > 20000:
    if experience >= 2:
        print("You are shortlisted. Your enquiry has been recorded. We will notify you. Thank you!!")
    else:
        print("Your work experience must be at least 2 years.")
else:
    print("Your enquiry has been recorded. We will notify you. Thank you!!")
