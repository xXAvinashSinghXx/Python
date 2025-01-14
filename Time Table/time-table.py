# Input Time Table of whole classes of the school
tt = {
    "XIA": {"Math": {"teacher": "komal", "period": [1, 2]},
            "Physic": {"teacher": "ks", "period": [3, 4]},
            "Chemistry": {"teacher": "ksp", "period": [5, 6]},
            "English": {"teacher": "voice", "period": [7, 8]}
            },
    "XIB": {"Math": {"teacher": "komal", "period": 1},
            "Physic": {"teacher": "ks", "period": 2},
            "Chemistry": {"teacher": "ksp", "period": 3},
            "English": {"teacher": "voice", "period": 4}
            }
}

# | Class >> Subject, Period, Teacher |
while True:
    print("----------------------------------------")
    
    # Class
    Class = input("Enter a class (Eg: XIA, XIB... or 'exit' to stop): ").strip()

    if Class.lower() == 'exit':
        print("Exiting the timetable program. Goodbye!")
        break

    # Subject/Period/Teacher
    if Class in tt:
        print(f"Class {Class} selected.")
        Choice = input("Enter a choice (subject, period, teacher): ").strip()

        # Subject
        if Choice.lower() == "subject":
            Subject = input("Enter a subject name (Eg: Math, Physic...): ").strip()

            if Subject in tt[Class]:
                subject_details = tt[Class][Subject]
                print(f"Subject: {Subject}")
                print(f"Teacher: {subject_details['teacher']}")
                print(f"Period: {subject_details['period']}")
            else:
                print(f"Subject '{Subject}' not found in class {Class}. Please try again.")

        # Period
        elif Choice.lower() == "period":
            try:
                Period = int(input("Enter a period number (1-8): ").strip())
                found = False

                for subject, details in tt[Class].items():
                    periods = details['period'] if isinstance(details['period'], list) else [details['period']]
                    if Period in periods:
                        print(f"Period {Period} is for:")
                        print(f"Subject: {subject}")
                        print(f"Teacher: {details['teacher']}")
                        found = True
                        break

                if not found:
                    print(f"No subject found for period {Period} in class {Class}.")

            except ValueError:
                print("Invalid period number. Please enter a number between 1 and 8.")

        # Teacher
        elif Choice.lower() == "teacher":
            Teacher = input("Enter a teacher's name: ").strip()
            found = False

            for subject, details in tt[Class].items():
                if details['teacher'].lower() == Teacher.lower():
                    print(f"Teacher {Teacher}")
                    print(f"Subject: {subject}")
                    print(f"Period: {details['period']}")
                    found = True
                    break

            if not found:
                print(f"Teacher '{Teacher}' not found in class {Class}.")

        else:
            print("Invalid choice. Please enter 'subject', 'period', or 'teacher'.")

    else:
        print(f"Class '{Class}' not found. Please try again.")
