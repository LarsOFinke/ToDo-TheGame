import sqlite3, os, sys # FOR DB
from typing import Any, List, Tuple, Optional   # FOR "execute_query" FUNCTIONS
from . import logging  # GET .ENV CONSTANTS AND LOGGING
from werkzeug.security import generate_password_hash, check_password_hash # User-SYSTEM SECURITY


#-- EXECUTE SQL --#
def execute_query(sql: str, params: Tuple[Any, ...], connectionstring: str, fetch: bool = False) -> Optional[List[Tuple]]:
    """Executes a SQL command with the provided parameters.

    This function connects to the SQLite database, executes the specified SQL command with the given parameters,
    and optionally fetches the results based on the `fetch` argument. 

    Args:
        sql (str): The SQL-Command to be executed. This can be any valid SQL statement such as 
                   SELECT, INSERT, UPDATE, or DELETE.
                   
        connectionstring (str): The DB-Connection-String used for the query
                   
        params (Tuple[Any, ...]): A tuple containing the parameters to bind to the SQL command. 
                                The number and types of parameters should match the placeholders in the SQL statement.
                                
        fetch (bool, optional): If True, the function fetches and returns all rows of the result set as a list of tuples.
                                If False, it returns a boolean indicating whether any rows were affected by 
                                the SQL command (True for affected, False for none). Defaults to False.
    Returns:
        Optional[List[Tuple]]: 
            - If `fetch` is True, returns a list of tuples where each tuple represents a row fetched from the database. 
              Returns an empty list if no rows were returned.
            - If `fetch` is False, returns a boolean value:
              - True if the SQL command affected one or more rows.
              - False if no rows were affected.
            - Returns None if an error occurs during execution.

    """
    try:
        with sqlite3.connect(connectionstring) as con:
            cursor = con.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            con.commit()
            cursor.execute(sql, params)
            
            if fetch:
                return cursor.fetchall()  # Return fetched results
            
            else:
                return cursor.rowcount > 0  # Return True for insert/update/delete if any rows affected, else False
            
    except sqlite3.Error as e:
        logging.error(f"An error occurred: {e}")
        return None  # Return None in case of error


### SET UP DATABASES ###
DB_DIRECTORY = os.path.join(os.path.dirname(__file__), "db")

if not os.path.exists(DB_DIRECTORY):
    os.mkdir(DB_DIRECTORY)
    
CONNECTIONSTRING = os.path.join(os.path.dirname(DB_DIRECTORY), "db", "ToDo-TheGame.db")

def create_users_table() -> bool:
    try:
        sql: str = "CREATE TABLE tblUsers(" \
                    "UserID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "UserUsername TEXT NOT NULL UNIQUE, " \
                    "UserPassword TEXT NOT NULL, " \
                    "UserType TEXT NOT NULL)"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False
    
def create_admins() -> bool:
    try:
        hashed_password = generate_password_hash("admin", method='pbkdf2:sha256')
        sql: str = "INSERT INTO tblUsers(UserUsername, UserPassword, UserType) VALUES ('admin', ?, 'admin')"
        execute_query(sql, (hashed_password,), CONNECTIONSTRING)
        return True

    except sqlite3.Error as e:
        logging.error(e)
        return False   

def create_tasks_table():
    try:
        sql: str = "CREATE TABLE tblTasks(" \
                    "TaskID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "TaskMode TEXT NOT NULL, " \
                    "TaskTopic TEXT NOT NULL, " \
                    "TaskCategory TEXT NOT NULL, " \
                    "TaskPriority TEXT NOT NULL, " \
                    "TaskDeadlineDate DATE, " \
                    "TaskStartDate DATE, " \
                    "TaskRemainingTime TEXT, " \
                    "TaskTitle TEXT NOT NULL, " \
                    "TaskDescription TEXT NOT NULL, " \
                    "TaskIsOpen BOOLEAN NOT NULL, " \
                    "UserIDRef INTEGER, " \
                    "FOREIGN KEY(UserIDRef) REFERENCES tblUsers(UserID))"
                    
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

