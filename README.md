# University Grading System

A command-line grading system built in Python that manages multiple students across multiple semesters and subjects, automatically calculating GPA and CGPA on a 4.0 scale (Bangladesh university style).

## Features

- **Multiple Students:** Store and manage records for any number of students
- **Semester-Wise Subjects:** Each student can have multiple semesters, each with its own set of subjects and marks
- **Automatic Grade Conversion:** Marks are converted into letter grades and grade points automatically
- **GPA & CGPA Calculation:** Calculates GPA per semester and an overall CGPA across all semesters
- **View All Students:** Quick overview of every student's CGPA
- **Update & Delete:** Update marks for any subject, or remove a student entirely
- **Class Ranking:** Ranks all students by CGPA, highest first
- **Input Validation:** Handles invalid input gracefully (non-numeric values, marks outside 0-100)
- **Persistent Storage:** Saves all data to a JSON file, so records are not lost when the program closes

## GPA Scale

| Marks Range | Letter Grade | Grade Point |
|-------------|--------------|-------------|
| 80-100 | A+ | 4.00 |
| 75-79 | A | 3.75 |
| 70-74 | A- | 3.50 |
| 65-69 | B+ | 3.25 |
| 60-64 | B | 3.00 |
| 55-59 | B- | 2.75 |
| 50-54 | C+ | 2.50 |
| 45-49 | C | 2.25 |
| 40-44 | D | 2.00 |
| 0-39 | F | 0.00 |

## How to Run

```bash
python university_grading.py
```

## Menu Options

```
========================================
     UNIVERSITY GRADING SYSTEM
========================================
1. Add Student
2. View Student
3. View All Students
4. Delete Student
5. Update Marks
6. Show Class Ranking
7. Exit
========================================
```

## Example Usage

```
Choose an option (1-7): 1
Enter student name: Rahim
Enter semester name (type 'done' to finish): Semester 1
Enter subject name (type 'done' to finish semester): Math
Enter marks for Math: 85
Enter subject name (type 'done' to finish semester): Physics
Enter marks for Physics: 78
Enter subject name (type 'done' to finish semester): done
Enter semester name (type 'done' to finish): done
Rahim added successfully!
```

## Built With

- Python 3
- Core concepts used: nested dictionaries, loops, functions, tuples, `sorted()` with `lambda`, `try/except`, file handling with `json`

## Project Journey

This project was built step by step over 10 days as part of a daily Python practice routine:

| Day | Feature Added |
|-----|----------------|
| 1 | Add student with multiple subjects |
| 2 | View student with all subjects |
| 3 | Marks to grade point conversion |
| 4 | Semester structure with GPA and CGPA calculation |
| 5 | Update marks and delete student |
| 6 | Input validation (invalid text and out-of-range marks) |
| 7 | Class ranking sorted by CGPA |
| 8 | Save and load data using JSON |
| 9 | View all students and polished menu design |
| 10 | Final documentation and cleanup |

## Author

Apu Paul