import csv

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
        Phone number must be exactly 10 digits.
        """
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be exactly 10 digits.")
        self._phNumber = value

    def __str__(self):
        """
        Returns a string representation of the Employee object.
        """
        return f"Employee[{self.id}]: {self.fname} {self.lname}, Dept: {self.department}, Phone: {self.phNumber}"

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
        format="%(asctime)s %(levelname)s: %(message)s"
    )

    print("Running Employee class tests...")

    test_cases = [
        # Valid
        {"id": "E100", "fname": "Jane", "lname": "Doe", "department": "HRM", "phNumber": "1234567890"},
        # Invalid first name (empty)
        {"id": "E101", "fname": "", "lname": "Smith", "department": "FIN", "phNumber": "1234567890"},
        # Invalid last name (digits)
        {"id": "E102", "fname": "Bob", "lname": "Sm1th", "department": "ITD", "phNumber": "1234567890"},
        # Invalid department (not 3 uppercase)
        {"id": "E103", "fname": "Alice", "lname": "Brown", "department": "finance", "phNumber": "1234567890"},
        # Invalid phone (not 10 digits)
        {"id": "E104", "fname": "Tom", "lname": "Lee", "department": "MKT", "phNumber": "12345"},
    ]

    for i, data in enumerate(test_cases, 1):
        try:
            emp = Employee(**data)
            print(f"Test {i}: Created employee: {emp}")
        except Exception as e:
            print(f"Test {i}: Error - {e}")
            logging.error(f"Test {i}: Failed to create employee with data {data}: {e}")
