from employee import (
    load_employees, save_employees, create_employee,
    edit_employee, delete_employee, display_employees
)

def prompt_employee_fields(existing=None):
    """
    Prompts user for employee fields. If 'existing' is provided, shows current values.
    Returns a tuple: (id, fname, lname, department, phNumber)
    """
    if existing:
        print(f"Leave blank to keep current value.")
        fname = input(f"First Name [{existing.fname}]: ") or existing.fname
        lname = input(f"Last Name [{existing.lname}]: ") or existing.lname
        department = input(f"Department [{existing.department}]: ") or existing.department
        phNumber = input(f"Phone Number [{existing.phNumber}]: ") or existing._phNumber
        return (existing.id, fname, lname, department, phNumber)
    else:
        id = input("ID: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        department = input("Department (3 uppercase letters): ")
        phNumber = input("Phone Number (10 digits): ")
        return (id, fname, lname, department, phNumber)

def main():
    employees = load_employees()
    while True:
        print("\nEmployee Management Menu")
        print("1. List Employees")
        print("2. Add Employee")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Quit")
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            try:
                id, fname, lname, department, phNumber = prompt_employee_fields()
                create_employee(employees, id, fname, lname, department, phNumber)
                print("Employee added.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            display_employees(employees)
            try:
                idx = int(input("Enter employee number to edit: ")) - 1
                if not (0 <= idx < len(employees)):
                    print("Invalid employee number.")
                    continue
                _, fname, lname, department, phNumber = prompt_employee_fields(employees[idx])
                edit_employee(employees, idx, fname, lname, department, phNumber)
                print("Employee updated.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            display_employees(employees)
            try:
                idx = int(input("Enter employee number to delete: ")) - 1
                delete_employee(employees, idx)
                print("Employee deleted.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
