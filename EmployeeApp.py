from employee import Employee, Manager
from EmployeeData import load_employees, save_employees
import EmployeeView as view

def main():
    employees = load_employees()

    while True:
        try:
            choice = view.show_menu()

            if choice == "1":
                # List
                view.show_employees(employees)

            elif choice == "2":
                # Add
                data = view.prompt_new_employee()
                if data.get("role") == "Manager":
                    emp = Manager(
                        id=data["id"],
                        fname=data["fname"],
                        lname=data["lname"],
                        department=data["department"],
                        phNumber=data["phNumber"],
                        team_size=int(data.get("team_size", 0)),
                    )
                else:
                    emp = Employee(
                        id=data["id"],
                        fname=data["fname"],
                        lname=data["lname"],
                        department=data["department"],
                        phNumber=data["phNumber"],
                    )
                employees.append(emp)
                save_employees(employees)
                view.show_message("Employee added.")

            elif choice == "3":
                # Edit
                if not employees:
                    view.show_message("No employees to edit.")
                    continue
                view.show_employees(employees)
                idx = view.prompt_index(len(employees))
                emp = employees[idx]
                data = view.prompt_edit_employee(emp)

                # Apply edits (business rules are enforced by model setters)
                emp.fname = data["fname"]
                emp.lname = data["lname"]
                emp.department = data["department"]
                emp.phNumber = data["phNumber"]
                if isinstance(emp, Manager) and "team_size" in data:
                    emp.team_size = int(data["team_size"])

                save_employees(employees)
                view.show_message("Employee updated.")

            elif choice == "4":
                # Delete
                if not employees:
                    view.show_message("No employees to delete.")
                    continue
                view.show_employees(employees)
                idx = view.prompt_index(len(employees))
                employees.pop(idx)
                save_employees(employees)
                view.show_message("Employee deleted.")

            elif choice == "5":
                view.show_message("Goodbye!")
                break

            else:
                view.show_error("Invalid option. Please enter a number from 1 to 5.")

        except Exception as e:
            # Any model validation or bad input surfaces here
            view.show_error(str(e))

if __name__ == "__main__":
    main()
