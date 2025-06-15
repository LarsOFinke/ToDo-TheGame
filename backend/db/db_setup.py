import sqlite3, os, sys # FOR DB
from typing import Any, List, Tuple, Optional   # FOR "execute_query" FUNCTIONS
from werkzeug.security import generate_password_hash, check_password_hash # User-SYSTEM SECURITY
from .. import logging  # GET .ENV CONSTANTS AND LOGGING


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


### SET UP DATABASE ###
DB_DIRECTORY = os.path.join(os.path.dirname(__file__), "databases")
CONNECTIONSTRING = os.path.join(os.path.dirname(DB_DIRECTORY), "databases", "ToDo-TheGame.db")

if not os.path.exists(DB_DIRECTORY):
    os.mkdir(DB_DIRECTORY)
    
## SET UP TABLES ##

# USERS-SYSTEM #
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

# TEAMS-SYSTEM #
def create_teams_table():
    try:
        sql: str = "CREATE TABLE tblTeams(" \
                    "TeamID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "TeamName TEXT NOT NULL, " \
                    "UserIDRef INTEGER, " \
                    "FOREIGN KEY(UserIDRef) REFERENCES tblUsers(UserID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

# TASKS-SYSTEM #
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
                    "TeamIDRef INTEGER, " \
                    "FOREIGN KEY(UserIDRef) REFERENCES tblUsers(UserID), " \
                    "FOREIGN KEY(TeamIDRef) REFERENCES tblTeams(TeamID))"
                    
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

# MEMBERS-SYSTEM #
def create_members_table():
    try:
        sql: str = "CREATE TABLE tblMembers(" \
                    "MemberID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "TeamName TEXT NOT NULL, " \
                    "UserIDRef INTEGER, " \
                    "TeamIDRef INTEGER, " \
                    "FOREIGN KEY(UserIDRef) REFERENCES tblTeams(UserID), " \
                    "FOREIGN KEY(TeamIDRef) REFERENCES tblUsers(TeamID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

# REPORT-BOOK-SYSTEM #
def create_report_books_table():
    try:
        sql: str = "CREATE TABLE tblReportBooks(" \
                    "ReportBookID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "UserIDRef INTEGER, " \
                    "FOREIGN KEY(UserIDRef) REFERENCES tblUsers(UserID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

def create_weeks_table():
    try:
        sql: str = "CREATE TABLE tblWeeks(" \
                    "WeekID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "WeekFrom DATE NOT NULL, " \
                    "WeekTo DATE NOT NULL, " \
                    "ReportBookIDRef INTEGER, " \
                    "FOREIGN KEY(ReportBookIDRef) REFERENCES tblReportBooks(ReportBookID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

def create_days_table():
    try:
        sql: str = "CREATE TABLE tblDays(" \
                    "DayID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "DayDate DATE NOT NULL, " \
                    "WeekIDRef INTEGER, " \
                    "FOREIGN KEY(WeekIDRef) REFERENCES tblWeeks(WeekID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

def create_report_entries_table():
    try:
        sql: str = "CREATE TABLE tblReportEntries(" \
                    "ReportEntryID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "ReportEntryLearningField TEXT NOT NULL, " \
                    "ReportEntryActivity TEXT NOT NULL, " \
                    "ReportEntryDuration REAL NOT NULL, " \
                    "DayIDRef INTEGER, " \
                    "FOREIGN KEY(DayIDRef) REFERENCES tblDays(DayID))"
        execute_query(sql, (), CONNECTIONSTRING)
        return True
    
    except sqlite3.Error as e:
        logging.error(e)
        return False

## CHECK IF DATABASE ALREADY EXISTS, CREATE IF NOT ##
if not os.path.exists(CONNECTIONSTRING):
    if not create_users_table():
        logging.error("Could not create User-table! Something went wrong...")
        sys.exit()
    if not create_admins():
        logging.error("Could not create admins! Something went wrong...")
        sys.exit()
    if not create_teams_table():
        logging.error("Could not create teams-table! Something went wrong...")
        sys.exit()
    if not create_tasks_table():
        logging.error("Could not create tasks-table! Something went wrong...")
        sys.exit()
    if not create_todos_table():
        logging.error("Could not create todos-table! Something went wrong...")
        sys.exit()
    if not create_members_table():
        logging.error("Could not create members-table! Something went wrong...")
        sys.exit()
    if not create_report_books_table():
        logging.error("Could not create report-book-table! Something went wrong...")
        sys.exit()
    if not create_weeks_table():
        logging.error("Could not create weeks-table! Something went wrong...")
        sys.exit()
    if not create_days_table():
        logging.error("Could not create days-table! Something went wrong...")
        sys.exit()
    if not create_report_entries_table():
        logging.error("Could not create report-entries-table! Something went wrong...")
        sys.exit()
