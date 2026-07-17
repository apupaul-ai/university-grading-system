# University Grading System

A command-line grading system built in Python that manages multiple students, each with multiple subjects, and calculates GPA on a 4.0 scale (Bangladesh university style).

## Features

- **Multiple Students:** Store records for any number of students
- **Multiple Subjects per Student:** Add as many subjects and marks as needed
- **GPA Calculation:** Converts marks to grade points and calculates GPA on a 4.0 scale
- **Nested Data Structure:** Uses dictionaries to organize student and subject data

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

Follow the on-screen menu to add students, enter subjects and marks, and view results.

## Built With

- Python 3
- Core concepts used: nested dictionaries, loops, functions, type conversion

## Project Journey

This project is being built step by step as part of a daily Python practice routine, adding one feature at a time (add student, view records, GPA calculation, error handling, file storage, and more).

## Author

Apu Paul