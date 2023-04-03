# Task-Management-System
This is a simple task management system that allows users to register, login, add, and view tasks. The system stores user data and task data in text files.

## Getting Started

Clone the project to your local machine.
Open the whole folder for this task in VS Code otherwise the program will look in your root directory for the text files.
Use the following username and password to access the admin rights:
username: admin
password: password

## Functionality

### Login
This code reads usernames and passwords from the user.txt file to allow a user to login. If no user.txt file exists, the program writes one with a default admin account. After logging in, the user is prompted with the following options:


### Register new user
This option allows an admin user to register a new user by providing a unique username and password.

### Add task
This option allows an admin user to add a new task by providing the following details:

Username of the person to whom the task is assigned
Task title
Task description
Due date
Assigned date
View all tasks
This option allows an admin user to view all tasks that have been added to the system.

### View my tasks
This option allows a non-admin user to view all tasks that have been assigned to them.

### Generate reports
This option allows an admin user to generate reports. The user can choose to generate the following reports:

Number of tasks and number of completed tasks
Percentage of tasks that are incomplete
Percentage of tasks that are overdue
### Data Storage

User data is stored in user.txt.
Task data is stored in tasks.txt.

Contributors

Wissam Zendjebil





