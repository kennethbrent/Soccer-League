import csv
if __name__ == "__main__": 
    sharks = []
    dragons = []
    raptors = []
    experienced_players = []
    unexperienced_players = []
    with open('soccer_players.csv', newline='') as csvfile, open('teams.txt', 'w') as txtfile:
        reader = csv.reader(csvfile, delimiter=",")
        rows = list(reader)
        for row in rows[0::]:
            if row[2] == "YES":
                experienced_players.append(row)
            elif row[2] == "NO":
                unexperienced_players.append(row)

        # allocate players to teams
        def allocate_players(teamOne,teamTwo,teamThree,list,count):
            for player in list:
                if len(teamOne) < count:
                    teamOne.append(player)
                elif len(teamOne) >= count and len(teamTwo) < count:
                    teamTwo.append(player)
                elif len(teamTwo) >= count and len(teamThree) < count:
                    teamThree.append(player)

        #function to format and write teams to txt file
        def write_teams_to_file(teamName, team):
            txtfile.write("\n")
            txtfile.write(teamName + "\n")
            txtfile.write("===========" + "\n")
            for player in team:
                txtfile.write(player[0] + ", ")
                txtfile.write(player[2] + ", ")
                txtfile.write(player[3] + "\n")


        #use allocate players function to assign experienced players to a team
        allocate_players(sharks,dragons,raptors,experienced_players,3)
        #use allocate players function to assign unexperienced players to a team
        allocate_players(sharks,dragons,raptors,unexperienced_players,6)
        write_teams_to_file("Sharks",sharks)
        write_teams_to_file("Dragons",dragons)
        write_teams_to_file("Raptors", raptors)
