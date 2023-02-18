#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime


#variables
reports_last_generated = False      #variable to force generate report to run if false


def menu_input(user):                                                   #function for menu input needs user
    menu = ""

    if user == "admin":
    
        menu = input('''
Select one of the following Options below:
r  - Registering a user         s  - View statistics
a  - Adding a task              gr - Generate reports
va - View all tasks             ds - Display statistics
vm - View my task               e  - Exit

Input: ''').lower()

    else:
        menu = input('''
Select one of the following Options below:
va - View all tasks             vm - View my task
e  - Exit

Input: ''').lower()

    return menu

def new_user(list_users):                                               #function for new user nees list_user to make sure no user is added twice
    '''In this block you will write code to add a new user to the user.txt file
    - You can follow the following steps:
        - Request input of a new username
        - Request input of a new password
        - Request input of password confirmation.
        - Check if the new password and confirmed password are the same.
        - If they are the same, add them to the user.txt file,
        - Otherwise you present a relevant message.'''

    #Variables
    new_user = ""
    new_password_1 = ""
    new_password_2 = ""

    new_user = input("Please enter a new user name: ")
    while list_users.count(new_user) > 0:                           #loop to stop multiple users with the same name
        new_user = input("Username taken, please enter a new user name: ")
    
    new_password_1 = input("Please enter a password: ")
    new_password_2 = input("Please re-enter your password: ")

    while new_password_1 != new_password_2:                         #loop to garentee matching passwords
        new_password_1 = input("Passwords dont match, please re-enter the password: ")
        new_password_2 = input("Please re-enter your password: ")

    with open("user.txt","a") as file_user:
        file_user.write(f"\n{new_user}, {new_password_1}")

    print("")                                                       #layout
    print(f"You have sucsessfully added a new user: {new_user} with password: {new_password_1}")
    list_users.append(new_user)

def add_new_task(list_users):                                           #function for adding new task nees list_user to make sure user exists
    '''In this block you will put code that will allow a user to add a new task to task.txt file
    - You can follow these steps:
        - Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.
        - Then get the current date.
        - Add the data to the file task.txt and
        - You must remember to include the 'No' to indicate if the task is complete.'''
    
    #variables
    asigned_to = ""
    task = ""
    task_description = ""
    date_asigned = ""
    date_due = ""
    task_complete = ""


    asigned_to = input("please enter the user you want to asign the task to: ")

    while list_users.count(asigned_to) != 1:                        #loop to make sure user exists
        asigned_to = input("Username does not exist, please enter one that does: ")

    task = input("What is the task? ")
    task_description = input("Please enter a task description: ")
    date_asigned = input("Please enter the date asigned (dd Mmm yyyy): ")
    date_due = input("Please enter the due date (dd Mmm yyyy): ")
    task_complete = input("Is the task complete? (Yes/No): ")

    with open("tasks.txt","a") as file_tasks:                       #opening tasks.txt
        file_tasks.write(f"\n{asigned_to}, {task}, {task_description}, {date_asigned}, {date_due}, {task_complete}")  #writing to tasks.text

    print("")
    print("You have added:")
    print("________________________________________________________________________________________________________________________")
    print("")                    
    print(f"Task:               {task}")                 #visualising data
    print(f"Asigned to:         {asigned_to}")
    print(f"Date assigned:      {date_asigned}")
    print(f"Due date:           {date_due}")
    print(f"Task Complete?      {task_complete}")
    print(f"Task description:   {task_description}")
    print("________________________________________________________________________________________________________________________")

def view_all_tasks():
    '''In this block you will put code so that the program will read the task from task.txt file and
    print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    You can do it in this way:
        - Read a line from the file.
        - Split that line where there is comma and space.
        - Then print the results in the format shown in the Output 2 
        - It is much easier to read a file using a for loop.'''
    
    print("________________________________________________________________________________________________________________________")

    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        for line in file_tasks:
            line = line.strip("\n")                                 #removing \n
            task = line.split(", ")                                 #spliting into list
            
            print("")                    
            print(f"Task:               {task[1]}")                 #visualising data
            print(f"Asigned to:         {task[0]}")
            print(f"Date assigned:      {task[3]}")
            print(f"Due date:           {task[4]}")
            print(f"Task Complete?      {task[5]}")
            print(f"Task description:   {task[2]}")
            print("________________________________________________________________________________________________________________________")    

