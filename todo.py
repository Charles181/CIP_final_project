from datetime import datetime

date = datetime.now()
currentTime = date.strftime("%d/%m/%Y %H:%M")

valid_options = {
    1: "View your list",
    2: "Add an activity",
    3: "Mark activity as complete",
    4: "Delete an activity",
    5: "Save and exit"
    }

todo_list = {}

def display_todo_list(todo_list,text):
    print(f"{text}")
    print("-" * 40)
    for activity, status in todo_list.items():
        print(f"| {activity}: {status}")
    print("-" * 40)

def main_menu():
    print("Welcome to your To-Do list ")
    print("Current time is", currentTime)
    print("Please select an option: ")
    print("")
    for key,value in valid_options.items():
        print(f"{key}) {value}")

def get_valid_option():
    """Asks user for an option, if the option is valid, return given value.
    except ValueError handles the case when user inputs an empty string, which would terminate the program and return a ValueError Traceback
    """

    try:
        option = int(input("Please enter an option: "))
        if option in valid_options:
            print("")
            print(f"You selected option {option}: {valid_options[option]}")
            return option
        else:
            print("")
            print("Invalid option, please try again.")
            return get_valid_option()
    except ValueError:
        print("")
        print("No option entered.\n Please try again...")
        return get_valid_option()
def load_todo_list():
    #Loads list from txt file and initiates the dictionary with the values in the file.
    #If the file doesn't exist, the program creates it and starts with an empty list.
    try:
        with open('data.txt', "r") as file:
            for line in file:
                activity, status = line.strip().split(': ')
                todo_list[activity] = status
    except:
        print("**************************************")
        print("*No database found, creating data.txt*")
        print("**************************************")
        file = open('data.txt', "x")
        return

def save_todo_list():
    #Updates txt file with the data on the dictionary
    with open('data.txt', "w") as file:
        for activity, status in todo_list.items():
            file.write(f"{activity}: {status}\n")
    
def add_activity():
    print("-----Add activity------")
    print("Enter 0 to go to main menu")
    activity = input("Please enter the name of an activity to add: \n")
    if not activity:
        print("***Please enter a valid activity name.***")
        return add_activity()
    elif activity in todo_list:
        print(f"{activity} is already on the list!")
        print("")
        return
    elif activity == "0":
        print("")
        return
    todo_list[activity] = "Pending"
    save_todo_list()
    print(f"***Added activity: {activity} - Pending***")
    print("-----------------------")


def mark_complete():
    print("-----Mark activity as complete-----")
    print("Enter 0 to go to main menu")
    activity = input("Which activity have you completed? \n")
    if not activity:
        print("***Please enter a valid activity name.***")
        return mark_complete()
    elif activity in todo_list:
        if todo_list[activity] == 'Pending':
            todo_list[activity] = 'Completed'
            print(f"You've succesfully updated activity {activity}")
            print("-----------------------------------")
        else:
            print(f"{activity} is already completed!")
            return mark_complete()
    elif activity == "0":
        return
    else:
        print(f"{activity} is not in your to do list, please try again or go back to main menu")
        return mark_complete()
    
def delete_activity():
    print("-----Delete activity-----")
    print("Enter 0 to go to main menu")
    activity = input("Which activity would you like to delete from the list? \n")
    if not activity:
        print("***Please enter a valid activity name.***")
        return delete_activity()
    elif activity in todo_list:
        todo_list.pop(activity)
        save_todo_list()
        print(f"{activity} deleted successfully!")
    elif activity == "0":
        return
    else:
        print(f"{activity} is not in your to do list")
        return delete_activity()
    
load_todo_list()
display_todo_list(todo_list,"Current to-do list:")
while True:
    main_menu()
    option = get_valid_option()
    
    if option == 1:
        print("")
        display_todo_list(todo_list,"Your to do list:")
        print("")
    elif option == 2:
        add_activity()
    elif option == 3:
        mark_complete()
    elif option == 4:
        delete_activity()
    elif option == 5:
        print("Saving and exiting.")
        save_todo_list()
        break

    