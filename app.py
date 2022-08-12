choice = input("""
Enter Student ID\n""")


# Check if student ID exists in the database, if yes, bring the menu below.

menu = int(input("""
1. Enrolment
2. Academic Records
3. Student Account
4. Quit\n"""))

# Validating the input.
if menu==1:
    option = int(input("""Select an Option Below:
                    1. Add Classes
                    2. Drop classes
                    3. Swap classes.\n"""))
        
if menu ==2:
    # Display transcripts, with name, course id, course name, course semester, year, course's number of credits and students GPA
    print("Display academic records\n") 

if menu ==3:
    # Display student's account balance for the semester
    print("Display student's finance records\n")
