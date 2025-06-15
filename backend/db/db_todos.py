from .db_setup import execute_query, CONNECTIONSTRING

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
    results = execute_query (sql, (task_id,), CONNECTIONSTRING, fetch=True)
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

def close_todo(todo_id):
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "UPDATE tblTodos SET TodoIsOpen=0 WHERE TodoID=?"
    return execute_query(sql, (todo_id,), CONNECTIONSTRING)

def open_todo(todo_id):
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "UPDATE tblTodos SET TodoIsOpen=1 WHERE TodoID=?"
    return execute_query(sql, (todo_id,), CONNECTIONSTRING)
