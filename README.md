# Assignment 3 - HR Employee Management System (MVC)

## Overview

This project is an Employee Management System built in Python using an MVC (Model-View-Controller) design.

- **Model (`employee.py`)** defines the `Employee` and `Manager` classes with validation rules.
- **Data (`EmployeeData.py`)** handles CSV file storage, including persistence of both Employees and Managers.
- **View (`EmployeeView.py`)** provides menu display, prompts, and user-facing messages.
- **Controller (`EmployeeApp.py`)** drives the menu loop, routing user input to the correct logic.

### Features

- Add, edit, delete, and list employees/managers
- Input validation (names, department codes, phone numbers, team size for managers)
- Persistent CSV storage (`employee_data.csv`)
- Logging of invalid test cases to `employee_test.log`

## How to Run

1. **Install Python**

   Make sure you have Python 3.x installed.

2. **Navigate to the Project Folder**

   In a terminal, move into the assignment directory:

   ```
   cd Assignment3-mvc
   ```

3. **Run the Application**

   Start the interactive menu:

   ```
   python EmployeeApp.py
   ```

   This launches the CLI menu where you can:
   - List all employees
   - Add new employees or managers
   - Edit existing records
   - Delete employees
   - Quit the program

4. **Run Validation Tests**

   To run validation tests and generate `employee_test.log`:

   ```
   python employee.py
   ```

   This will:
   - Create valid Employee and Manager objects
   - Attempt invalid cases (empty name, invalid department, bad phone, negative team size)
   - Print results to the terminal
   - Log failures to `employee_test.log`

## Files

- `employee.py` — Core business logic, including Employee and Manager classes, validation rules, CRUD helpers, and validation tests.
- `EmployeeData.py` — Handles CSV load/save with support for both Employees and Managers.
- `EmployeeView.py` — Provides menu display, user prompts, and formatted output.
- `EmployeeApp.py` — Main CLI menu (controller) that links the Model, View, and Data.
- `employee_data.csv` — Data storage file, created/updated automatically.
- `employee_test.log` — Log file with error messages from invalid test cases.
- `.prompt/dev_notes.md` — Development log showing Copilot prompts, outputs, and full reflections.

## Sample Input/Output

### CLI Menu Example

```
Employee Management Menu
1. List Employees
2. Add Employee
3. Edit Employee
4. Delete Employee
5. Quit
Select an option (1-5): 2
ID: E500
First Name: Ava
Last Name: Wells
Department (3 uppercase letters): FIN
Phone Number (10 digits or formatted): 2223334444
Is this a manager? (y/n): n
Employee added.
```

After listing:

```
1. Employee[E500]: Ava Wells, Dept: FIN, Phone: (222)333-4444
```

### Adding a Manager

```
Select an option (1-5): 2
ID: M501
First Name: Raj
Last Name: Singh
Department (3 uppercase letters): ENG
Phone Number (10 digits or formatted): 333-444-5555
Is this a manager? (y/n): y
Team Size: 12
Employee added.
```

Listing again:

```
1. Employee[E500]: Ava Wells, Dept: FIN, Phone: (222)333-4444
2. Employee[M501]: Raj Singh, Dept: ENG, Phone: (333)444-5555 (Mgr, team: 12)
```

### Running Tests

```
=== Employee/Manager Validation Tests ===
Created valid Employee: Employee[E001]: Alice Smith, Dept: HRM, Phone: (123)456-7890
Correctly failed to create Employee (Empty first name): First name cannot be empty or contain digits.
Correctly failed to create Employee (Last name contains digit): Last name cannot be empty or contain digits.
Correctly failed to create Employee (Department not uppercase): Department must be exactly 3 uppercase letters.
Correctly failed to create Employee (Phone number too short): Phone number must be exactly 10 digits after formatting.
Correctly failed to create Employee (Phone number not digits): Phone number must be exactly 10 digits after formatting.
Created valid Manager: Employee[M001]: Grace Hopper, Dept: ENG, Phone: (555)321-9876 (Mgr, team: 5)
Correctly failed to create Manager (negative team size): team_size must be a non-negative integer.
Correctly failed to create Manager (bad phone): Phone number must be exactly 10 digits after formatting.
```

### Sample Log Output (`employee_test.log`)

```
2025-09-16 20:24:52,966 ERROR: Invalid Employee (Phone number not digits): Phone number must be exactly 10 digits after formatting.
2025-09-16 20:25:04,427 ERROR: Invalid Manager (bad phone): Phone number must be exactly 10 digits after formatting.
```
