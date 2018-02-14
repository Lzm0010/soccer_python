import csv


def sort_players():
    #team dictionaries
    sharks = {"Name":"Sharks", "Team":[]}
    dragons = {"Name":"Dragons", "Team":[]}
    raptors = {"Name":"Raptors", "Team":[]}

    # upon opening the file
    # create dictionaries of all columns
    # sort the dictionaries of each individual player by the experience column
    with open("soccer_players.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        sorted_players = sorted(reader, key=lambda r: r["Soccer Experience"])

        #append each dictionary to a different team in thirds
        for i, row in enumerate(sorted_players):
            if i % 3 == 0:
                sharks["Team"].append(row)
            elif i % 3 == 1:
                dragons["Team"].append(row)
            elif i % 3 == 2:
                raptors["Team"].append(row)

    return sharks, dragons, raptors

def make_team_list(teams_list):
    #create a team.txt file
    # then loop through teams
    # writing the team name on the first line
    # and then the player, the exp. and the guardians on their own line
    f = open("team.txt", "w+")
    for team in teams_list:
        f.write("{}\n".format(team['Name']))
        for member in team["Team"]:
            f.write("{}, {}, {}\n".format(member['Name'], member['Soccer Experience'], member['Guardian Name(s)']))

    f.close()

def make_player_letters(teams_list):
    #create a separate file for each player
    #write a letter with the players information in the file
    for team in teams_list:
        for member in team["Team"]:
            f = open("{}.txt".format(member['Name'].lower().replace(" ", "_")), "w+")
            f.write("Dear {}, \n Congrats! {} has made the {}! First practice will take place on Wednesday, February 14th at 7:00pm.".format(member['Guardian Name(s)'], member['Name'], team['Name']))
            f.close()


if __name__ == "__main__":
    teams = sort_players()
    make_team_list(teams)
    make_player_letters(teams)
