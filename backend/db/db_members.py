from .db_setup import execute_query, CONNECTIONSTRING

def add_new_member(new_member: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblMembers(TeamName, TeamRole, UserIDRef, TeamIDRef) VALUES (?,?,?,?)"
    return execute_query(sql, (new_member.get("teamName"), "member", new_member.get("userId"), int(new_member.get("teamId"))), CONNECTIONSTRING)

def get_members_for_team(team_id: int) -> list[dict]:
    """Returns a list containing all members for a team"""
    members: list = []
    
    sql: str = "SELECT UserIDRef, TeamRole FROM tblMembers WHERE TeamIDRef=?"
    user_ids: list = execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)
    
    for user_id in user_ids:
        sql: str = "SELECT UserUsername FROM tblUsers WHERE UserID=?"
        username = execute_query(sql, (user_id[0],), CONNECTIONSTRING, fetch=True)[0][0] 
        members.append({
            "id": user_id[0],
            "username": username,
            "teamRole": user_id[1],
        })
        
    return members

def get_member_count_for_team(team_id: int) -> int:
    sql: str = "SELECT COUNT(MemberID) FROM tblMembers WHERE TeamIDRef=?"
    return execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)[0][0]
