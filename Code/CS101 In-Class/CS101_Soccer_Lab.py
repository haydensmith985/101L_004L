import csv
player_dict = {} #importing csv and converting into a dictionary by key of jeresy number
file = open("player_info.csv", 'r')
csvreader = csv.reader(file, delimiter = ',')
rows = []
for row in csvreader:
    rows.append(row)
for i in range (0, len(rows)):
    player_dict[rows[i][3]] = rows[i]
    
def roster(): #printing out the roster
    for jeresy in player_dict:
        print(player_dict[jeresy][2], player_dict[jeresy][0], player_dict[jeresy][3], player_dict[jeresy][4])

def player_ranking(): #getting the top number of players in a certain position
    position = input('Enter what position you would like : \n')
    num_of_players = int(input('Enter the number of players you would like to see : \n'))
    sort_player_dict = sorted(player_dict.items(), key=lambda x: int(x[1][4]))
    printed = 0
    for i in sort_player_dict:
        if position == i[1][0] and printed < num_of_players:
            print('Name: ', i[1][2], 'Position: ', i[1][0], 'Jeresy Number: ', i[1][3], 'Ranking: ', i[1][4])
            printed += 1

def update_player_ranking(): #updating a players ranking
    player_num = input('Enter the jeresy number of the player you would like to update : \n')
    new_ranking = (input('Enter the new ranking you would like to assign to that player: \n'))
    if player_num in player_dict:
        player_dict[player_num][4] = new_ranking
    else:
        print('The player you want to update does not exsist.')

def delete_player(): #deleting a player from the roster
    player_num = input('Enter the jeresy number of the player you would like to delete : \n')
    if player_num in player_dict:
        del player_dict[player_num]
    else:
        print('The jeresy number you entered is not valid.\n')

def top_players(): #print out the top players above a min ranking value
    user_ranking = int(input('Enter a minimum ranking : \n'))
    for players in player_dict:
        if int(player_dict[players][4]) >= user_ranking:
            print(player_dict[players][2], player_dict[players][0], player_dict[players][3], player_dict[players][4], '\n\n')

x = 1
while x == 1:
    print('Welcome to the AFC Richmond Player Database!') #printing menu
    print('Please choose: \nR - Roster \nP - Player Ranking by Position \nU - Update a Player\'s ranking \nD - Delete a Player \nT - Top Players \nQ - Quit')
    try:
        user_input = input('Enter your choice : \n') #getting menu choice from user
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
            x == 2 #ending loop (quit)
        else:
            print('\n\nInvalid input. Please try again.')
    except:
        print('\n\nThe input you entered is invalid. Please try again.') #catch-all except for invalid input


