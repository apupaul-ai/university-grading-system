students = {}

def get_grade(marks):
    if marks >= 80:
        return "A+", 4.00
    elif marks >= 75:
        return "A", 3.75
    elif marks >= 70:
        return "A-", 3.50
    elif marks >= 65:
        return "B+", 3.25
    elif marks >= 60:
        return "B", 3.00
    elif marks >= 55:
        return "B-", 2.75
    elif marks >= 50:
        return "C+", 2.50
    elif marks >= 45:
        return "C", 2.25
    elif marks >= 40:
        return "D", 2.00
    else:
        return "F", 0.00


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
        letter, point = get_grade(marks)
        print(f"{subject}: {marks} -> Grade: {letter} ({point})")


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