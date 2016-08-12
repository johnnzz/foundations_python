'''
Assignment 6
Foundations of Programming: Python
28 July 2016

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

Rubric:

    Make a function for the code that loads the each rows of data you have in the
      ToDo.txt text file into a python Dictionary and adds it to a Python List.

    Make a function for the code that displays the contents of the List to the user.

    Make a function for the code that allows the user to Add or Remove tasks from
      the list, plus save the tasks in the List tasks-priorities using numbered choices.

    Make a function for the code that saves the data from the table into the Todo.txt
       file when the program exits.

    Make a Class to hold the functions.
'''


file_name="todo.txt"
last_id=0

CMD_HELP = """
  '?' or 'help' to print this help")
  '1', 'a' or 'add' to add a task")
  '2', 'r' or 'remove' to remove a task")
  '3', 'l' or 'list' to list tasks")
  '4', 'q' or 'quit' or 'exit' to exit")
"""

class todo():
    """
    Class that manipulates a todo list.

    Rubric:

        Make a Class to hold the functions.
    """

    @staticmethod

    def ensure_file_exists(_file_name = "todo.txt"):
        """
        Open file in append mode, then close it, which will create the
        file if it doesn't already exist.  This simplifies the exception
        handling during the data import.

        args:
            file_name (string): name of file to process

        returns:
            error (bool): True if an error was encountered, else False
            error_msg (string): Message describing the failure, if any
        """

        # return a flag indicating success/failure
        _error=False
        _error_msg=""

        try:
            _todo_file = open(_file_name, "a")
            _todo_file.close()

        except:
            _error=True
            _error_msg="Cannot open " + _file_name + " for writing, check file permissions."

        finally:
            return (_error, _error_msg)


    def read_data(_file_name = "todo.txt"):
        """
        read the existing records from the file

        file:
            File is expected to be character delimited (pipe) with three
            fields, ID#, task name, task priority

            ex:
                1|wash dishes|low
                2|clean house|low
                3|watch Lost|high

            fields:
                ID#: unique integer
                task name: string
                task priority: string; one of 'high', 'medium', 'low'

        args:
            file_name (string): name of the file to process

        returns:
            error (bool): True if an error was encountered, else False
            error_msg (string): Message describing the failure, if any
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }
            last_id (int): ID number of the last entry, defaults to 1

        Rubric:

            Make a function for the code that loads the each rows of data you have in the
            ToDo.txt text file into a python Dictionary and adds it to a Python List.

        """

        # return a flag indicating success/failure
        _error=False
        _error_msg=""
        _task_list = []
        _last_id = 0

        try:
            _todo_file = open(_file_name, "r")

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
            if _file_name == None:
                _error_msg="The file name was not defined."
            else:
                _error_msg="Could not read contents of "+ _file_name + ", check for corruption."

        finally:
            return( _error, _error_msg, _task_list, _last_id)


    def save_data(_task_list = [], _file_name = "todo.txt"):
        """
        write the existing records to the file

        file:
            File is to be character delimited (pipe) with three
            fields, ID#, task name, task priority

            ex:
                1|wash dishes|low
                2|clean house|low
                3|watch Lost|high

            fields:
                ID#: unique integer
                task name: string
                task priority: string; one of 'high', 'medium', 'low'

        args:
            file_name (string): name of the file to process
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }

        returns:
            error (bool): True if an error was encountered, else False
            msg (string):
                if failure: Message describing the failure
                else: Message describing success

        Rubric:

            Make a function for the code that saves the data from the table into the Todo.txt
            file when the program exits.

        """

        # open file in write mode, this overwrites the current file,
        # but we have the previous entries in memory
        _error=False
        _msg=""

        try:
            _todo_file = open(_file_name, "w")

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
            _msg="Successfully wrote tasks to " + _file_name + "!"

        except:
            _error=True
            _msg="Could not write records to " + _file_name + "!"

        finally:
            return(_error, _msg)


    def croak(_error_msg = "Unspecified error"):
        """
        upon fatal error, print error message and exit

        args:
            _error_msg (string): description of the error

        returns:
            doesn't
        """
        print()
        print("FATAL ERROR!", _error_msg)
        print("Cannot continue, program exiting.")
        exit()


    def list_avail_commands(_msg = "None specified"):
        """
        print the available commands

        args:
            _msg (string): text describing available commands

        returns:
            nothing

        Rubric:

            Make a function for the code that displays the contents of the List to the user.

        """
        print()
        print("Available commands:")
        print(_msg)


    def proceed_yes_no(_prompt = "Enter [y]es or [n]o: "):
        """
        get a yes or no answer from the user

        args:
            prompt (string): text to prompt user with

        returns:
            choice (bool): True if yes, False if no
        """

        print()

        while(True):

            # get some input
            _entry = False
            while(not _entry):
                _entry = input(_prompt).strip()
                _entry = _entry.lower()

            # check for yes; exit if found
            if _entry in [ "y", "yes" ]:
                _choice = True
                break

            # check for no; exit if found
            elif _entry in [ "n", "no" ]:
                _choice = False
                break

            # if it didn't match yes or no, ask again
            else:
                continue

        # return a bool so we can test if true
        return(_choice)


    def get_task_name(_prompt = "Enter the task name: ",
                      _invalid_entries = [ "l", "list", "a", "add", "r", "remove", "?", "help" ]):
        """
        get the task name

        args:
            prompt (string): text to prompt user with

        returns:
            abort (bool): if True, quit requested
            task_name (string): task name, if quit not requested, else null
        """

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
            if _task_name.lower() in _invalid_entries:
                print("You cannot enter that command here.")
                print()
                _task_name = ""
                continue

            # we don't really have a way to validate task names beyond what we have
            # done above, so anything that gets this far is assumed a valid task
            # name.
            break

        return (_abort, _task_name)


    def get_priority(_prompt = "Enter the task priority, [h]igh, [m]edium, [l]ow or [q]uit: ",
                     _invalid_entries = [ "list", "a", "add", "r", "remove", "?", "help" ]):
        """
        get the task priority

        args:
            prompt (string): text to prompt user with

        returns:
            abort (bool): if True, quit requested
            task_priority (string): task priority ["high", "medium", "low"],
                if quit not requested, else null
        """

        # return a flag if we are returning valid input.
        _abort = False
        _task_priority = ""

        while(True):

            # get some input
            while(not _task_priority):
                _task_priority=input(_prompt).strip().lower()

            # check for accidental use of contextually incorrect commands
            # this helps avoid them entering a priority named "list", etc. by
            # accident.
            if _task_priority.lower() in _invalid_entries:
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


    def add_record_loop(_task_list = [], _last_id = 0):
        """
        add tasks until the user quits

        args:
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }

            last_id (int): last (greatest) id# in task_list

        returns:
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }
            last_id (int): last ID#

        Rubric:

            Make a function for the code that allows the user to Add or Remove tasks from
            the list, plus save the tasks in the List tasks-priorities using numbered choices.

        """

        # return a flag if we are returning valid input.
        _abort_name=False
        _abort_priority=False

        while(not _abort_name or not _abort_priority):

            print()

            # get task name
            _abort_name, _task_name = todo.get_task_name("Enter the name of the task to add or [q]uit: ")
            if _abort_name:
                print("Exiting task entry mode by request.")
                print()
                # exit add mode if user specifies quit
                break

            print()

            # get task priority
            _abort_priority, _task_priority = todo.get_priority("Enter the task priority, [h]igh, [m]edium, [l]ow or [q]uit: ")
            if _abort_priority:
                print("Abandoning task by request.")
                # if the user specified quit during task priority entry we'll
                # assume they didn't like their entry and we'll just retry.
                continue

            # we have an entry, let's save it

            # id will be the last_id plus 1
            _task_id = _last_id + 1
            # increment the last_id
            _last_id += 1

            # make a todo dictionary record
            _record = { "id": _task_id, "task": _task_name, "priority": _task_priority}

            # add record to the task list
            _task_list.append(_record)

        return(_task_list, _last_id)


    def remove_a_record(_task_list = []):
        """
        remove a task

        args:
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }

        returns:
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }

        Rubric:

            Make a function for the code that allows the user to Add or Remove tasks from
            the list, plus save the tasks in the List tasks-priorities using numbered choices.

        """

        # return a flag if we are returning valid input.
        _abort_name = False
        # since they want to remove an existing entry, refresh their memory
        todo.list_current_tasks(_task_list)

        while (not _abort_name):

            # get task name
            _abort_name, _task_name = todo.get_task_name("Enter the name or id# of the task to remove or [q]uit: ")
            if _abort_name:
                print("Exiting task removal mode by request.")
                print()
                # exit remove mode if user specifies quit
                break

            # scan the list for the specified entry.  check all entries that start with the
            # string for easier lookup.  also check the id as an alternate method of selection.
            # use index for deletion because there may be multiple entries of the same name
            _records_found = 0
            for _index, _task in enumerate(_task_list):
                if _task["task"].lower().startswith(_task_name.lower()) or _task_name == str(_task["id"]):
                    # keep track entries if we have a match
                    _del_index = _index
                    _del_task = _task["task"]
                    _del_id = str(_task["id"])
                    # keep track of how many you found to avoid ambiguity
                    _records_found = _records_found + 1

            # if more than one entry matches give them a selection hint and make them
            # try again.
            if _records_found > 1:
                print("Request matches more than one record, please select entry by id.")
                continue

            # make sure they really want to delete
            _prompt="Are you sure you wish to remove id# " + _del_id + " '" + _del_task + "' [y/n]? "
            _remove_directive = todo.proceed_yes_no(_prompt)

            # delete specified entry
            if _remove_directive:
                del _task_list[_del_index]
                print("Deleted id#", _del_id, "'" + _del_task + "'.")
                print()
                break

            # let them know we are not deleting
            else:
                print("Not deleting", _del_task, "by request.")
                print()
                _abort_name = True
                break

        return(_task_list)


    def list_current_tasks(_task_list):
        """
        print a formatted list of tasks to the screen

        args:
            task_list (list of dicts): Tasks loaded into a list of dicts
                dict = { 'id': <id num>, 'task': <task name>,
                    'priority': <task priority> }
        returns:
            nothing

        Rubric:

            Make a function for the code that displays the contents of the List to the user.

        """

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
            print("  No tasks to list.")
            print()



