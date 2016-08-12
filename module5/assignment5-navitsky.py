'''
Assignment 5
Foundations of Programming: Python
23 July 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:

Script manages a "ToDo list." The ToDo file will contain (Task, Priority)
which stored in a Python Dictionary. Each Dictionary will represent
one row of data. Data will then be added to a Python List to create a
table of data.

Create a text file called todo.txt using the following data:

  Clean House, low
  Pay Bills, high

When the program starts, load the each row of data you have in the todo.txt
text file into a python Dictionary.

After you get a row of data add it to a Python List object (now the data will
be managed as a table or two dimensional array).

Display the contents of the List to the user.

Allow the user to Add or Remove tasks from the list, plus Save the tasks in
the List tasks-priorities.

Save the data from the table into the todo.txt file when the program exits.
'''


#--- File Handling

# Open file in append mode, then close it, which will create the
# file if it doesn't already exist.  This simplifies the exception
# handling during the data import.
def file_exists():

    # return a flag indicating success/failure
    _error=False
    _error_msg=""

    try:
        _todo_file = open("todo.txt", "a")
        _todo_file.close()

    except:
        _error=True
        _error_msg="Cannot open todo.txt for writing, check file permissions."

    finally:
        return (_error, _error_msg)


# read the existing records from the todo.txt file
def read_data():

    # return a flag indicating success/failure
    _error=False
    _error_msg=""
    _task_list = []
    # if we don't read anything from file, start the last id at 1
    _last_id = 1

    try:
        _todo_file = open("todo.txt", "r")

        # file is pipe delimited to allow the use of commas in the data
        for _line in _todo_file:
            # read in line of task data
            _task_id, _task_name, _task_priority = _line.split("|")
            # create a list with the task data stripping the
            # new line from the file
            _record = { "id": _task_id, "task": _task_name, "priority": _task_priority.strip("\n")}
            # add record to the inventory
            _task_list.append(_record)
        _todo_file.close()

        # figure out what the last id is so we can compute an id for new record

        # we don't control the order of the file so we can't assume the last id
        # is the largest.  scan the list for the largest id.
        for _record in _task_list:
            if int(_record["id"]) > _last_id:
                _last_id = int(_record["id"])

    except:
        _error=True
        _error_msg="Could not read contents of todo.txt, check for corruption."

    finally:
        return( _error, _error_msg, _task_list, _last_id)


# save todo list to the file todo.txt
def save_data(_task_list):
    # open todo file in write mode in the current directory
    # this overwrites the current file, but we have the previous
    # entries in memory
    _error=False
    _msg=""

    try:
        _todo_file = open("todo.txt", "w")

        print()

        # write out the records
        for _record in _task_list:
            # unpack the values for processing
            _task_id = _record["id"]
            _task_name = _record["task"]
            _task_priority = _record["priority"]

            # give the user feedback
            print("...writing: " + _task_name)

            # write the entry to the file
            _todo_file.write(str(_task_id) + "|" + _task_name + "|" + str(_task_priority) + "\n")

        print()
        # close the file before exiting
        _todo_file.close()
        _msg="Successfully wrote tasks to todo.txt!"

    except:
        _error=True
        _msg="Could not write records to todo.txt!"

    finally:
        return(_error, _msg)


#--- User I/O


# upon fatal error, print error message and exit
def croak():
    print()
    print("FATAL ERROR!", error_msg)
    print("Cannot continue, program exiting.")
    exit()


# print the available commands
def print_help(_msg):
    print()
    print("Available commands:")
    print(_msg)


# only take yes or no for an answer
def get_yes_no(_prompt):

    print()

    while(True):

        # get some input
        _entry = False
        while(not _entry):
            _entry = input(_prompt).strip()
            _entry = _entry.lower()

        # check for yes; exit if found
        if _entry in [ "y", "yes" ]:
            _return = True
            break

        # check for no; exit if found
        elif _entry in [ "n", "no" ]:
            _return = False
            break

        # if it didn't match yes or no, ask again
        else:
            continue

    # return a bool so we can test if true
    return(_return)


