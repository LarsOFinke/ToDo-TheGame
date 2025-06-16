
def teams_to_json(teams):
    return  [
                {
                    "id": team[0],
                    "name": team[1]
                }
                
                for team in teams
            ]
    
    
