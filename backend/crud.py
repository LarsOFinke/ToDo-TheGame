import sqlite3, os, sys # FOR DB
from typing import Any, List, Tuple, Optional   # FOR "execute_query" FUNCTIONS
from . import logging  # GET .ENV CONSTANTS AND LOGGING
from werkzeug.security import generate_password_hash, check_password_hash # User-SYSTEM SECURITY


# EXECUTE SQL
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


def create_user_table() -> bool:
    try:
        sql: str = "CREATE TABLE tblUser(" \
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
        sql: str = "INSERT INTO tblUser(UserUsername, UserPassword, UserType) VALUES ('admin', ?, 'admin')"
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
                    "TaskCategory TEXT NOT NULL, " \
                    "TaskPriority TEXT NOT NULL, " \
                    "TaskDeadlineDate DATE, " \
                    "TaskStartDate DATE, " \
                    "TaskRemainingTime TEXT, " \
                    "TaskTitle TEXT NOT NULL, " \
                    "TaskDescription TEXT NOT NULL)"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False
    
if not os.path.exists(CONNECTIONSTRING):
    if not create_user_table():
        logging.error("Could not create User-table! Something went wrong...")
        sys.exit()
    if not create_admins():
        logging.error("Could not create admins! Something went wrong...")
        sys.exit()
    if not create_tasks_table():
        logging.error("Could not create tasks-table! Something went wrong...")
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
    sql: str = "INSERT INTO tblUser(UserUsername, UserPassword, UserType) VALUES (?, ?, 'user')"
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
    sql: str = "SELECT UserPassword FROM tblUser WHERE UserUsername = ?"
    result = execute_query(sql, (username,), CONNECTIONSTRING, fetch=True)
    
    if not result:
        return False    # No matches for the username
    
    password_db = result[0][0]
    
    if check_password_hash(password_db, password):
        return True # Passwords match
    
    return False    # Password doesn't match with database

def get_all_usernames() -> list:
    """Returns a list containing all usernames in the database"""
    sql: str = "SELECT UserUsername FROM tblUser"
    
    with sqlite3.connect(CONNECTIONSTRING) as con:
        cursor = con.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        usernames: list = [user[0] for user in results]
        
    return usernames


#-- TASKS --#

def add_new_task(new_task: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblTasks(TaskMode, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription)" \
                "VALUES (?,?,?,?,?,?,?,?)"
                
    return execute_query(
                            sql, 
                            (new_task["mode"], new_task["category"], new_task["priority"], 
                            new_task["deadlineDate"], new_task["startDate"], new_task["remainingTime"], 
                            new_task["title"], new_task["description"]), 
                            CONNECTIONSTRING
                        )

def get_all_tasks() -> list:
    """Returns a list containing all tasks in the database"""
    sql: str = "SELECT TaskID, TaskMode, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription FROM tblTasks"
    
    with sqlite3.connect(CONNECTIONSTRING) as con:
        cursor = con.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        
        tasks: list = [
                            {
                                "id": task[0],
                                "mode": task[1],
                                "category": task[2],
                                "priority": task[3],
                                "deadlineDate": task[4],
                                "startDate": task[5],
                                "remainingTime": task[6],
                                "title": task[7],
                                "description": task[8]
                            }
                            for task in results
                       ]
        
    return tasks

def edit_task(edited_task: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "UPDATE tblTasks " \
                "SET TaskMode = ?, TaskCategory = ?, TaskPriority = ?, TaskDeadlineDate = ?, TaskStartDate = ?, TaskRemainingTime = ?, TaskTitle = ?, TaskDescription = ? " \
                "WHERE TaskID = 1"
                
    return execute_query(
                            sql, 
                            (edited_task["mode"], edited_task["category"], edited_task["priority"], 
                            str(edited_task["deadlineDate"]), edited_task["startDate"], edited_task["remainingTime"], 
                            edited_task["title"], edited_task["description"]), 
                            CONNECTIONSTRING
                        )
