from .db_setup import execute_query, CONNECTIONSTRING
from .db_todos import add_todo_to_task, get_todos_for_task, update_todos_for_task, close_todos_for_task, delete_todo

def add_new_task(mode: str, new_task: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = f"INSERT INTO tblTasks(TaskMode, TaskTopic, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription, TaskIsOpen, {mode.upper()}IDRef)" \
                "VALUES (?,?,?,?,?,?,?,?,?,TRUE,?)"
    if not execute_query(
                    sql, 
                    (new_task["mode"], new_task["topic"], new_task["category"], new_task["priority"], 
                    new_task["deadlineDate"], new_task["startDate"], new_task["remainingTime"], 
                    new_task["title"], new_task["description"], new_task["modeId"]), 
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

def get_all_open_tasks_user(user_id: int) -> list[dict]:
    """Returns a list containing all tasks in the database"""
    sql: str = "SELECT TaskID, TaskMode, TaskTopic, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription, TaskIsOpen FROM tblTasks WHERE UserIDRef=?"
    results = execute_query(sql, (user_id,), CONNECTIONSTRING, fetch=True)
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

def get_all_open_tasks_team(team_id: int) -> list[dict]:
    """Returns a list containing all tasks in the database"""
    sql: str = "SELECT TaskID, TaskMode, TaskTopic, TaskCategory, TaskPriority, TaskDeadlineDate, TaskStartDate, TaskRemainingTime, TaskTitle, TaskDescription, TaskIsOpen FROM tblTasks WHERE TeamIDRef=?"
    results = execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)
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