def create_todos_table():
    try:
        sql: str = "CREATE TABLE tblTodos(" \
                    "TodoID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "TodoText TEXT NOT NULL, " \
                    "TodoIsOpen BOOLEAN NOT NULL, " \
                    "TaskIDRef INTEGER, " \
                    "FOREIGN KEY(TaskIDRef) REFERENCES tblTasks(TaskID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

def create_teams_table():
    try:
        sql: str = "CREATE TABLE tblTeams(" \
                    "TeamID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "TeamName TEXT NOT NULL)"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

if not os.path.exists(CONNECTIONSTRING):
    if not create_users_table():
        logging.error("Could not create User-table! Something went wrong...")
        sys.exit()
    if not create_admins():
        logging.error("Could not create admins! Something went wrong...")
        sys.exit()
    if not create_tasks_table():
        logging.error("Could not create tasks-table! Something went wrong...")
        sys.exit()
    if not create_todos_table():
        logging.error("Could not create todos-table! Something went wrong...")
        sys.exit()
    if not create_teams_table():
        logging.error("Could not create teams-table! Something went wrong...")
        sys.exit()
          
 
### SET UP CRUD-FUNCTIONALITY ###

#-- User --#
def create_user(username: str, password: str) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    sql: str = "INSERT INTO tblUsers(UserUsername, UserPassword, UserType) VALUES (?, ?, 'user')"
    return execute_query(sql, (username, hashed_password), CONNECTIONSTRING)

def validate_user(username: str, password: str) -> bool:
    """Validates whether a User is successfull or not

    Args:
        username (str): Username from Frontend
        password (str): Password from Frontend

    Returns:
        True: if Password matches that from the database for the called user
        False: if user not found in the Database OR password does NOT match that from the database for the called user 
    """
    sql: str = "SELECT UserPassword FROM tblUsers WHERE UserUsername = ?"
    result = execute_query(sql, (username,), CONNECTIONSTRING, fetch=True)
    
    if not result:
        return False    # No matches for the username
    
    password_db = result[0][0]
    
    if check_password_hash(password_db, password):
        return True # Passwords match
    
    return False    # Password doesn't match with database

def get_all_usernames() -> list:
    """Returns a list containing all usernames in the database"""
    sql: str = "SELECT UserUsername FROM tblUsers"
    
    with sqlite3.connect(CONNECTIONSTRING) as con:
        cursor = con.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        usernames: list = [user[0] for user in results]
        
    return usernames

def get_user_id(username) -> int:
    """Returns the user id from the database"""
    sql: str = "SELECT UserID FROM tblUsers WHERE UserUsername = ?"
    result = execute_query(sql, (username,), CONNECTIONSTRING, fetch=True)
    user_id = result[0][0]
        
    return user_id


