# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.
#%%
#=====importing libraries===========
import os
import datetime

#Functions:
    
#Function 1: Registers a new user and adds it to the user.txt file, making sure not to allow duplicate users.
def reg_user():
    new_username = (input("New Username:  \n"))
    while new_username in list_user:
        print ("Username already registered: ")
        new_username = (input("New Username:  \n"))
    
    if new_username not in list_user:
        list_user.append(new_username)
    
    new_password = ("New Password:  \n" )
    confirm_password = ("Confirm Your Password:  \n")

    while new_password == confirm_password:
        print("New user added!")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:
          user_data = []
          for k in username_password:
           user_data.append(f"{k};{username_password[k]}")
           out_file.write("\n".join(user_data))
    else:
     print("Passwords do not match!")

#Function 2: Adds a new task to the task.txt file, asks the user for several inputs then adds them to the file. 
def add_task ():
  open_file = open("tasks.txt", "a+")

  curr_date = datetime.date.today()
  task_username = input("Name of person assigned to task: ")
  task_title = input("Title of Task: ")
  task_description = input("Description of Task: ")
  due_date_time  = input("Due date: (DD MM YYYY) ") 
  completed = input("Is the task completed: (Yes/No)").lower()

  open_file.write(f"\n {task_username}, {task_title}, {task_description}, {curr_date}, {due_date_time}, {completed}")
  open_file.close()
  print("Task added.")

#Function 3: Displays all tasks in the tasks.txt file, in a user friendly manner
def view_all():
    with open("tasks.txt", "r+") as read_file:
        data = read_file.readlines()

        for x, task in enumerate(data):
         split_data = task.split(", ")

        dis_str = f"_______________________________________\n"
        dis_str += "\n"
        dis_str += f"Task Number: ----- {x}\n"
        dis_str += f"Task: ------------ {split_data[1]}\n"
        dis_str += f"Assigned to: ----- {split_data[0]}\n"
        dis_str += f"Date Assigned: --- {split_data[3]}\n"
        dis_str += f"Date Due: -------- {split_data[4]}\n"
        dis_str += f"Task Description - {split_data[2]}"
        dis_str += "\n"
        dis_str += f"______________________________________ \n"
        print(dis_str)
        


#Function 4: Displays only the tasks assinged to the user logged in
def view_mine():
    with open("tasks.txt", "r") as mine_file:
     data = mine_file.readlines()

    for x, task in enumerate(data):
       split_data = task.split(", ")
       if curr_user in split_data[0]:   
        dis_str = f"_______________________________________\n"
        dis_str += "\n"
        dis_str += f"Task Number: ----- {x+1}\n"
        dis_str += f"Task: ------------ {split_data[1]}\n"
        dis_str += f"Assigned to: ----- {split_data[0]}\n"
        dis_str += f"Date Assigned: --- {split_data[3]}\n"
        dis_str += f"Date Due: -------- {split_data[4]}\n"
        dis_str += f"Task Description - {split_data[2]}"
        dis_str += "\n"
        dis_str += f"______________________________________ \n"
        print(dis_str)

#This function also allows the user to edit and update a task, changing who the task is assigned to, and the due date. 
    while True: 
        vm_choice = int(input("Please enter the number of the task you would to edit:  (Type -1 to return to main menu)"))

        if 0 <= vm_choice < len(data):
          new_data = data[vm_choice]

          dis_str = print("1:\tMark the task as complete")
          dis_str = print("2:\tEdit the task")

          edit_choice = int(input("How would you like to edit the task?: "))

        if edit_choice == 1:
             split_data = new_data.split()
             split_data[5] == "yes"

             tasks = open('tasks.txt', 'w')
             for task in data:
              tasks.write(task)

             tasks.close()
             break
                     
            
        elif edit_choice == 2:
               if split_data[5] == ("no"):
                  new_username = ("Please type the new username assigned to this task: ")
                  split_data[0] = new_username

                  new_due_date = ("Enter new due date: dd mm yy")
                  split_data[4] = new_due_date

                  data[vm_choice] = new_data

                  tasks = open('tasks.txt', 'w')
                  for task in data:
                   tasks.write(task)

                  tasks.close()
                  break
         
               else:
                print ("Unable to edit completed task.")
         
        elif vm_choice <= 0 or vm_choice >=3:
         print("Invalid choice. ")
         continue

    
        elif vm_choice == -1:
         print("Returning you to main menu. ")
         break
 
    mine_file.close()
    print("Task updated!")

#Function 5: Creates the task_overview and user_overview.txt files, displaying statistics of the assigned tasks. 
        
reports_dict = {}

def generate_reports():

