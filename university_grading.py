students = {}

def add_student():
    name = input("Enter student name: ")
    students[name] = {}

    while True:
        subject = input("Enter subject name (type 'done' to finish): ")
        if subject.lower() == "done":
            break
        marks = float(input(f"Enter marks for {subject}: "))
        students[name][subject] = marks

    print(f"{name} added successfully with {len(students[name])} subject(s)!")


while True:
    print("\n--- University Grading System ---")
    print("1. Add Student")
    print("2. Exit")

    choice = input("Choose an option (1-2): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")