# Student Attendance Calculator

## 1. Project Overview

The **Student Attendance Calculator** is a Python-based command-line application used to manage and analyze student attendance.

The program allows the user to:

* Generate an attendance report for a student.
* Calculate attendance percentage for each subject.
* Check whether a student is eligible based on the 75% attendance requirement.
* Calculate the number of additional classes required to reach 75% attendance.
* Analyze attendance for the entire class.
* Display attendance reports for all students.

The project is designed to run completely through the **command line/terminal**.

---

## 2. Technologies Used

* **Programming Language:** Python 3
* **Interface:** Command Line Interface (CLI)
* **Data Storage:** Python Dictionary
* **Editor:** Visual Studio Code

No external Python libraries are required.

---

## 3. Project Structure

```text
Student-Attendance-Calculator/
│
├── attendance.py
└── README.md
```

### Files Description

| File            | Description                            |
| --------------- | -------------------------------------- |
| `attendance.py` | Contains the complete Python program   |
| `README.md`     | Project documentation and instructions |

---

## 4. Requirements

Before running the project, make sure the following software is installed:

### Python

Python 3.8 or later is recommended.

Check whether Python is installed by opening a terminal and running:

```bash
python --version
```

If that does not work on Windows, try:

```bash
py --version
```

The terminal should display the installed Python version.

---

## 5. Installation and Setup

### Step 1: Install Python

Download and install Python from the official Python website.

During installation on Windows, make sure to select:

```text
Add Python to PATH
```

before clicking **Install Now**.

### Step 2: Install Visual Studio Code

Install Visual Studio Code if it is not already installed.

Open Visual Studio Code after installation.

### Step 3: Create the Project Folder

Create a folder named:

```text
Student-Attendance-Calculator
```

Open this folder in Visual Studio Code.

### Step 4: Create the Python File

Inside the project folder, create a file named:

```text
attendance.py
```

Paste the complete Student Attendance Calculator Python program into this file.

### Step 5: Create README.md

In the same project folder, create:

```text
README.md
```

This README file contains the project documentation.

---

## 6. Dependencies

This project does **not require any external Python packages**.

All functionality is implemented using Python's built-in features.

Therefore, no `pip install` command is required.

---

## 7. How to Run the Project

### Using Visual Studio Code Terminal

Open the project folder in Visual Studio Code.

Open the terminal using:

```text
Terminal → New Terminal
```

Navigate to the project folder if necessary.

Run the program using:

```bash
python attendance.py
```

On some Windows systems, you can also use:

```bash
py attendance.py
```

---

## 8. Program Menu

After starting the program, the following menu is displayed:

```text
STUDENT ATTENDANCE CALCULATOR

1. Student Attendance Report
2. Attendance Shortage
3. Class Attendance Analysis
4. Display All Students
5. Exit

Enter your choice:
```

The user can enter a number from `1` to `5`.

---

## 9. Features

### 1. Student Attendance Report

Enter a student ID such as:

```text
S101
```

The program displays:

* Student ID
* Student name
* Subject-wise attendance
* Attendance percentage
* Eligibility status
* Total classes
* Classes attended
* Overall attendance percentage
* Overall status

Example:

```text
Student ID : S101
Name       : Omkar Kharat

Subject : Python
Attended: 42 / 50
Percentage: 84.0 %
Status: ELIGIBLE
```

---

### 2. Attendance Shortage

This option checks subjects where attendance is below 75%.

For example:

```text
ATTENDANCE SHORTAGE

Python: 70.0% Attend 2 more class(es)
```

The program calculates how many additional classes the student needs to attend continuously to reach 75%.

If attendance is already 75% or above, it displays:

```text
No shortage
```

---

### 3. Class Attendance Analysis

This option calculates the attendance percentage of every student in the class.

It also calculates the overall class attendance.

Example:

```text
CLASS ANALYSIS

S101 Omkar Kharat: 81.74%
S102 Yash Ghodke: 93.96%
S103 Ganesh Reddy: 70.43%
S104 Dhurv Kumar: 84.35%

Overall Class Attendance: ...
```

---

### 4. Display All Students

This option generates attendance reports for all students stored in the program.

The program processes each student ID automatically and displays their complete attendance report.

---

### 5. Exit

Selecting:

```text
5
```

closes the program.

The program displays:

```text
Thank you
```

---

## 10. Student Data

The program currently contains attendance data for four students:

| Student ID | Name         |
| ---------- | ------------ |
| S101       | Omkar Kharat |
| S102       | Yash Ghodke  |
| S103       | Ganesh Reddy |
| S104       | Dhurv Kumar  |

The attendance data is stored using nested Python dictionaries.

Example:

```python
"S101": {
    "name": "Omkar Kharat",
    "attendance": {
        "Python": [42, 50],
        "Mathematics": [45, 50],
        "English": [38, 45],
        "EVS": [40, 50],
        "Physics": [43, 50]
    }
}
```

The first value represents classes attended and the second value represents total classes.

For example:

```text
[42, 50]
```

means:

```text
42 classes attended out of 50 classes
```

---

## 11. Attendance Calculation

The attendance percentage is calculated using:

```text
Attendance Percentage =
(Classes Attended / Total Classes) × 100
```

For example:

```text
Attended = 42
Total = 50

Percentage = (42 / 50) × 100
           = 84%
```

The student is therefore:

```text
ELIGIBLE
```

because the attendance is at least 75%.

---

## 12. Eligibility Criteria

The project uses a minimum attendance requirement of **75%**.

```text
Attendance >= 75%  → ELIGIBLE

Attendance < 75%   → SHORTAGE
```

---

## 13. Configuration

There are no external configuration files or environment variables required.

To add or modify students, edit the `students` dictionary inside:

```text
attendance.py
```

For example:

```python
"S105": {
    "name": "New Student",
    "attendance": {
        "Python": [40, 50],
        "Mathematics": [42, 50],
        "English": [38, 45],
        "EVS": [44, 50],
        "Physics": [41, 50]
    }
}
```

---

## 14. Troubleshooting

### Python command not recognized

If this command:

```bash
python --version
```

does not work, try:

```bash
py --version
```

If neither command works, install Python and make sure Python is added to the system PATH.

---

### File not found

Make sure the terminal is opened inside the project folder.

You can check the files using:

```bash
dir
```

Then run:

```bash
python attendance.py
```

---

### Invalid Student ID

If an ID that does not exist is entered, the program displays:

```text
id not found
```

Use one of the available IDs:

```text
S101
S102
S103
S104
```

---

## 15. Example Execution

```text
STUDENT ATTENDANCE CALCULATOR

1. Student Attendance Report
2. Attendance Shortage
3. Class Attendance Analysis
4. Display All Students
5. Exit

Enter your choice: 1

Enter Student ID: S101

STUDENT ATTENDANCE REPORT
Student ID : S101
Name       : Omkar Kharat

Subject wise Attendance

Subject : Python
Attended: 42 / 50
Percentage: 84.0 %
Status: ELIGIBLE
```

---

## 16. Conclusion

The Student Attendance Calculator provides a simple command-line solution for managing and analyzing student attendance.

It demonstrates the use of:

* Python dictionaries
* Nested dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Attendance percentage calculations
* String formatting
* Command-line programming

The project can be further extended by adding features such as file storage, student registration, attendance updating, and report generation.