#Generating the task_overview.txt file. 
    report_stats = ""
    rep_compl = (0)
    rep_uncompl = (0)
    rep_overd = (0)
    rep_total = len(reports_dict)
 
    for comp in reports_dict:
       if reports_dict[comp][5] == "yes":
        rep_compl += 1

       elif reports_dict[comp][5] == "no":
        rep_uncompl += 1
        print(f"Due date: {reports_dict[comp][4]}")
        rep_ov_check = input("Has the due date passed? (y/n)").lower()
        if rep_ov_check == 'y':
           rep_overd += 1
        else:
           print("Task not yet overdue")
           continue

    report_stats =  f"_______________________________________\n"
    report_stats = "\n"
    report_stats += f"Tasks generated: ------ {rep_total}"
    report_stats += f"Tasks completed: ------ {rep_compl}"
    report_stats += f"Tasks uncompleted: ---- {rep_uncompl}"
    report_stats += f"Tasks overdue: -------- {rep_overd}"
    report_stats += f"Incomplete tasks: ----- {round(rep_uncompl/rep_total)*100, 2}%"
    report_stats += f"Overdue tasks: -------- {round(rep_overd/rep_total)*100, 2}%"
    report_stats = "\n"
    report_stats =  f"_______________________________________\n"

    with open('task overview.txt', 'w') as task_ov_w:
     task_ov_w.write(report_stats)


#Generating the user_overview.txt file. 
    total_user = len(list_user)
    use_ov_w = open('user overview.txt', 'w')

    use_ov = f"___________________________________________ \n"
    use_ov += f"\n"
    use_ov += f"Users registered: -------- {total_user}"
    use_ov += f"Tasks generated/tracked: - {rep_total}\n"

    total_rep_user = (0)
    u_rep_compl = (0)
    u_rep_uncompl = (0)
    u_rep_overd = (0)

    for u in list_user:
     if reports_dict[comp][0] == u:
      total_rep_user += 1
   
     elif reports_dict[comp][0] == u and reports_dict[comp][5]== 'yes':
      u_rep_compl += 1

     elif reports_dict[comp][0] == u and reports_dict[comp][5]== 'no':
      u_rep_uncompl += 1

      print(f"Due date: {reports_dict[comp][4]}")
      u_ov_check = input("Has the due date passed? (y/n)").lower()
      if u_ov_check == 'y':
        u_rep_overd += 1
      elif u_ov_check == 'n':
        print("Task not yet overdue")
        continue
      else:
         print("Incorrect input")
         u_ov_check = input("Has the due date passed? (y/n)").lower()

    use_ov =  f"________________________________________________\n"
    use_ov += "\n"
    use_ov += f"Username: -------------------------- {user}"
    use_ov += f"No. of tasks assigned: ------------- {total_rep_user}"
    use_ov += f"Percentage of total tasks: --------- {round((total_rep_user/rep_total) * 100, 2)}%"
    use_ov += f"Percentage of completed tasks: ----- {round((u_rep_compl/total_rep_user) * 100, 2)}%"
    use_ov += f"Percentage of uncompleted tasks: --- {round((u_rep_uncompl/total_rep_user) * 100, 2)}%"
    use_ov += f"Percentage of overdue tasks: ------- {round((u_rep_overd/total_rep_user) * 100, 2)}%\n"
    use_ov += "\n"
    use_ov =  f"________________________________________________\n"

    use_ov_w.write()
    use_ov_w.close()
    print("Reports generated. ")


#Function 6: This displays the generated reports in the console, instead of as a .txt file. 
def display_statistics():
   with open("task_overview.txt", 'r') as task_read:
      read_file = task_read.readlines()
      print("Task overview:\n")

      for x in read_file:
         print(x)
    
         print ("User overview:\n")

    
   with open("user_overview.txt", 'r') as user_read:
      read_file1 = user_read.readlines()
      for y in read_file1:
         print(y) 
    
print("\n")

      
#====Login Section====
#Empty dictionary, and two lists. These will be handy later when generating reports. 
user_info = {}
list_user = []
list_pass = []

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
        list_user.append(curr_user)
        list_pass.append(curr_pass)
        user_info["Usernames"] = list_user
        user_info["Password"] = list_pass

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if curr_user == "admin":
     menu = input('''Select one of the following Options below:\n
R: ----- Registering a user
A: ----- Adding a task
VA: ---- View all tasks
VM: ---- View my task
GR: ---- Generate reports
DS: ---- Display statistics
E: ----- Exit\n
: ''').lower()
    else:
       menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
       
    if menu == 'r':
       reg_user()

    elif menu == 'a':
       add_task()

    elif menu == 'va':
       view_all()

    elif menu == 'vm':
       view_mine()

    elif menu == 'gr':
       generate_reports()

    elif menu == 'ds':
       while True:
            try: 
             file = open('user_overview.txt', 'r')
             display_statistics()
             file.close()
             break
            except FileExistsError as error:
                print("\nFile does not exist")
                generate_reports()

    elif menu == 'e':
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please Try again")
# %%
