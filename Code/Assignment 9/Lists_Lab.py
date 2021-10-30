#HAYDEN SMITH
#LISTS_LAB
#CS101L_004
#THIS PROGRAM WILL ACT AS A TEACHER GRADE PORTAL
#THE PROGRAM WILL LOOP THROUGH VARIOUS MENU OPTIONS UNTIL THE USER WANTS TO LEAVE
#THE PROGRAM WILL VERIFY EACH INPUT AS BEING VALID BY PUTTING INPUT IN TYPE/AMOUNT BOUNDS

import math

tests = [] #INITIALIZING EMPTY LISTS
programs = []

def add_test(): #ADDING USER TEST SCORES TO THE TEST REGISTERY
    num = 'unknown'
    while num == 'unknown':
        try:
            test_score = int(input('Enter a test score from 1-100 : \n'))
            if test_score < 1 or test_score > 100:
                print('Your test score must be between and including 1 and 100. Please try again. \n')
                continue
            else:
                tests.append(test_score)
                print('Test added. \n')
                num = 'known'
        except ValueError:
            print('Your score must be an integer. Please try again. \n')
            continue

def remove_test(): #REMOVING USER TEST SCORE FROM TEST REGISTRY
    process = 'undone'
    while process == 'undone':
        try:
            test_to_remove = int(input('Enter a test to remove 1-100 : \n'))
            if test_to_remove in tests:
                tests.remove(test_to_remove)
                print('Test removed. \n')
                process = 'done'
            else:
                print('Test score not found. Please try again. \n')
                continue
        except ValueError:
            print('You must enter a test score to remove between 1-100. Please try again. \n')
            continue

def clear_tests(): #CLEAR USER TEST REGISTRY
    verify = input('Are you sure you would like to clear all test data? This action cannot be undone. (Y/N) \n')
    if verify == 'Y' or verify == 'y':
        print('Tests cleared. \n')
        tests.clear()

def add_assignment(): #ADDING USER TEST SCORES TO THE TEST REGISTERY
    num = 'unknown'
    while num == 'unknown':
        try:
            assignment_score = int(input('Enter an assignment score from 1-100 : \n'))
            if assignment_score < 1 or assignment_score > 100:
                print('Your assignment score must be between and including 1 and 100. Please try again. \n')
                continue
            else:
                programs.append(assignment_score)
                num = 'known'
                print('Assignment added. \n')
        except ValueError:
            print('Your score must be an integer. Please try again. \n')
            continue

def remove_assignment(): #REMOVING USER PROGRAM SCORE FROM TEST REGISTRY
    process = 'undone'
    while process == 'undone':
        try:
            assignment_to_remove = int(input('Enter an assignment to remove 1-100 : \n'))
            if assignment_to_remove in tests:
                programs.remove(assignment_to_remove)
                print('Assignment removed. \n')
                process = 'done'
            else:
                print('Assignment score not found. Please try again. \n')
                continue
        except ValueError:
            print('You must enter an assignment score to remove between 1-100. Please try again. \n')
            continue

def clear_assignments(): #CLEAR USER PROGRAM REGISTRY
    verify = input('Are you sure you would like to clear all assignment data? This action cannot be undone. (Y/N) \n')
    if verify == 'Y' or verify == 'y':
        programs.clear()
        print('Assignments cleared. \n')

def print_scores():
    tests_num = len(tests) + 1 #GETTING GENERAL STATS
    assignments_num = len(programs) + 1
    tests_min = min(tests)
    assignments_min = min(programs)
    tests_max = max(tests)
    assignments_max = max(programs)
    tests_average = sum(tests) / (len(tests) + 1) #FINDING AVERAGES
    assignments_average = (sum(programs) / (len(programs) + 1))
    tests_sum = 0
    for scores in tests:
        tests_sum += math.pow((scores - tests_average), 2)
    tests_sd = (math.sqrt((tests_sum / (len(tests) + 1)))) #CALCULATING STDS
    assignments_sum = 0
    for scores in programs:
        assignments_sum += math.pow((scores - assignments_average), 2)
    assignments_sd = math.sqrt((assignments_sum / (len(programs) + 1)))
    ta_round = round(tests_average, 2)
    tsd_round = round(tests_sd, 2)
    aa_round = round(assignments_average, 2) #FORMATTING STATS AND ROUNDING
    asd_round = round(assignments_sd, 2)
    print('\n') #PRINTING OUT STATS
    print('Tests       ||  Number:', tests_num, '  Min:', tests_min, '  Max:', tests_max, '  Avg:', ta_round, '  Std:', tsd_round)
    print('Assignments ||  Number:', assignments_num, '  Min:', assignments_min, '  Max:', assignments_max, '  Avg:', aa_round, '  Std:', asd_round)
    print('\n')


answer = 'void'
while answer != 'Q' or answer != 'q': #MENU LOOP
    print('Teacher Grade Portal') #PRINTING MENUS
    print('1) Add Test')
    print('2) Remove Test')
    print('3) Clear Tests')
    print('4) Add Assignment')
    print('5) Remove Assignment')
    print('6) Clear Assignments')
    print('7) Print Scores')
    print('Q) Quit')
    answer = input('Please choose from the options above : \n')
    if answer == '1':
        add_test()
    if answer == '2':
        remove_test()
    if answer == '3':
        clear_tests()
    if answer == '4':
        add_assignment()
    if answer == '5':
        remove_assignment()
    if answer == '6':
        clear_assignments()
    if answer == '7':
        print_scores()
    if answer == 'Q' or answer == 'q':
        print('Exiting program--have a good day.')
        quit()


