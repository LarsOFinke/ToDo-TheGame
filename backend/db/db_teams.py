from .db_setup import execute_query, CONNECTIONSTRING

def add_new_team(new_team: dict) -> bool:
    """
    Returns:
        True: if successfully added
        False: if error happened
    """
    sql: str = "INSERT INTO tblTeams(TeamName, UserIDRef) VALUES (?,?)"
    return execute_query(sql, (new_team.get("teamName"), int(new_team.get("userId"))), CONNECTIONSTRING)

def get_teams_by_user(team_id: int) -> list[dict]:
    """Returns a list containing all teams for a user in the database"""
    sql: str = "SELECT TeamID, TeamName FROM tblTeams WHERE UserIDRef=?"
    results = execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)
    teams: list =   [
                        {
                            "id": team[0],
                            "name": team[1]
                        }
                        for team in results
                    ]
    
    return teams