def edit_data(user, task_number_to_change, paramiter_to_change, new_value):                               #function to edit data      
    
    #variables
    new_data = []
    
    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        for line in file_tasks:
            line = line.strip("\n")                                 #removing \n
            task = line.split(", ")                                 #spliting into list
            new_data.append(task)                                   #adding task list to new data list

    with open("tasks.txt","w") as file_tasks:                       #opening tasks.txt
        
        #variables
        add_new_line = False
        task_number = 0

        for task in new_data:
            
            if add_new_line == False:       #add new line except for at the begining and end
                add_new_line = True
            else:
                file_tasks.write("\n")

            if task[0] == user:
                task_number = task_number + 1

            if task[0] == user and task_number_to_change == task_number and paramiter_to_change == "user":     
                file_tasks.write(f"{new_value}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}")

            elif task[0] == user and task_number_to_change == task_number and paramiter_to_change == "completed":
                file_tasks.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {new_value}")

            elif task[0] == user and task_number_to_change == task_number and paramiter_to_change == "due_date":
                file_tasks.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {new_value}, {task[5]}")            

            else:
                file_tasks.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}")


#view my task functions
def view_all_my_tasks():                    #view all my tasks function
    '''In this block you will put code the that will read the task from task.txt file and
    print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    You can do it in this way:
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the username you have
        read from the file.
        - If they are the same print it in the format of Output 2 in the task PDF'''
    
    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        
        #Variables
        task_number = 1

        print("________________________________________________________________________________________________________________________")

        for line in file_tasks:
            line = line.strip("\n")                                 #removing \n
            task = line.split(", ")                                 #spliting into list
            
            if task[0] == user:
                print("")                                               #visualising data   
                print(f"Task {task_number}:             {task[1]}")     #Display all tasks in a manner that is easy to read. Make sure that each task is displayed with a corresponding number which can be used to identify the task.
                print(f"Asigned to:         {task[0]}")
                print(f"Date assigned:      {task[3]}")
                print(f"Due date:           {task[4]}")
                print(f"Task Complete?      {task[5]}")
                print(f"Task description:   {task[2]}")
                print("________________________________________________________________________________________________________________________")   

                task_number = task_number + 1

    return task_number      #used to return error if task that doesn't exist is selected

def view_selected_task(select_task):        #Selecting task

    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        
        #Variables
        task_number = 1

        print("________________________________________________________________________________________________________________________")

        for line in file_tasks:
            line = line.strip("\n")                                 #removing \n
            task = line.split(", ")                                 #spliting into list
            
            if task[0] == user:
                
                if select_task == task_number:
                    print("")                                               #visualising data   
                    print(f"Task {task_number}:             {task[1]}")     #Display all tasks in a manner that is easy to read. Make sure that each task is displayed with a corresponding number which can be used to identify the task.
                    print(f"Asigned to:         {task[0]}")
                    print(f"Date assigned:      {task[3]}")
                    print(f"Due date:           {task[4]}")
                    print(f"Task Complete?      {task[5]}")
                    print(f"Task description:   {task[2]}")
                    print("________________________________________________________________________________________________________________________") 

                    task_complete = task[5].lower()
                    return task_complete                #needed as completed tasks shouldn't be editable

                task_number = task_number + 1
            
def edit_task(select_task, list_users, user):

    #variables
    edit_task_menu_choice = ""
    new_user = ""
    new_due_date = ""


    while edit_task_menu_choice != "e":
        
        edit_task_menu_choice = input('''
Select one of the following Options below:
mc - Mark the task as complete
eu - Edit user asigned to task
ed - Edit due date
e  - Exit

Input: ''').lower()

        print("________________________________________________________________________________________________________________________")
        print("")       #layout

        if edit_task_menu_choice == "mc":
            print(f"Task {select_task} is marked as complete")
            edit_task_menu_choice = "e"     #need to return as you cant edit a completed task
            
            edit_data(user, select_task, "completed", "Yes")

        elif edit_task_menu_choice == "eu":
            new_user = input("Which user would you like asigned to this task: ")        #need to check if user exists

            while list_users.count(new_user) != 1:                        #loop to make sure user exists
                new_user = input("Username does not exist, please enter one that does: ")
            
            edit_data(user, select_task, "user", new_user)
            
            edit_task_menu_choice = "e"     #need to return as this user cant edit another users task

            view_my_tasks()                 #returning to start as tasks have dropped due to user changing
            

        elif edit_task_menu_choice == "ed":
            new_due_date = input("Please enter a new due date (dd Mmm yyyy): ")
            edit_data(user, select_task, "due_date", new_due_date)


        elif edit_task_menu_choice == "e":
            print("Exiting edit task")

        else:
            print("You have made a wrong choice, Please Try again")

        print("________________________________________________________________________________________________________________________")

