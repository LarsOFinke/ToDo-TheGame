from .db_setup import execute_query, CONNECTIONSTRING

def add_new_team(new_team: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    team_name = new_team.get("teamName")
    user_id = int(new_team.get("userId"))
    
    # Create new Team in tblTeams #
    sql: str = "INSERT INTO tblTeams(TeamName, UserIDRef) VALUES (?,?)"
    if not execute_query(sql, (team_name, user_id), CONNECTIONSTRING):
        return False
    
    # Create owner-entry in tblMembers #
    team_id = get_team_id(team_name)
    sql: str = "INSERT INTO tblMembers(TeamName, UserIDRef, TeamIDRef) VALUES (?,?,?)"
    return execute_query(sql, (team_name, user_id, team_id), CONNECTIONSTRING)

def get_team_id(team_name: str) -> int:
    sql: str = "SELECT TeamID FROM tblTeams WHERE TeamName=?"
    return execute_query(sql, (team_name,), CONNECTIONSTRING, fetch=True)[0][0]

def get_all_teams_not_joined(user_id: int) -> list[dict]:
    """
    Returns a list containing all joinable teams for a user in the database. 
    Return an empty list if no available.
    """
    sql: str = "SELECT DISTINCT TeamIDRef, TeamName FROM tblMembers WHERE TeamIDRef NOT IN (SELECT TeamIDRef FROM tblMembers WHERE UserIDRef = ?)"
    results = execute_query(sql, (user_id,), CONNECTIONSTRING, fetch=True)
    try:
        teams: list =   [
                            {
                                "id": team[0],
                                "name": team[1]
                            }
                            for team in results
                        ]
    except:
        return []
    
    return teams

def get_teams_by_user(user_id: int) -> list[dict]:
    """Returns a list containing all teams for a user in the database"""
    sql: str = "SELECT TeamIDRef, TeamName FROM tblMembers WHERE UserIDRef=?"
    results = execute_query(sql, (user_id,), CONNECTIONSTRING, fetch=True)
    teams: list =   [
                        {
                            "id": team[0],
                            "name": team[1]
                        }
                        for team in results
                    ]
    
    return teams
