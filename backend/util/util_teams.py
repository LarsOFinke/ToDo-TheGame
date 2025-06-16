from ..db.db_setup import execute_query, CONNECTIONSTRING

def teams_to_json(teams: list[tuple]) -> list[dict]:
    return  [
                {
                    "id": team[0],
                    "name": team[1],
                    "founder": get_founder_details(team[0])
                }
                
                for team in teams
            ]
    
def get_founder_details(team_id: int) -> int:    
    sql: str = "SELECT UserIDRef FROM tblTeams WHERE TeamID=?"
    founder_id: int = execute_query(sql, (team_id,), CONNECTIONSTRING, fetch=True)[0][0]
    
    sql: str = "SELECT UserUsername FROM tblUsers WHERE UserID=?"
    founder_name: str = execute_query(sql, (founder_id,), CONNECTIONSTRING, fetch=True)[0][0]
    
    return  {
                "id": founder_id, 
                "name": founder_name
            }
