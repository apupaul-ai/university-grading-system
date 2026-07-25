import json

students = {}


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)


def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
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


def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if marks < 0 or marks > 100:
                print("Error! Marks must be between 0 and 100. Try again.")
                continue
            return marks
        except ValueError:
            print("Error! Please enter a valid number.")


def get_valid_credit(subject):
    while True:
        try:
            credit = float(input(f"Enter credit hours for {subject}: "))
            if credit <= 0:
                print("Error! Credit hours must be greater than 0. Try again.")
                continue
            return credit
        except ValueError:
            print("Error! Please enter a valid number.")


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
            marks = get_valid_marks(subject)
            credit = get_valid_credit(subject)
            students[name][semester][subject] = {"marks": marks, "credit": credit}

    print(f"{name} added successfully!")
    save_data()


def view_student():
    name = input("Enter student name to view: ")

    if name not in students:
        print("Student not found.")
        return

    print(f"\n--- Record for {name} ---")

    total_weighted_points = 0
    total_credits = 0

    for semester, subjects in students[name].items():
        print(f"\n{semester}:")
        semester_weighted_points = 0
        semester_credits = 0

        for subject, data in subjects.items():
            marks = data["marks"]
            credit = data["credit"]
            letter, point = get_grade(marks)
            print(f"  {subject}: {marks} (Credit: {credit}) -> Grade: {letter} ({point})")
            semester_weighted_points += point * credit
            semester_credits += credit
            total_weighted_points += point * credit
            total_credits += credit

        semester_gpa = semester_weighted_points / semester_credits
        print(f"  Semester GPA: {semester_gpa:.2f}")

    cgpa = total_weighted_points / total_credits
    print(f"\nOverall CGPA: {cgpa:.2f}")


def view_all_students():
    if not students:
        print("No students added yet.")
        return

    print("\n--- All Students ---")
    for name in students:
        total_weighted_points = 0
        total_credits = 0

        for semester, subjects in students[name].items():
            for subject, data in subjects.items():
                letter, point = get_grade(data["marks"])
                total_weighted_points += point * data["credit"]
                total_credits += data["credit"]

        if total_credits > 0:
            cgpa = total_weighted_points / total_credits
            print(f"{name} - CGPA: {cgpa:.2f}")


def delete_student():
    name = input("Enter student name to delete: ")

    if name not in students:
        print("Student not found.")
        return

    del students[name]
    print(f"{name} has been deleted.")
    save_data()


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

    new_marks = get_valid_marks(subject)
    students[name][semester][subject]["marks"] = new_marks
    print(f"Marks updated successfully! {subject} is now {new_marks}.")
    save_data()


def show_ranking():
    if not students:
        print("No students added yet.")
        return

    cgpa_list = []

    for name in students:
        total_weighted_points = 0
        total_credits = 0

        for semester, subjects in students[name].items():
            for subject, data in subjects.items():
                letter, point = get_grade(data["marks"])
                total_weighted_points += point * data["credit"]
                total_credits += data["credit"]

        if total_credits > 0:
            cgpa = total_weighted_points / total_credits
            cgpa_list.append((name, cgpa))

    sorted_list = sorted(cgpa_list, key=lambda x: x[1], reverse=True)

    print("\n--- Class Ranking ---")
    rank = 1
    for name, cgpa in sorted_list:
        print(f"{rank}. {name} - CGPA: {cgpa:.2f}")
        rank += 1


load_data()

while True:
    print("\n" + "=" * 40)
    print("     UNIVERSITY GRADING SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Show Class Ranking")
    print("7. Exit")
    print("=" * 40)

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        view_all_students()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_marks()
    elif choice == "6":
        show_ranking()
    elif choice == "7":
        print("Thank you for using the University Grading System!")
        break
    else:
        print("Invalid choice! Please select 1-7.")