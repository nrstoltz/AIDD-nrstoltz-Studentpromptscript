from employee import Employee, Manager
import csv

CSV_FIELDS = ["id", "fname", "lname", "department", "phNumber", "role", "team_size"]

def load_employees(filename="employee_data.csv"):
    """
    Loads employees from a CSV file. Creates Employee or Manager objects based on the 'role' column.
    If 'role' is missing or not 'Manager', creates an Employee.
    If 'team_size' is missing or blank, defaults to 0.
    Skips invalid rows safely.
    Returns a list of Employee and Manager objects.
    """
    employees = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    role = row.get("role", "Employee")
                    team_size_str = row.get("team_size", "")
                    team_size = int(team_size_str) if team_size_str.strip().isdigit() else 0
                    if role == "Manager":
                        emp = Manager(
                            id=row["id"],
                            fname=row["fname"],
                            lname=row["lname"],
                            department=row["department"],
                            phNumber=row["phNumber"],
                            team_size=team_size
                        )
                    else:
                        emp = Employee(
                            id=row["id"],
                            fname=row["fname"],
                            lname=row["lname"],
                            department=row["department"],
                            phNumber=row["phNumber"]
                        )
                    employees.append(emp)
                except Exception:
                    continue  # Skip invalid rows
    except FileNotFoundError:
        pass
    return employees

def save_employees(employees, filename="employee_data.csv"):
    """
    Saves a list of Employee and Manager objects to a CSV file.
    Always writes the header row. For each employee:
    - Outputs raw phone digits using getphNumber().
    - Writes role as 'Manager' if Manager, else 'Employee'.
    - Writes team_size if Manager, else 0.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for emp in employees:
            row = {
                "id": emp.id,
                "fname": emp.fname,
                "lname": emp.lname,
                "department": emp.department,
                "phNumber": emp.getphNumber(),
                "role": "Manager" if isinstance(emp, Manager) else "Employee",
                "team_size": emp.team_size if isinstance(emp, Manager) else 0
            }
            writer.writerow(row)
