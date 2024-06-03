TodoApp README
Overview
TodoApp is a simple to-do list application built using Python's Tkinter library. It allows users to add, delete, mark tasks as completed, and consult the status of tasks.

Features
Add Task: Users can add a new task to the list.
Delete Task: Users can delete a selected task from the list.
Mark Task as Completed: Users can mark a selected task as completed.
Consult Task: Users can view the details and status of a selected task.
Installation
To run this application, you need to have Python installed on your system. This application uses the Tkinter library, which comes pre-installed with Python.

Usage
Clone or Download the Repository:

Clone the repository using git clone <repository-url> or download the zip file from the repository and extract it.
Navigate to the Directory:

bash
Copiar código
cd path-to-directory
Run the Application:

bash
Copiar código
python todo_app.py
Code Structure
Classes and Methods
TodoApp
__init__(self, root): Initializes the application, sets up the UI components, and defines the main structure.
add_task(self): Adds a new task to the list.
delete_task(self): Deletes the selected task from the list.
mark_completed(self): Marks the selected task as completed.
consult_task(self): Shows information about the selected task in a message box.
update_task_listbox(self): Updates the Listbox with the current tasks and their status.
UI Components
Task Entry: An entry widget for typing new tasks.
Add Task Button: A button to add a task to the list.
Task Listbox: A Listbox to display tasks.
Delete Task Button: A button to delete the selected task.
Mark Completed Button: A button to mark the selected task as completed.
Consult Task Button: A button to consult the selected task's details.
Example
Here's an example of how to initialize and run the application:

python
Copiar código
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
Contributing
If you want to contribute to this project, feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.

Contact
If you have any questions or suggestions, please open an issue in the repository.

This README provides an overview of the TodoApp application, how to install and run it, a brief explanation of the code structure, and instructions for contributing to the project.