# print a banner
print()
print("TASK MANAGER 2000")
print("[1][a]dd, [2][r]emove tasks, [3][l]ist, [4][q]uit, [?]help")
print()

# test that the todo.txt file exists and is writable
error, error_msg = todo.ensure_file_exists(file_name)
if error:
    # if we can't open the file, we can't proceed.
    todo.croak(error_msg)

# read any existing data from todo.txt
error, error_msg, task_list, last_id = todo.read_data(file_name)
if error:
    # if the contents of the file don't match our expectations
    # we can't proceed.
    todo.croak(error_msg)

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
        todo.list_avail_commands(CMD_HELP)
        continue


    # quit; they want to exit the program
    if command in [ "4", "q", "quit", "exit" ]:
        # ask if they'd like to save
        quit_directive = todo.proceed_yes_no("Are you sure you want to quit [y/n]? ")
        # save the data
        if quit_directive:
            # quit the main command loop
            break
        else:
            # go back to the command loop
            print()
            continue


    # list; show them the current task items
    if command in [ "3", "l", "list", "p", "print" ]:
        todo.list_current_tasks(task_list)
        continue


    # add; go into task data entry mode
    if command in [ "1", "a", "add", "n", "new" ]:
        # remind them this is a entry *loop*
        print()
        print("Continue to add tasks until you are done.")
        task_list, last_id = todo.add_record_loop(task_list, last_id)
        continue


    # remove; let them remove an entry
    if command in [ "2", "r", "remove", "d", "del", "delete" ]:
        print()
        print("Remove a single entry.")
        if task_list:
            task_list = todo.remove_a_record(task_list)
            continue
        else:
            print("  No tasks to remove.")
            print()
            continue

# done with command loop, we are exiting

# only ask them to save if the task list is not empty
if task_list:

    # ask if they'd like to save
    save_directive = todo.proceed_yes_no("Would you like to save these records [y/n]? ")

    # save as directed
    if save_directive:

        # open todo file in write mode in the current directory
        # this overwrites the current file, but we have any previous
        # entries in memory

        # save data
        error, msg = todo.save_data(task_list, file_name)
        if error:
            # since we previously opened and read the file, errors here are
            # both unclear and unrecoverable.  print a message and exit.
            todo.croak(msg)
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