def view_my_tasks():                        #view my tasks function

    #Variable 
    task_number = 0
    select_task = 0
    task_complete = ""

    task_number = view_all_my_tasks()            

    #select task loop
    while select_task >= 0:
        
        print("")       #layout

        select_task = int(input("Enter a task number to edit or -1 to go back: "))      #Allow the user to select either a specific task (by entering a number) or input ‘-1’ to return to the main menu.

        if select_task < task_number:
            task_complete = view_selected_task(select_task)
            if task_complete == "yes":      #needed as completed tasks shouldn't be editable
                print("")
                print("Task has been completed, you can not edit.")
                print("________________________________________________________________________________________________________________________")
            else:
                edit_task(select_task, list_users, user)

        else:
            print("________________________________________________________________________________________________________________________")
            print("")
            print("Task doesn't exist")
            print("________________________________________________________________________________________________________________________")


def view_statistics():
    #variables
    task_count = 0                                                  #count of tasks

    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        for line in file_tasks:
            task_count = task_count + 1

    print(f"""Statastics                    
------------------------------------------------------------------------------------------------------------------------
Number of users:    {len(list_users)}
Number of tasks:    {task_count}
------------------------------------------------------------------------------------------------------------------------""") #layout



#functions for generating reports
def generate_reports(list_users):
    
    reports_last_generated = datetime.now().strftime("%d %b %Y")     #working out the last time report was last generated
    
    print("")
    print("Generating reports...")
    print("")

    #task variables
    new_data = []
    task_count = 0                                                  #count of tasks
    incomplete_tasks = 0
    today = datetime.now()
    overdue = 0

    #user variables
    list_user_tasks_asigned = []
    list_user_tasks_complete = []
    list_user_tasks_overdue = []
    list_percentage_complete = []
    list_percentage_incomplete = []
    list_percentage_overdue = []
    

    for user in list_users:
        list_user_tasks_asigned.append(0)
        list_user_tasks_complete.append(0)
        list_user_tasks_overdue.append(0)

    with open("tasks.txt","r") as file_tasks:                       #opening tasks.txt
        for line in file_tasks:
            line = line.strip("\n")                                 #removing \n
            task = line.split(", ")                                 #spliting into list
            new_data.append(task)                                   #adding task list to new data list

            task_count = task_count + 1                             #counts number of tasks

            if task[5].lower() == "no":                             #counts incomplete tasks
                incomplete_tasks = incomplete_tasks +1
                
                date_time = datetime.strptime(task[4], "%d %b %Y")  #converting due date to date_time

                if today > date_time:
                    overdue = overdue + 1                           #counting overdue tasks

            for user in list_users:
                
                if task[0] == user:
                    list_user_tasks_asigned[list_users.index(user)] = list_user_tasks_asigned[list_users.index(user)] + 1     #adds 1 to list when user is mentioned in task
            
                if task[0] == user and task[5].lower() == "yes":
                    list_user_tasks_complete[list_users.index(user)] = list_user_tasks_complete[list_users.index(user)] + 1   #adds 1 to list when task is complete

                if task[0] == user and task[5].lower() == "no":
                    date_time = datetime.strptime(task[4], "%d %b %Y")  #converting due date to date_time
                    if today > date_time:
                        list_user_tasks_overdue[list_users.index(user)] = list_user_tasks_overdue[list_users.index(user)] + 1   #adds 1 to list when task is complete


    #task calculations
    completed_tasks = task_count - incomplete_tasks
    percentage_incomplete = incomplete_tasks / task_count * 100
    percentage_overdue_total = overdue / task_count * 100
    percentage_overdue_incomplete = overdue / incomplete_tasks * 100

    #user calculations
    
    for (user_tasks_asigned, user_tasks_complete, user_tasks_overdue) in zip(list_user_tasks_asigned, list_user_tasks_complete, list_user_tasks_overdue):    #list_percentage_complete & incomplete  #list_percentage_overdue
        if user_tasks_asigned == 0:
            list_percentage_complete.append("-")
            list_percentage_incomplete.append("-")
            list_percentage_overdue.append("-")

