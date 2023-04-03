# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


#fuction to register user
def reg_user():
    new_username = input("New Username: ")
    if new_username in username_password: #if user is already registered then the error message is displayed
            print("Username already exisits")
            reg_user() #ask for new username by calling the function again 
    else:    
        new_password = input("New Password: ")
    
            # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")
    
        if new_username in username_password:
            print("Username already exisits")
        else:
            if new_password == confirm_password:
            
                username_password[new_username] = new_password
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                        out_file.write("\n".join(user_data))
        
            else:
                    print("Passwords do no match")



#function to add task
def add_task(task_list):
    
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        


#Function to view all the tasks
def view_all(task_list):
    #iterate through the list of tasks
    for t in task_list: 
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
   

def view_mine(task_list):
    for idx, t in enumerate(task_list,start=1): #use enumerate to index each task
           if t['username'] == curr_user:
                disp_str = f"Task Number: {idx}\n" 
                #print(f"Task Number: {idx}")
                disp_str += f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
    option = int(input("Please select either a specific task  or input ‘-1’ to return to the main menu."))
    if option  == -1:
        pass #return to main menu
    else:
        make_change(option,task_list)
   

#Function called to make changed to chosen task         
def make_change(option,task_list):
    chosen_task = task_list[option-1]
    complete = input("Do you want to mark the task as complete? (Y/N): ")
    try:
        if complete == "Y":
            chosen_task['completed'] = "Yes" 
            task_data[option-1] = chosen_task
            add_task(task_list) #call add_task function to update the task in the task file
        elif complete == "N" and chosen_task['completed'] == False: #only edit a task if it is not yet completedß
            user_edit = input("Do you want to edit the username of the person to whom the task is assigned: ?")
            if user_edit == "Y" :
                new_user = input("Enter the new username: ")
                chosen_task['username'] = new_user #update the user to which the task is assinged to
                task_data[option-1] = chosen_task
                add_task(task_list)
            if user_edit == "N":
                while True: 
                    try: #use try & except to ensure the date is in the correct format
                        new_date = input("Enter the new due date of task (YYYY-MM-DD): ")
                        new_date_time = datetime.strptime(new_date, DATETIME_STRING_FORMAT)
                        chosen_task['due_date'] = new_date_time 
                        task_data[option-1] = chosen_task
                        add_task(task_list)
                        break
            
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
    
        else:
            print("You can't edit a completed task")
    except ValueError:
            print("Invalid input")



def task_report(task_data,task_overview):
    d = datetime.today()
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    total_tasks = 0
    for i in task_data:
        if i['completed'] == True:
            completed_tasks += 1
        elif i['completed'] == False and i['due_date'] > d:
                overdue_tasks += 1
                uncompleted_tasks += 1
        elif i['completed'] == False:
                uncompleted_tasks += 1
        total_tasks += 1
    percentage_incomplete =round((uncompleted_tasks/total_tasks) * 100,2)
    
    percentage_overdue = round((overdue_tasks/total_tasks) * 100,2)
    
    disp_rpt = f"The total number of completed tasks: \t {completed_tasks}\n"
    disp_rpt += f"The total number of uncompleted tasks: \t {uncompleted_tasks}\n"
    disp_rpt += f"The total number of tasks that haven’t been completed and that are overdue: \t {overdue_tasks}\n"
    disp_rpt += f"The percentage of tasks that are incomplete: \t {percentage_incomplete}\n"
    disp_rpt += f"The percentage of tasks that are overdue: \n {percentage_overdue}\n"
    print(disp_rpt)
    task_overview.write(disp_rpt)
    task_overview.close()

def user_report(task_data,username_password,user_overview):
    total_users = len(username_password.keys())
    total_task = len(task_data)
    totals = f"The total number of users registered with task_manager.py: \t {total_users}\n"
    totals += f"The total number of tasks that have been generated and tracked using task_manager.py: \t {total_task}\n"
    user_overview.write(totals)    
    
    
    user_complete = 0
    user_incomplete = 0
    user_overdue = 0
    user_task = 0
    for key in username_password:
        for j in task_data:
            if j['username'] == key and j['completed'] == True:
                user_task += 1
                user_complete += 1
            elif j['username'] == key and j['completed'] == False:
                    if j['due_date'] > datetime.today():
                        user_task += 1
                        user_overdue += 1
                    else:
                        user_incomplete += 1
            
        percentage_assigned = round((user_task/total_task) * 100,2)
        percentage_complete =round((user_complete/user_task) * 100,2)
        percentage_incomplete =round((user_incomplete/user_task) * 100,2)
        percentage_overdue = round((user_overdue/user_task) * 100,2)
        
        disp_rpt = f"\n\t \t{key}:\n"
        disp_rpt += f"The total number of tasks assigned to {key}: \t {user_task}\n"
        disp_rpt += f"The percentage of the total number of tasks that havebeen assigned to {key}: \t {percentage_assigned}\n"
        disp_rpt += f"The percentage of the tasks assigned to {key} thathave been completed: \t {percentage_complete}\n"
        disp_rpt += f"The percentage of the tasks assigned to {key} that must still be completed: \t {percentage_incomplete}\n"
        disp_rpt += f"The percentage of tasks assigned to {key} that are incomplete: \t {percentage_incomplete}\n"
        disp_rpt += f"The percentage of the tasks assigned to {key} that are overdue: \t {percentage_overdue}\n"
   
        user_overview.write(disp_rpt)
    user_overview.close()


     
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    if curr_user == "admin":
        menu = str(input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - Display statistics
e - Exit
: ''')).lower()
    else:
        menu = str(input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''')).lower()
    if menu == 'r':
        reg_user()

        # - Request input of a new password
        
    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username in username_password.keys():
            
            
            #continue
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break
        
                except ValueError:
                    print("Invalid datetime format. Please use the format specified")
        
    
            # Then get the current date.
            curr_date = date.today()
            ''' Add the data to the file task.txt and
                Include 'No' to indicate if the task is complete.'''
            new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": False
            }
    
            task_list.append(new_task)
            
            add_task(task_list)
            print("Task successfully added.")
        else:
            print("User does not exist. Please enter a valid username") 
            pass #return to main menu if user does not exist

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        view_all(task_list)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine(task_list)
    
    elif menu == 'gr' and curr_user == 'admin': 
        task_overview = open('task_overview.txt', 'w')
        user_overview = open('user_overview.txt', 'w')
        task_report(task_list,task_overview)
        user_report(task_list,username_password,user_overview)
   
        
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)
        
        if not os.path.exists("task_overview.txt"):
            with open("task_overview.txt", "a+") as task_overview:
                task_report(task_list,task_overview)
      
        with open("task_overview.txt", "r") as file1:
            content = file1.readlines()
            for line in content:
                print(line)
                
        if not os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "a+") as user_overview:
                user_report(task_list,username_password,user_overview)
               
        with open("user_overview.txt", "r") as file2:
            content = file2.readlines()
            for line in content:
                print(line)
    


    
       # print("-----------------------------------")
       # print(f"Number of users: \t\t {num_users}")
       # print(f"Number of tasks: \t\t {num_tasks}")
       # print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
        
        
        
        
        

        
        
        