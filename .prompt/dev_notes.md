Assignment 3 – Prompt Log


Prompt 1 (Part 1 – Employee & Manager Classes)

User Prompt:
Write a Python class called Employee with attributes: id, fname, lname, department, and phNumber. Use private variables and getters/setters. Add validation. Add a Manager subclass with team_size.

How well it worked:
Copilot generated the Employee class with validation and docstrings, and created a Manager subclass with a team_size attribute. It correctly used inheritance, but I had to guide it to validate team_size as a non-negative integer.

Follow-up Prompt:
Update the Manager subclass so that team_size must be a non-negative integer, raising ValueError if not.
This fixed an early bug where Copilot allowed negative numbers without complaint.

Prompt 2 (Part 2 – Persistence Layer)

User Prompt:
Write Python functions in a new file EmployeeData.py to load and save employees and managers to a CSV file, including role and team_size.

How well it worked:
Copilot generated EmployeeData.py with headers, role detection, and team_size handling. It wrote “Manager” or “Employee” to the role column. It worked overall, but I had to fix the case where team_size was blank because it initially crashed on empty strings.

Follow-up Prompt:
Change the load_employees function so that if team_size is blank, it defaults to 0 instead of throwing an error.
This solved the problem and let the CSV load correctly even if the column was empty.

Prompt 3 (Part 3 – View Layer)

User Prompt:
Write Python functions in EmployeeView.py to handle menu display, user prompts for adding or editing employees, showing messages, and handling errors.

How well it worked:
Copilot created functions for show_menu, show_employees, prompt_new_employee, prompt_edit_employee, and helpers for showing messages and errors. It also asked if an employee was a manager and prompted for team_size. The only issue was that prompt_edit_employee used the private variable _phNumber.

Follow-up Prompt:
Update prompt_edit_employee so it shows the formatted phone number by default, but still stores the raw digits if Enter is pressed.
This made the UI cleaner and avoided exposing private variables.

Prompt 4 (Part 4 – Controller Layer)

User Prompt:
Write Python controller file EmployeeApp.py that ties together EmployeeData, EmployeeView, and the Employee classes. The app should load employees at startup, show the menu, route input to the right function, and save changes.

How well it worked:
Copilot generated a working CLI loop that called into the Model and View correctly. It handled Add, Edit, Delete, List, and Quit as required. However, it duplicated some code at the bottom, leaving stray print and break lines that caused an IndentationError.

Follow-up Prompt:
Clean up the EmployeeApp.py loop to remove duplicated code and indentation errors. Ensure “Goodbye!” only prints once when quitting.
After this, the loop ran smoothly.

Prompt 5 (Part 5 – Testing & Demonstration)

User Prompt:
Expand the validation tests at the bottom of employee.py to include more invalid employee cases and more manager tests.

How well it worked:
Copilot added a larger test block with valid and invalid employees and managers. It logged errors to employee_test.log with timestamps. I only had to tweak logging so that results append instead of overwriting.

Follow-up Prompt:
Update the logging configuration so that logs append instead of overwrite by adding filemode="a".
This ensured each run added to the log instead of replacing it.




Part 6 – AI Reflection

Dear HR Management Team,

I wanted to write back to you with my main insights from using AI tools to assist in my completion of the prototype Employee Management System, specifically one using MVC architecture. Below I have summarized what I learned while working with AI and what it means for whether these tools are a good fit for future software projects.

AI generated many of the key parts of the system correctly. It built the Employee and Manager classes with validation rules, handled CSV persistence with load and save functions, and created the CLI menu that tied everything together. It even produced useful test blocks that validated both correct and incorrect input and logged errors to a file. Where AI struggled was in small but meaningful details. For example, it sometimes tried to expose private variables directly in the UI, produced duplicated or misplaced code (like an extra str method or indentation errors in the menu loop), and required guidance to properly enforce new attributes such as a manager’s team_size. Each time I encountered these issues, providing the prompt along with the expected outcome description from the assignment document fixed the mistakes. This showed me that success depended on carefully guiding the AI with detailed prompts rather than assuming its first answer would be perfect.

I am sure you are all fascinated and knowledgeable about the specifics of MVC architecture, so here are some technical details I noticed while using AI. The code separation was handled well across the four files: employee.py contained the business logic and validation, EmployeeData.py managed CSV storage, EmployeeView.py handled the user prompts and output, and EmployeeApp.py tied it all together as the controller. The main problems I had to fix were when AI blurred these boundaries, such as showing raw phone number digits in the UI or letting validation slip out of the Employee class. Correcting those points made the MVC architecture much cleaner and highlighted how AI can follow structure but still needs supervision to enforce design principles.

Compared to writing this program manually, AI clearly saved time. I estimate that about 65–70 percent of the boilerplate code (class structure, CRUD functions, CSV handling, menu scaffolding) was generated automatically. My main effort went into checking validation logic, adjusting inheritance, and making sure the modules fit the MVC model. If I had built this all from scratch, it would have taken significantly longer. Using AI shifted my role toward oversight, testing, and refining rather than typing out every line. Thinking ahead, if we used a more agentic AI that could complete the assignment directly from the specification, the nature of programming would change even further, with developers acting more like reviewers, framers, and testers of AI work than traditional coders.

AI showed some struggles with object-oriented programming concepts like inheritance and polymorphism. The Manager subclass worked, but at first the team_size attribute was not validated correctly, and the str method needed adjustments to extend the Employee version cleanly. I fixed these issues by tightening the setter logic and making sure polymorphic behavior (Employee vs. Manager) was consistently respected across data saving, loading, and displaying. These fixes were small but important, and they showed that AI handles general structures well but still falters on nuanced OOP rules.

From a business perspective, the return on investment was strongest in cutting down time spent on repetitive structures and boilerplate code. This freed me to focus on testing edge cases and ensuring compliance with the HR department’s strict data rules. The risks are worth noting. Small AI mistakes could lead to data integrity issues if not caught, and over-reliance on AI could reduce the development of junior programmers’ skills in fundamentals. There are also potential hidden costs around code quality and security, since AI does not always default to the most secure or maintainable approach.

Overall, AI provided strong value in helping build this prototype quickly and professionally. It let me deliver a working Employee Management System that enforces strict data rules, fits the MVC model, and avoids many of the problems the old spreadsheet-based system caused. Based on this experience, I would recommend that AI be used as a supportive tool in future HR software projects, as long as its outputs are paired with strong human oversight to ensure quality and reliability.
