#Hayden Smith
#CS101_L
#1 October 2021
#This program simulates a slot machine using user-defined functions
#It will ask the parameters of the bet and then adjust the users 'balance' before running again
#All input is within a certain value range and will be adjusted if input is outside the bounds stated

import random

def play_again(): #asking the user if they would like to continue playing
    while True:
        choice = input('Would you like to play again? (y / n) : \n')
        if choice == 'y' or choice == 'Y':
            return True
            
        if choice == 'n' or choice == 'N':
            return False
        else:
            print('You have entered an invalid value. Please only use characters provided.')

def get_wager(): #entering wager amount
    while True:
        global wager
        wager = int(input('Please enter how many chips you would like to wager : \n'))
        if wager <= 0 or wager > bank['money']:
            print('Your value must be greater than zero and no more than all the current chips you have in the bank.')
        else:
            return wager

def get_slot_results(): #getting random numbers to simulate a slot machine
    global reel1
    global reel2
    global reel3
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    results = [reel1, reel2, reel3]
    print(reel1, reel2, reel3)
    return results

def get_matches(reel1, reel2, reel3): #assessing the reels to count matches
    global matches
    matches = 0
    if reel1 == reel2 and reel2 == reel3:
        matches = 3
    if reel1 == reel2 and reel2 != reel3:
        matches = 2
    if reel2 == reel3 and reel2 != reel1:
        matches = 2
    else:
        matches = 0
    print(matches, 'matches.\n')
    return matches

def get_bank(): #asking user for amount of money they wish to start with
    while True:
        chips = int(input('How many chips would you like to start with? (1 - 100) : \n'))
        if chips < 1 or chips > 100:
            print('You have entered an invalid value. Please only enter a number between 1 and 100.')
        else:
            bank['money'] = chips
            return chips

def get_payout(wager, matches): #calculating payout based off of wager and number of matches
    payout = 0
    if matches == 3:
        payout = (wager * 10) - wager
    if matches == 2:
        payout = (wager * 3) - wager
    if matches == 0:
        payout = 0 - wager
    return payout

bank = {'money' : 0}
print('Welcome to the slot machine!')
get_bank()
while True:
    get_wager()
    get_slot_results()
    get_matches(reel1, reel2, reel3)
    outcome = get_payout(wager, matches)
    bank['money'] += outcome
    print('Current account balance:', bank['money'])
    if bank['money'] > 0:
        if play_again() == False:
            print('Thank you for playing!')
            quit()
        else:
            continue
    else:
        print('You do not have any more money to play with. Thank you for playing!')
        quit()
    

    





