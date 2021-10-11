#Hayden Smith
#Lab_06
#CS_101L_004
#7_October_2021
#This program will verify a 10-digit alpha-numeric code assigned to a student for a library card
#The code will denote the students area of study and seniority
#The code will check for proper input length and other formatting characteristics
#The code will first verify the input is properlly formatted, then check to see if the input is valid and what it means

import string #importing modules

def get_length(card_num): #validate length of input
    if len(card_num) == 10:
        return True
    else:
        print('Error: Card lenth not 10')
        return False

def get_first_five(card_num): #first portion is A-Z
    string = card_num[0 : 4]
    if string.isalpha() == True:
        return True
    else:
        print('Error: First 5 digits of card must be A-Z')
        return False

def get_index_five(card_num): #possible school input
    card_list = list(card_num)
    if card_list[5] != '1' and card_list[4] != '2' and card_list[4] != '3':
        print('Error: 6th digit must be 1, 2, or 3.')
        return False
    else:
        return True

def get_index_six(card_num): #possible grade input
    card_list = list(card_num)
    if card_list[6] != '1' and card_list[6] != '2' and card_list[6] != '3' and card_list[6] != '4':
        print('Error: 7th digit must be 1-4.')
        return False
    else:
        return True

def get_index_rest(card_num): #validate rest of card num
    check = card_num[7:10]
    if check.isdigit() == True:
        return True
    else:
        print('Error: Last three digits must be 0-9.')
        return False

def get_school(card_num): #determine school type
    if card_num[5] == '1':
        school = 'School of Computing and Engineering SCE'
    elif card_num[5] == '2':
        school = 'School of Law'
    else:
        school = 'College of Arts and Sciences'
    return school

def get_grade(card_num): #determine grade
    if card_num[6] == '1':
        grade = 'Freshman'
    elif card_num[6] == '2':
        grade = 'Sophomore'
    elif card_num[6] == '3':
        grade = 'Junior'
    else:
        grade = 'Senior'
    return grade

def get_check_digit(card_num): #find check digit
    check_digit = 0
    cardlist = list(card_num)
    for i in range (0, 5):
        check_digit += string.ascii_uppercase.index(cardlist[i]) * (i + 1)
    for i in range (5, 9):
        check_digit += int(cardlist[i]) * (i + 1)
    check_digit = (check_digit % 10) - 0 
    return check_digit

def check_digit_check(card_num): #match check digit to card num
    val1 = int(card_num[9])
    val2 = get_check_digit(card_num)
    if val1 == val2:
        return True
    else:
        print('Error: Invalid check digit.')
        return False

card_num = input('Enter a library card number : ') #input
x = 1
while x == 1: #loop for valid input and output results if working
    if get_length(card_num) == True:
        g = 0
    else:
        card_num = input('Enter your library card number : ')
        continue
    if get_first_five(card_num) == True:
        g = 0
    else:
        card_num = input('Enter your library card number : ')
        continue
    if get_index_five(card_num) == True:
        g = 0
    else:
        card_num = input('Enter your library card number : ')
        continue
    if get_index_six(card_num) == True:
        g = 0
    else:
        card_num = input('Enter your library card number : ')
        continue
    if get_index_rest(card_num) == True:
        g = 0
    else:
        card_num = input('Enter your library card number : ')
        continue
    if check_digit_check(card_num) == True:
        x = 0
        print('Library card valid.')
        print('Student is a', get_school(card_num), 'student and a', get_grade(card_num), '.')
    else:
        card_num = input('Enter your library card number : ')


        




