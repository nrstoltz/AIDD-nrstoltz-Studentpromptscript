import csv
import re

class Employee:
    """
    Employee class to store employee details.
    Attributes are private and accessed via getters and setters with validation.
    """

    def __init__(self, id, fname, lname, department, phNumber):
        """
        Constructor to initialize Employee object.
        ID is read-only after creation, and all other attributes go through setters for validation.
        """
        self._id = id  # Set id directly, making it read-only after creation
        self.fname = fname
        self.lname = lname
        self.department = department
        self.phNumber = phNumber

    # Getter for id (read-only)
    @property
    def id(self):
        """
        Gets the employee ID. Read-only after creation.
        """
        return self._id

    # No setter for id to make it read-only

    # Getter and setter for first name
    @property
    def fname(self):
        """
        Gets the employee's first name.
        """
        return self._fname

    @fname.setter
    def fname(self, value):
        """
        Sets the employee's first name.
        Name cannot be empty or contain digits.
        """
        if not value or any(char.isdigit() for char in value):
            raise ValueError("First name cannot be empty or contain digits.")
        self._fname = value

    # Getter and setter for last name
    @property
    def lname(self):
        """
        Gets the employee's last name.
        """
        return self._lname

    @lname.setter
    def lname(self, value):
        """
        Sets the employee's last name.
        Name cannot be empty or contain digits.
        """
        if not value or any(char.isdigit() for char in value):
            raise ValueError("Last name cannot be empty or contain digits.")
        self._lname = value

    # Getter and setter for department
    @property
    def department(self):
        """
        Gets the employee's department.
        """
        return self._department

    @department.setter
    def department(self, value):
        """
        Sets the employee's department.
        Department must be exactly 3 uppercase letters.
        """
        if not (isinstance(value, str) and len(value) == 3 and value.isupper() and value.isalpha()):
            raise ValueError("Department must be exactly 3 uppercase letters.")
        self._department = value

    # Getter and setter for phone number
    @property
    def phNumber(self):
        """
        Gets the employee's phone number, formatted as (XXX)XXX-XXXX.
        """
        num = self._phNumber
        return f"({num[:3]}){num[3:6]}-{num[6:]}"

    @phNumber.setter
    def phNumber(self, value):
        """
        Sets the employee's phone number.
        Accepts formatted numbers and sanitizes to 10 digits.
        """
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string.")
        digits = re.sub(r'\D', '', value)
        if len(digits) != 10:
            raise ValueError("Phone number must be exactly 10 digits after formatting.")
        self._phNumber = digits

    def getphNumber(self) -> str:
        """
        Returns the unformatted 10-digit phone number.
        """
        return self._phNumber

    def __str__(self):
        """
        Returns a string representation of the Employee object.
        """
        return f"Employee[{self.id}]: {self.fname} {self.lname}, Dept: {self.department}, Phone: {self.phNumber}"

class Manager(Employee):
    """
    Manager subclass of Employee, with an additional team_size attribute.
    """
    def __init__(self, id, fname, lname, department, phNumber, team_size):
        super().__init__(id, fname, lname, department, phNumber)
        self.team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError("team_size must be a non-negative integer.")
        self._team_size = value

    def __str__(self):
        return (f"Employee[{self.id}]: {self.fname} {self.lname}, Dept: {self.department}, "
                f"Phone: {self.phNumber} (Mgr, team: {self.team_size})")

def load_employees(filename="employee_data.csv"):
    """
    Loads employees from a CSV file and returns a list of Employee objects.
    CSV columns: id, fname, lname, department, phNumber
    """
    employees = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    emp = Employee(
                        id=row['id'],
                        fname=row['fname'],
                        lname=row['lname'],
                        department=row['department'],
                        phNumber=row['phNumber']
                    )
                    employees.append(emp)
                except Exception as e:
                    # Skip invalid rows
                    continue
    except FileNotFoundError:
        pass  # Return empty list if file does not exist
    return employees