# get the task name
def enter_task(_prompt):

    # return a flag if we are returning valid input.
    _abort = False
    _task_name = ""

    while (True):

        # get some input
        while (not _task_name):
            _task_name = input(_prompt).strip()

        # let them abort if they want
        if _task_name.lower() in [ "q", "quit", "exit" ]:
            _task_name = ""
            _abort = True

        # check for accidental use of contextually incorrect commands
        # this helps avoid them entering a task named "list", etc. by
        # accident.
        invalid_entries = [ "l", "list", "a", "add", "r", "remove", "?", "help" ]
        if _task_name.lower() in invalid_entries:
            print("You cannot enter that command here.")
            print()
            _task_name = ""
            continue

        # we don't really have a way to validate task names beyond what we have
        # done above, so anything that gets this far is assumed a valid task
        # name.
        break

    return (_abort, _task_name)


# get the task priority
def enter_priority():

    # return a flag if we are returning valid input.
    _abort = False
    _task_priority = ""

    while(True):

        # get some input
        while(not _task_priority):
            _task_priority=input("Enter the task priority, [h]igh, [m]edium, [l]ow or [q]uit: ").strip().lower()

        # check for accidental use of contextually incorrect commands
        # this helps avoid them entering a priority named "list", etc. by
        # accident.
        invalid_entries = [ "list", "a", "add", "r", "remove", "?", "help" ]
        if _task_priority.lower() in invalid_entries:
            print("You cannot enter that command here.")
            print()
            _task_priority = ""
            continue

        # convert input into consistent values
        if _task_priority in [ "h", "high" ]:
            _task_priority = "high"
            break

        if _task_priority in [ "m", "medium", "med" ]:
            _task_priority = "medium"
            break

        if _task_priority in [ "l", "low" ]:
            _task_priority = "low"
            break

        # let them abort if they want
        if _task_priority in [ "q", "quit", "exit" ]:
            _task_priority = ""
            _abort = True
            break

        # if they get this far the input wasn't a valid setting so do it again

    return(_abort, _task_priority)


#--- Commands


# add tasks until the user quits
def add_records():

    # return a flag if we are returning valid input.
    abort_name=False
    abort_priority=False
    global last_id

    while(not abort_name or not abort_priority):

        print()

        # get task name
        abort_name, task_name = enter_task("Enter the name of the task to add or [q]uit: ")
        if abort_name:
            print("Exiting task entry mode by request.")
            print()
            # exit add mode if user specifies quit
            break

        print()

        # get task priority
        abort_priority, task_priority = enter_priority()
        if abort_priority:
            print("Abandoning task by request.")
            # if the user specified quit during task priority entry we'll
            # assume they didn't like their entry and we'll just retry.
            continue

        # we have an entry, let's save it

        # id will be the last_id plus 1
        task_id = last_id + 1
        # increment the last_id
        last_id += 1

        # make a todo dictionary record
        record = { "id": task_id, "task": task_name, "priority": task_priority}

        # add record to the task list
        task_list.append(record)


# remove a task
def remove_item():

    # return a flag if we are returning valid input.
    abort_name = False
    # since they want to remove an existing entry, refresh their memory
    print_tasks(task_list)

    while (not abort_name):

        # get task name
        abort_name, task_name = enter_task("Enter the name or id# of the task to remove or [q]uit: ")
        if abort_name:
            print("Exiting task removal mode by request.")
            print()
            # exit remove mode if user specifies quit
            break

        # scan the list for the specified entry.  check all entries that start with the
        # string for easier lookup.  also check the id as an alternate method of selection.
        # use index for deletion because there may be multiple entries of the same name
        records_found = 0
        for index, task in enumerate(task_list):
            if task["task"].lower().startswith(task_name.lower()) or task_name == str(task["id"]):
                # keep track entries if we have a match
                del_index = index
                del_task = task["task"]
                del_id = str(task["id"])
                # keep track of how many you found to avoid ambiguity
                records_found = records_found + 1

        # if more than one entry matches give them a selection hint and make them
        # try again.
        if records_found > 1:
            print("Request matches more than one record, please select entry by id.")
            continue

        # make sure they really want to delete
        _prompt="Are you sure you wish to remove id# " + del_id + " '" + del_task + "'? "
        remove_directive = get_yes_no(_prompt)

        # delete specified entry
        if remove_directive:
            del task_list[del_index]
            print("Deleted id#", del_id, "'" + del_task + "'.")
            print()
            break

        # let them know we are not deleting
        else:
            print("Not deleting", del_task, "by request.")
            print()
            abort_name = True
            break


