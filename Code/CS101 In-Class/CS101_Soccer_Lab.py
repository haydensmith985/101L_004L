import csv
player_dict = {} #importing csv and converting into a dictionary by key of jeresy number
file = open("player_info.csv", 'r')
csvreader = csv.reader(file, delimiter = ',')
rows = []
for row in csvreader:
    rows.append(row)
for i in range (1, len(rows)):
    player_dict[rows[i][3]] = rows[i]


def roster(): #printing out the roster
    for key in player_dict.keys():
        value = player_dict[key]
        print(value[2], '     ', key, '     ', value[3])

def player_ranking(): #getting the top number of players in a certain position
    position = input('Enter what position you would like : \n')
    num_of_players = int(input('Enter the number of players you would like to see : \n'))
    look = 1
    printed = 0
    while printed < num_of_players:
        for players in player_dict:
            if int(player_dict[players][4]) == look and player_dict[players][0] == position:
                print(players[players])
                printed +=1
                look += 1
            else:
                look +=1

def update_player_ranking():
    player_num = input('Enter the jeresy number of the player you would like to update : \n')
    new_ranking = (input('Enter the new ranking you would like to assign to that player'))
    if player_num in player_dict:
        player_dict[player_num][4] = new_ranking
    else:
        print('The player you want to update does not exsist.')

def delete_player():
    player_num = input('Enter the jeresy number of the player you would like to delete : \n')
    if player_num in player_dict:
        del player_dict[player_num]
    else:
        print('The jeresy number you entered is not valid.')

def top_players():
    user_ranking = int(input('Enter a minimum ranking : \n'))
    for players in player_dict:
        if int(player_dict[players][4]) >= user_ranking:
            print(player_dict[players])

x = 1
while x == 1:
    print('Welcome to the AFC Richmond Player Database!')
    print('Please choose: \nR - Roster \nP - Player Ranking by Position \nU - Update a Player\'s ranking \nD - Delete a Player \nT - Top Players \nQ - Quit')
    try:
        user_input = input('Enter your choice : \n')
        if user_input == 'R' or user_input == 'r':
            roster()
        elif user_input == 'P' or user_input == 'p':
            player_ranking()
        elif user_input == 'U' or user_input == 'u':
            update_player_ranking()
        elif user_input == 'D' or user_input == 'd':
            delete_player()
        elif user_input == 'T' or user_input == 't':
            top_players()
        elif user_input == 'Q' or user_input == 'q':
            x == 2
        else:
            print('\n\nInvalid input. Please try again.')
    except:
        print('\n\nThe input you entered is invalid. Please try again.')


