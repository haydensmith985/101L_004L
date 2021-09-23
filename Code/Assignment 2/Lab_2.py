########################################################################
##
## CS 101 Lab
## Program Grade Calculator
## Hayden Smith
## hiszx5@umsystems.edu
##
## PROBLEM : Develop a program to calculate a student's final grade while taking different weights into account
##
## ALGORITHM :
##      1. Have user input name and grades w/ attendance
##      2. Calculate grades based off of pre-determined weights
##
## ERROR HANDLING:
##      Automatically change values outside the range of 0 - 100 and update the user
##
## OTHER COMMENTS:
##      Feeling a little extra hungry right now
##
########################################################################

#weight system dictionary
weighting = {'Labs': 0.7, 'Lab_Exams': 0.2, 'Attendance': 0.1}
#welome & input from user
print('Welcome to the grade calculator!\n')
name = input('Who\'s grades are we calculating today?\n')
labs_grade = int(input('Please enter your lab grade :\n'))
exams_grade = int(input('Please enter your exams grade :\n'))
attendance = int(input('Please enter your attendance average :\n'))


#defining weighted grade calculation function
def calc_weighted_grades(labs_perc, exams_perc, attendance_perc):
    grades_list = [labs_perc, exams_perc, attendance_perc]
    for i in grades_list:
        if i > 100:
            i = 100
            print(
                'A value you entered was more than 100. It has been changed to 100\n')
        elif i < 0:
            i = 0
            print(
                'A value you entered was less than 0. It has been changed to 0.\n')
        else:
            break
    final_grade = ((labs_perc * weighting['Labs']) + (exams_perc * weighting['Lab_Exams']) + (attendance_perc * weighting['Attendance']) / 1)
    return final_grade


#calling function to make grade variable global
grade_percentage = calc_weighted_grades(labs_grade, exams_grade, attendance)


#defining function for grade letter
def calc_grade_letter(grade_percent):
    if grade_percent >= 90:
        letter = 'A'
    elif 80 <= grade_percent < 90:
        letter = 'B'
    elif 70 <= grade_percent < 80:
        letter = 'C'
    elif 60 <= grade_percent < 70:
        letter = 'D'
    elif grade_percent < 60:
        letter = 'F'
    return letter


#outputting answers
print(name + '\'s final grade is:', round(grade_percentage, 1))
print('That means you have a(n)', calc_grade_letter(grade_percentage))