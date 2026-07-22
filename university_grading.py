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
        semester = input("Enter semester name (type 'done' to finish): ")
        if semester.lower() == "done":
            break

        students[name][semester] = {}

        while True:
            subject = input("Enter subject name (type 'done' to finish semester): ")
            if subject.lower() == "done":
                break
            marks = float(input(f"Enter marks for {subject}: "))
            students[name][semester][subject] = marks

    print(f"{name} added successfully!")


def view_student():
    name = input("Enter student name to view: ")

    if name not in students:
        print("Student not found.")
        return

    print(f"\n--- Record for {name} ---")

    total_points = 0
    total_subjects = 0

    for semester, subjects in students[name].items():
        print(f"\n{semester}:")
        semester_points = 0
        semester_subject_count = 0

        for subject, marks in subjects.items():
            letter, point = get_grade(marks)
            print(f"  {subject}: {marks} -> Grade: {letter} ({point})")
            semester_points += point
            semester_subject_count += 1
            total_points += point
            total_subjects += 1

        semester_gpa = semester_points / semester_subject_count
        print(f"  Semester GPA: {semester_gpa:.2f}")

    cgpa = total_points / total_subjects
    print(f"\nOverall CGPA: {cgpa:.2f}")


def delete_student():
    name = input("Enter student name to delete: ")

    if name not in students:
        print("Student not found.")
        return

    del students[name]
    print(f"{name} has been deleted.")


def update_marks():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found.")
        return

    semester = input("Enter semester name: ")
    if semester not in students[name]:
        print("Semester not found.")
        return

    subject = input("Enter subject name: ")
    if subject not in students[name][semester]:
        print("Subject not found.")
        return

    new_marks = float(input(f"Enter new marks for {subject}: "))
    students[name][semester][subject] = new_marks
    print(f"Marks updated successfully! {subject} is now {new_marks}.")


while True:
    print("\n--- University Grading System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Update Marks")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")