def save_employees(employees, filename="employee_data.csv"):
    """
    Saves a list of Employee objects to a CSV file.
    CSV columns: id, fname, lname, department, phNumber
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'fname', 'lname', 'department', 'phNumber']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for emp in employees:
            writer.writerow({
                'id': emp.id,
                'fname': emp.fname,
                'lname': emp.lname,
                'department': emp.department,
                'phNumber': emp._phNumber  # Store raw digits
            })

def create_employee(employees, id, fname, lname, department, phNumber, filename="employee_data.csv"):
    """
    Adds a new Employee to the list and saves to CSV.
    Raises ValueError if an employee with the same ID already exists.
    """
    if any(emp.id == id for emp in employees):
        raise ValueError(f"Employee with ID {id} already exists.")
    try:
        new_emp = Employee(id, fname, lname, department, phNumber)
        employees.append(new_emp)
        save_employees(employees, filename)
        return new_emp
    except Exception as e:
        raise ValueError(f"Failed to create employee: {e}")

def edit_employee(employees, index, fname=None, lname=None, department=None, phNumber=None, filename="employee_data.csv"):
    """
    Edits an existing Employee (by index). Does not allow changing ID.
    Only updates provided fields. Raises IndexError or ValueError on error.
    """
    if not (0 <= index < len(employees)):
        raise IndexError("Employee index out of range.")
    emp = employees[index]
    try:
        if fname is not None:
            emp.fname = fname
        if lname is not None:
            emp.lname = lname
        if department is not None:
            emp.department = department
        if phNumber is not None:
            emp.phNumber = phNumber
        save_employees(employees, filename)
        return emp
    except Exception as e:
        raise ValueError(f"Failed to edit employee: {e}")

def delete_employee(employees, index, filename="employee_data.csv"):
    """
    Deletes an Employee by index. Raises IndexError if index is invalid.
    """
    if not (0 <= index < len(employees)):
        raise IndexError("Employee index out of range.")
    try:
        removed = employees.pop(index)
        save_employees(employees, filename)
        return removed
    except Exception as e:
        raise ValueError(f"Failed to delete employee: {e}")

def display_employees(employees):
    """
    Prints a list of employees in the format:
    1. ID - Last, First - Department - Phone
    """
    if not employees:
        print("No employees to display.")
        return
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. {emp.id} - {emp.lname}, {emp.fname} - {emp.department} - {emp.phNumber}")

if __name__ == "__main__":
    import logging

    logging.basicConfig(
        filename="employee_test.log",
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s: %(message)s",
        filemode="a"
    )

    print("=== Employee/Manager Validation Tests ===")

    # Valid Employee
    try:
        emp1 = Employee("E001", "Alice", "Smith", "HRM", "123-456-7890")
        print("Created valid Employee:", emp1)
    except Exception as e:
        print("Failed to create valid Employee:", e)
        logging.error(f"Valid Employee creation failed: {e}")

    # Invalid Employees
    invalid_cases = [
        {"id": "E002", "fname": "", "lname": "Jones", "department": "ITD", "phNumber": "1234567890", "desc": "Empty first name"},
        {"id": "E003", "fname": "Bob", "lname": "J0nes", "department": "ITD", "phNumber": "1234567890", "desc": "Last name contains digit"},
        {"id": "E004", "fname": "Carol", "lname": "White", "department": "itd", "phNumber": "1234567890", "desc": "Department not uppercase"},
        {"id": "E005", "fname": "Dan", "lname": "Brown", "department": "MKT", "phNumber": "12345", "desc": "Phone number too short"},
        {"id": "E006", "fname": "Eve", "lname": "Black", "department": "MKT", "phNumber": "abcdefghij", "desc": "Phone number not digits"},
    ]
    for case in invalid_cases:
        try:
            emp = Employee(case["id"], case["fname"], case["lname"], case["department"], case["phNumber"])
            print(f"ERROR: Created invalid Employee ({case['desc']}):", emp)
        except Exception as e:
            print(f"Correctly failed to create Employee ({case['desc']}):", e)
            logging.error(f"Invalid Employee ({case['desc']}): {e}")

    # Valid Manager
    try:
        mgr1 = Manager("M001", "Grace", "Hopper", "ENG", "(555) 321-9876", 5)
        print("Created valid Manager:", mgr1)
    except Exception as e:
        print("Failed to create valid Manager:", e)
        logging.error(f"Valid Manager creation failed: {e}")

    # Invalid Manager (negative team size)
    try:
        mgr2 = Manager("M002", "Henry", "Ford", "ENG", "555.123.4567", -3)
        print("ERROR: Created invalid Manager (negative team size):", mgr2)
    except Exception as e:
        print("Correctly failed to create Manager (negative team size):", e)
        logging.error(f"Invalid Manager (negative team size): {e}")

    # Invalid Manager (bad phone)
    try:
        mgr3 = Manager("M003", "Ivy", "Lee", "ENG", "555", 2)
        print("ERROR: Created invalid Manager (bad phone):", mgr3)
    except Exception as e:
        print("Correctly failed to create Manager (bad phone):", e)
        logging.error(f"Invalid Manager (bad phone): {e}")