# print a formatted list of tasks to the screen
def print_tasks(_task_list):
    # don't print header if task list is empty
    if _task_list:

        # print header
        print()
        print("id".ljust(4), "task".ljust(20), "priority".ljust(8))
        print("-" * 4, "-" * 20, "-" * 8)

        # print each entry in the task list
        for _record in _task_list:
            print(str(_record["id"]).ljust(4), _record["task"].ljust(20), _record["priority"].ljust(8))
        print()

    else:
        # handle empty lists
        print()
        print("  No entries yet")
        print()


#--- Main Method


CMD_HELP = """
  '?' or 'help' to print this help")
  'a' or 'add' to add a task")
  'r' or 'remove' to remove a task")
  'l' or 'list' to list tasks")
  'q' or 'quit' or 'exit' to exit")
"""

# print a banner
print()
print("TASK MANAGER 2000")
print("[a]dd, [l]ist, [r]emove tasks")
print()

# test that the todo.txt file exists and is writable
error, error_msg = file_exists()
if error:
    # if we can't open the file, we can't proceed.
    croak()

# read any existing data from todo.txt
error, error_msg, task_list, last_id = read_data()
if error:
    # if the contents of the file don't match our expectations
    # we can't proceed.
    croak()

# command loop
#   ask for commands until user asks to exit

while(True):

    # get some input, strip white-space and convert to lower case
    # to provide a more forgiving user interface.
    command=""
    while (not command):
        command = input("Enter a command, '?' for help: ").strip()
        command = command.lower()

    # help; print their options
    if command in [ "?", "h", "help" ]:
        print_help(CMD_HELP)
        continue

    # quit; they want to exit the program
    if command in [ "q", "quit", "exit" ]:
        # ask if they'd like to save
        quit_directive = get_yes_no("Are you sure you want to quit [y/n]? ")
        # save the data
        if quit_directive:
            # quit the main command loop
            break
        else:
            # go back to the command loop
            print()
            continue

    # list; show them the current task items
    if command in [ "l", "list", "p", "print" ]:
        print_tasks(task_list)
        continue

    # add; go into task data entry mode
    if command in [ "a", "add", "n", "new" ]:
        # remind them this is a entry *loop*
        print()
        print("Continue to add tasks until you are done.")
        add_records()
        continue

    # remove; let them remove an entry
    if command in [ "r", "remove", "d", "del", "delete" ]:
        print()
        print("Remove a single entry.")
        remove_item()
        continue

# done with command loop, we are exiting

# only ask them to save if the task list is not empty
if task_list:

    # ask if they'd like to save
    save_directive = get_yes_no("Would you like to save these records [y/n]? ")

    # save as directed
    if save_directive:

        # open todo file in write mode in the current directory
        # this overwrites the current file, but we have any previous
        # entries in memory

        # save data
        error, msg = save_data(task_list)
        if error:
            # since we previously opened and read the file, errors here are
            # both unclear and unrecoverable.  print a message and exit.
            croak()
        else:
            # print success
            print(msg)

    else:
        # acknowledge the user decision to exit w/o save
        print()
        print("Exit without save per request.")

else:
    # let the user know we aren't saving because there is no data to save
    print("No tasks to save, Goodbye!")