#-- TASKS --#
def add_new_task(new_task: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblTasks(TaskMode, TaskTopic, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription, TaskIsOpen)" \
                "VALUES (?,?,?,?,?,?,?,?,?,TRUE)"
    if not execute_query(
                    sql, 
                    (new_task["mode"], new_task["topic"], new_task["category"], new_task["priority"], 
                    new_task["deadlineDate"], new_task["startDate"], new_task["remainingTime"], 
                    new_task["title"], new_task["description"]), 
                    CONNECTIONSTRING
                ):
        return False
    
    # REPLACE WHERE-STATEMENT WITH E.G. DATE AS INDEX
    task_id = execute_query("SELECT TaskID FROM tblTasks WHERE TaskTitle = ?", (new_task["title"],), CONNECTIONSTRING, fetch=True)[0][0]  
    
    if len(new_task["todos"]) > 0:
        for todo in new_task["todos"]:
            sql: str = "INSERT INTO tblTodos(TodoText, TodoIsOpen, TaskIDRef) VALUES (?,TRUE,?)"
            execute_query(sql, (todo["text"], task_id), CONNECTIONSTRING)
        
    return True

def get_all_open_tasks() -> list[dict]:
    """Returns a list containing all tasks in the database"""
    sql: str = "SELECT TaskID, TaskMode, TaskTopic, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription, TaskIsOpen FROM tblTasks"
    
    with sqlite3.connect(CONNECTIONSTRING) as con:
        cursor = con.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        tasks: list = [
                            {
                                "id": task[0],
                                "mode": task[1],
                                "topic": task[2],
                                "category": task[3],
                                "priority": task[4],
                                "deadlineDate": task[5],
                                "startDate": task[6],
                                "remainingTime": task[7],
                                "title": task[8],
                                "description": task[9],
                                "todos": get_todos_for_task(task[0])
                            }
                            for task in results
                            if task[10] == 1
                       ]
    
    return tasks

def edit_task(edited_task: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "UPDATE tblTasks " \
                "SET TaskMode = ?, TaskTopic = ?, TaskCategory = ?, TaskPriority = ?, TaskDeadlineDate = ?, TaskStartDate = ?, TaskRemainingTime = ?, TaskTitle = ?, TaskDescription = ? " \
                "WHERE TaskID = ?"      
    if execute_query(
                            sql, 
                            (edited_task["mode"], edited_task["topic"], edited_task["category"], edited_task["priority"], 
                            str(edited_task["deadlineDate"]), edited_task["startDate"], edited_task["remainingTime"], 
                            edited_task["title"], edited_task["description"], edited_task["id"]), 
                            CONNECTIONSTRING
                        ):
        if not update_todos_for_task(edited_task["todos"]):
            return False
    
        if len(edited_task["deletedTodos"]) > 0:
            for todo in edited_task["deletedTodos"]:
                if not delete_todo(todo["id"]):
                    return False
                
        if len(edited_task["newTodoList"]) > 0:
            for todo in edited_task["newTodoList"]:
                if not add_todo_to_task(todo["text"], edited_task["id"]):
                    return False
        return True

def delete_task(task_id: int) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "DELETE FROM tblTodos WHERE TaskIDRef = ?"
    execute_query(sql, (task_id,), CONNECTIONSTRING)

    sql: str = "DELETE FROM tblTasks WHERE TaskID = ?"          
    return execute_query(sql, (task_id,), CONNECTIONSTRING)

def close_task(task_id: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    if close_todos_for_task(task_id):
        sql: str = "UPDATE tblTasks SET TaskIsOpen=FALSE WHERE TaskID = ?"      
        return execute_query(sql, (task_id,), CONNECTIONSTRING)


#-- TODOS --#
def add_todo_to_task(todo: str, task_id: int) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblTodos(TodoText, TodoIsOpen, TaskIDRef) VALUES (?,TRUE,?)"
    return execute_query(sql, (todo, task_id), CONNECTIONSTRING)

def get_todos_for_task(task_id: int) -> list[dict]:
    """Returns a list containing all todos for the task."""
    sql: str = "SELECT TodoID, TodoText, TodoIsOpen, TaskIDRef FROM tblTodos WHERE TaskIDRef = ?"
    
    with sqlite3.connect(CONNECTIONSTRING) as con:
        cursor = con.cursor()
        cursor.execute(sql, (task_id,))
        results = cursor.fetchall()
        
        todos: list = [
            {
                "id": todo[0],
                "text": todo[1],
                "isOpen": todo[2],
                "taskIdRef": todo[3],
            }
            for todo in results
        ]
    
    return todos

def update_todos_for_task(todos: list[dict]) -> bool:
    for todo in todos:
        sql: str = "UPDATE tblTodos SET TodoText=?, TodoIsOpen=? WHERE TodoID=?"
        if execute_query(sql, (todo["text"], todo["isOpen"], todo["id"]), CONNECTIONSTRING):
            continue
        else:
            return False
    return True

def close_todos_for_task(task_id: int) -> bool:
    sql: str = "UPDATE tblTodos SET TodoIsOpen=FALSE WHERE TaskIDRef = ?"
    return execute_query(sql, (task_id,), CONNECTIONSTRING)

def delete_todo(todo_id: int) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "DELETE FROM tblTodos WHERE TodoID = ?"      
    return execute_query(sql, (todo_id,), CONNECTIONSTRING)


#-- TEAMS --#
def add_new_team(team_name: str) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblTeams(TeamName) VALUES (?)"
    return execute_query(sql, (team_name,), CONNECTIONSTRING)