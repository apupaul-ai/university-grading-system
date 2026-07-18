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


def view_student():
    name = input("Enter student name to view: ")

    if name not in students:
        print("Student not found.")
        return

    print(f"\n--- Record for {name} ---")
    for subject, marks in students[name].items():
        print(f"{subject}: {marks}")


while True:
    print("\n--- University Grading System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")