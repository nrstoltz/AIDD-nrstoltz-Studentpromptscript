def show_menu() -> str:
    """Prints the main menu and returns the user's choice as a string."""
    print("\nEmployee Management Menu")
    print("1. List Employees")
    print("2. Add Employee")
    print("3. Edit Employee")
    print("4. Delete Employee")
    print("5. Quit")
    return input("Select an option (1-5): ").strip()

def show_employees(employees):
    """Prints a numbered list of employees using their __str__ method. If empty, prints a message."""
    if not employees:
        print("No employees to display.")
        return
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. {emp}")

def show_message(msg: str):
    """Prints a simple success or informational message."""
    print(msg)

def show_error(msg: str):
    """Prints an error message prefixed with 'Error: '."""
    print(f"Error: {msg}")

def prompt_is_manager() -> bool:
    """Asks if the employee is a manager and returns True or False."""
    ans = input("Is this a manager? (y/n): ").strip().lower()
    return ans == "y"

def prompt_new_employee() -> dict:
    """
    Prompts for new employee fields. If manager, also prompts for team_size.
    Returns a dict of raw input values.
    """
    data = {}
    data["id"] = input("ID: ")
    data["fname"] = input("First Name: ")
    data["lname"] = input("Last Name: ")
    data["department"] = input("Department (3 uppercase letters): ")
    data["phNumber"] = input("Phone Number (10 digits or formatted): ")
    if prompt_is_manager():
        data["role"] = "Manager"
        data["team_size"] = input("Team Size: ")
    else:
        data["role"] = "Employee"
    return data

def prompt_edit_employee(existing) -> dict:
    """
    Prompts for editing employee fields, showing current values.
    Enter keeps the old value. Returns a dict of possibly-updated values.
    """
    data = {}
    data["fname"] = input(f"First Name [{existing.fname}]: ") or existing.fname
    data["lname"] = input(f"Last Name [{existing.lname}]: ") or existing.lname
    data["department"] = input(f"Department [{existing.department}]: ") or existing.department
    data["phNumber"] = input(f"Phone Number [{existing.phNumber}]: ") or existing.getphNumber()
    if hasattr(existing, "team_size"):
        team_size = input(f"Team Size [{existing.team_size}]: ")
        data["team_size"] = team_size if team_size != "" else existing.team_size
    return data

def prompt_index(max_n: int) -> int:
    """
    Prompts for an employee number (1..max_n) and returns zero-based index.
    Raises ValueError if invalid.
    """
    val = input(f"Enter employee number (1-{max_n}): ").strip()
    if not val.isdigit():
        raise ValueError("Not a number.")
    idx = int(val) - 1
    if not (0 <= idx < max_n):
        raise ValueError("Number out of range.")
    return idx
