# Employee Management App

## Overview

This is a simple Employee Management System built in Python. It uses a CSV file for data storage and separates business logic from the user interface.

## How to Run

1. **Install Python**  
   Make sure you have Python 3.x installed.

2. **Clone or Download the Repository**  
   Open a terminal and navigate to the project folder.

3. **Run the Application**  
   ```
   python EmployeeApp.py
   ```

   This will start the menu-driven CLI for managing employees.

4. **Run Employee Class Tests**  
   To run the validation tests and generate `employee_test.log`:
   ```
   python employee.py
   ```

## Files

- `employee.py` — Business logic, Employee class, validation rules, CSV load/save, CRUD functions, and tests.
- `EmployeeApp.py` — CLI menu for interacting with employees.
- `employee_data.csv` — Data storage (created automatically).
- `employee_test.log` — Log file for test errors (created by running `employee.py`).
- `.prompt/dev_notes.md` — Prompt history, outputs, and reflections.

## Requirements

- Python 3.x
- No external dependencies required.