#        elif user_tasks_asigned - user_tasks_complete == 0:
#            list_percentage_overdue.append("-")

        else:
            percentage_complete = user_tasks_complete / user_tasks_asigned * 100
            list_percentage_complete.append(percentage_complete)
            
            percentage_incomplete = 100 - percentage_complete
            list_percentage_incomplete.append(percentage_incomplete)

            if user_tasks_asigned - user_tasks_complete == 0:           #divide by 0 error
                list_percentage_overdue.append(0)
            else:
                percent_overdue = user_tasks_overdue / (user_tasks_asigned - user_tasks_complete) * 100
                list_percentage_overdue.append(percent_overdue)
    


    blurb = (f"""Task Overview                    
------------------------------------------------------------------------------------------------------------------------
Number of tasks:                        {task_count}
Number of completed tasks:              {completed_tasks}
Number of uncomplete tasks:             {incomplete_tasks}
Number of overdue tasks:                {overdue}
Percentage of incomplete tasks:         {percentage_incomplete:.1f} %
Percentage of all tasks overdue:        {percentage_overdue_total:.1f} %
Percentage of incomplete tasks overdue: {percentage_overdue_incomplete:.1f} %
------------------------------------------------------------------------------------------------------------------------""") #layout

    print(blurb)
    print("")

    with open("task_overview.txt","w") as task_overview:                       #opening task_overview.txt
        task_overview.write(blurb)

    #User overview
    user_blurb = f"""User Overview                    
------------------------------------------------------------------------------------------------------------------------
Number of users:    {len(list_users)}
Number tasks:       {task_count}
------------------------------------------------------------------------------------------------------------------------

{"User":<20}{"Tasks":<20}{"Percentage Total":<20}{"Percentage":<20}{"Percentage":<20}{"Percentage Incomplete":<20}
{"":<20}{"Asigned":<20}{"Tasks Asigned (%)":<20}{"Completed (%)":<20}{"Incomplete (%)":<20}{"Overdue (%)":<20}
------------------------------------------------------------------------------------------------------------------------""" #layout
    
    for (user, user_tasks_asigned, user_tasks_complete, percentage_complete, percentage_incomplete, percentage_overdue) in zip(list_users, list_user_tasks_asigned, list_user_tasks_complete, list_percentage_complete, list_percentage_incomplete, list_percentage_overdue):
        user_blurb = user_blurb + f"""
{user:<20}{user_tasks_asigned:<20}{user_tasks_asigned/task_count*100:<20}{percentage_complete:<20}{percentage_incomplete:<20}{percentage_overdue:<20}"""
    user_blurb = user_blurb + """
------------------------------------------------------------------------------------------------------------------------"""

    print(user_blurb)

    with open("user_overview.txt","w") as user_overview:                       #opening task_overview.txt
        user_overview.write(user_blurb)




    return reports_last_generated       #needs to return reports_last_generated for display statistics to work




def display_statistics(reports_last_generated):

    if reports_last_generated == False:
        print("")
        print("Reports not generated.")
        reports_last_generated = generate_reports(list_users)
    
    else:
        print(f"Report last generated: {reports_last_generated}")

    return reports_last_generated



#Variables for logged in loop
logged_in = False

while logged_in == False:                                               #login loop
    #====Login Section====
    '''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
    '''

    #variables
    list_users = []
    list_passwords = []
    contents = ""
    user = ""
    password = ""

    #getting user & password data from file
    with open("user.txt","r") as file_user:                     #opening user.txt into a string
            for line in file_user:
                contents = contents + line

    contents = contents.split("\n")                             #splitting file user into list containing user, password

    for item in contents:
        item = item.split(", ")                                 #splitting user into user password
        list_users.append(str(item[0]))                         #Adding user to list_users
        list_passwords.append(str(item[1]))                     #Adding password to list_passwords

    #print(list_users)  #for error checking
    #print(list_passwords)  #for error checking
    
    print("")                                                   #layout
    
    #logging in
    user = input("Please enter your user name: ")

    while list_users.count(user) == 0:                          #loop for entering a user on the user_list
        user = input("User name doesn't exist, please enter your user name: ")

    #print(user)    #for error checking

    index_user = list_users.index(user)                         #need users index to check password
    #print(index_user)    #for error checking

    password = input("Please enter your user password: ")

    while password != list_passwords[index_user]:               #loop for entering correct password
        password = input("Password not correct, please enter your password: ")

    #print(password)  #for error checking
    
    logged_in = True

while True:                                 #main menu loop
#presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
    
    menu = menu_input(user)

    if menu == 'r' and user == "admin":                                 #add new user #admin only
        new_user(list_users)

    elif menu == 'a':                                                   #add new task
        add_new_task(list_users)

    elif menu == 'va':                                                  #view all tasks
        view_all_tasks()

    elif menu == 'vm':                                                  #view my tasks
        view_my_tasks()

    elif menu == "s" and user == "admin":                               #view statistics
        view_statistics()

    elif menu == "gr" and user == "admin":                              #generate reports
        reports_last_generated = generate_reports()

    elif menu == "ds" and user == "admin":                              #display statistics
        reports_last_generated = display_statistics(reports_last_generated)

    elif menu == 'e':                                                   #quit
        print("")
        print('Goodbye!!!')
        print("")                                                       #layout
        exit()

    else:                                                               #wrong choice
        print("You have made a wrong choice, Please Try again")