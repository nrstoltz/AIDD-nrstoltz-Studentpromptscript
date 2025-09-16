## Prompt 1
**User Prompt:**  
Write a Python class called Employee with attributes: id, fname, lname, department, and phNumber. Use private variables and getters/setters. Add validation: 
- First/last names cannot be empty or contain digits  
- Department must be exactly 3 uppercase letters  
- Phone number must be 10 digits  
Include docstrings.

**How well it worked:**  
Copilot generated the full Employee class with private attributes, getters, setters, validation rules, and docstrings. It also added a __str__ method, which was helpful. I only made a small edit so that id went through its setter instead of directly assigning _id, to stay consistent with best practices, and then in Step 2 I updated it to be read-only (no setter) per the new requirement. Otherwise, the output matched the expected outcome.



## Prompt 2
**User Prompt:**  
Update the Employee class so the employee ID is read-only after creation. Format phone numbers as (XXX)XXX-XXXX when accessed.

**How well it worked:**  
Copilot successfully removed the setter for `id`, making it read-only after creation, and formatted phone numbers in the getter while still storing them as digits. Both expected outcomes were met. I only had to fix a small issue where Copilot duplicated the `__str__` method at the bottom of the file. 



## Prompt 3
**User Prompt:**  
Write Python functions to load and save a list of Employee objects from a CSV file called employee_data.csv. The CSV columns should be id, fname, lname, department, phNumber.

**How well it worked:**  
Copilot generated both `load_employees()` and `save_employees()` functions. `load_employees()` correctly calls the Employee constructor for each row, handles missing files, and skips invalid rows. `save_employees()` writes a proper header row and saves the raw phone number digits. Imports were included automatically. No fixes were needed.



## Prompt 4
**User Prompt:**  
Write Python functions that:
- Add a new Employee to the list and save to CSV.
- Edit an existing Employee (but do not allow changing ID).
- Delete an Employee by index.
Include error handling.

**How well it worked:**  
Copilot generated `create_employee`, `edit_employee`, and `delete_employee` functions correctly. Each one enforces the rules, prevents ID changes, updates the CSV, and includes clear error handling. The code matched the expected outcome without requiring any manual fixes.




## Prompt 5
**User Prompt:**  
Write a Python function that prints a list of employees in the format:
1. ID - Last, First - Department - Phone

**How well it worked:**  
Copilot generated a correct `display_employees()` function. It prints employees in the required format with numbering, shows phone numbers formatted correctly, and handles the case of no employees. No fixes were needed.



## Prompt 6
**User Prompt:**  
Write a Python main loop that:
- Loads employees from CSV at startup
- Shows a menu with options: Add, Edit, Delete, List, Quit
- Calls the right function based on input
- Handles invalid input gracefully

**How well it worked:**  
Copilot generated EmployeeApp.py with a functional menu-driven CLI that used the business logic in employee.py. It loaded employees at startup, handled menu options correctly, and managed errors well. Copilot didn’t duplicate validation in the UI, and the only change I made was updating the phone prompt to show the formatted number while still keeping the raw digits as the default.  




## Prompt 7
**User Prompt:**  
Add test code to Employee class that tries valid and invalid data. Log errors to a file called employee_test.log.

**How well it worked:**  
Copilot added a __main__ test block to employee.py that creates a valid employee and intentionally triggers validation errors (empty first name, digits in last name, invalid department, short phone). Errors are written to employee_test.log with timestamps using Python’s logging module. No fixes were required beyond running the script; multiple runs append additional entries, as expected.





## Reflection Questions

1 •	What did AI get right away? What did it struggle with?

The AI got most of the main parts right away like setting up the Employee class with getters and setters, enforcing validation rules, CSV functions, CLI menu, etc.  It also added the test block at the bottom of employee.py that logged errors to employee_test.log without any issues. When I did run into errors, I noticed that giving it just the prompt to enter was usually close, but if I also gave it the expected outcome description from the assignment, it fixed the mistakes every time. That was super impressive to see because it showed me how much better the results were when I wrote a stronger, more detailed prompt that combined both pieces of information, and I feel like I learned how to guide AI with good prompts much better from this assignment.




2 •	How does separating business logic (Employee class) from UI logic (menu) help in real-world software?

Separating business logic from UI logic helps in real-world software because it makes the code cleaner, easier to test, and more reusable. I noticed this while working on the assignment because all the validation rules stayed in the Employee class, and the menu didn’t need to worry about them, it just called the functions. Keeping them separate also means the business logic can still be used if the interface changes, so if the menu was updated or replaced with something else, the rules would still work without me having to rewrite them.




3 •	What would change if we moved from CSV to a SQL database?

If we used a SQL database instead of a CSV, we would first have to edit the code to connect to the database, and then change the load and save functions so they work through SQL instead of reading and writing rows in a file. Using a database would also give the company a much more reliable and secure way to handle data storage, since databases are built to manage data integrity, scalability, and security in ways that a simple CSV file cannot.