# Name: Van Duc Tran
# File name: main.py
# Description: the Python app will accept student's name and GPA and test if the student qualifies for either the Dean's List or the Honor Roll.


last_name = str(input("Please enter student's last name (enter 'ZZZ' to quit): "))

while (last_name != 'ZZZ'):
    
    first_name = str(input("Please enter student's first name: "))
    studentGPA = float(input("Please enter student's GPA: "))
    
    if (studentGPA >= 3.5):
        print(first_name, last_name, "has made the Dean's List.")
        break
    elif (studentGPA >= 3.25):
        print(first_name, last_name, "has made the Honor Roll.")
        break
    else:
        print(first_name, last_name, "has not made the Dean's List or Honor Roll.")
        break