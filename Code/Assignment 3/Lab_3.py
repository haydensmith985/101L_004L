####################################################################
# Hayden Smith
# CS101L_004
# Lab 3
# Sept 22 2021
#
# This program will guess a user's number (between 1-100) by asking
# the user the remainder of the equation when the user divides their
# number by certain values
#
# This program will utilize many types of nested / surface-level
# for and while loops
####################################################################
print(
    '\nWelcome to the number guesser!\n'
    'PLease think of a number between and including 1 - 100'
)
repeat_game = 'Y'
while repeat_game == 'y' or repeat_game == 'Y':
    user_3_remainder = int(input('What is the remainder of your number divided by three? : \n'))
    if user_3_remainder != 0 and user_3_remainder != 1 and user_3_remainder != 2: #validating user input
        print('Invalid input...')
        user_3_remainder = int(input('Please enter a valid remainder : \n'))
    user_5_remainder = int(input('What is the remainder of your number divided by five? : \n'))
    user_7_remainder = int(input('What is the remainder of your number divided by seven? : \n'))
    while user_5_remainder == user_7_remainder:
        user_5_remainder = int(input('Your remainders for 5 and 7 cannot be the same. What is the remainder of your number / 5? : \n'))
        user_7_remainder = int(input('What is the remainder of your number / 7? : \n'))
    for i in range(0 , 101): #computing the number using a for loop running through all numbers 1-100
        r3 = False
        r5 = False
        r7 = False
        if i % 3 == user_3_remainder:
            r3 = True
        if i % 5 == user_5_remainder:
            r5 = True
        if i % 7 == user_7_remainder:
            r7 = True
        if r3 and r5 and r7: #checking to make sure the remainders line up with number
            print('Your number is:', i) #giving user their number
            print('Now that *is* impressive, right?')
            break
    repeat_game = input('Would you like to play again? (y/n) : \n') #looping code if user wants to play again
    if repeat_game != 'y' and repeat_game != 'Y':
        quit()





        
