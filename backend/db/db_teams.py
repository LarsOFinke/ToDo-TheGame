from .db_setup import execute_query, CONNECTIONSTRING

def add_new_team(new_team: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    team_name = new_team.get("teamName")
    user_id = int(new_team.get("userId"))
    
    sql: str = "INSERT INTO tblTeams(TeamName, UserIDRef) VALUES (?,?)"
    if not execute_query(sql, (team_name, user_id), CONNECTIONSTRING):
        return False
    
    sql: str = "SELECT TeamID FROM tblTeams WHERE TeamName=?"
    team_id = execute_query(sql, (team_name,), CONNECTIONSTRING, fetch=True)[0][0]
    if not team_id:
        return False
    
    sql: str = "INSERT INTO tblMembers(TeamName, UserIDRef, TeamIDRef) VALUES (?,?,?)"
    return execute_query(sql, (team_name, user_id, team_id), CONNECTIONSTRING)
        

def get_teams_by_user(team_id: int) -> list[dict]:
    """Returns a list containing all teams for a user in the database"""
    sql: str = "SELECT TeamIDRef, TeamName FROM tblMembers WHERE UserIDRef=?"
    results = execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)
    teams: list =   [
                        {
                            "id": team[0],
                            "name": team[1]
                        }
                        for team in results
                    ]
    
    return teams
