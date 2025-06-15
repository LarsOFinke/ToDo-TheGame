from .db_setup import execute_query, CONNECTIONSTRING, generate_password_hash, check_password_hash

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
    results = execute_query(sql, (), CONNECTIONSTRING, fetch=True)
    usernames: list = [user[0] for user in results]
        
    return usernames

def get_user_id(username) -> int:
    """Returns the user id from the database"""
    sql: str = "SELECT UserID FROM tblUsers WHERE UserUsername = ?"
    result = execute_query(sql, (username,), CONNECTIONSTRING, fetch=True)
    user_id = result[0][0]
        
    return user_id
