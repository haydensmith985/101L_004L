#Hayden Smith
#CS101L_004
#Crime Data Analyzer
#This program will organize a user-defined file into an assortment of dictionaries as determined by a looping menu
#Program will account for files that do not exsist within given directory
import csv
from collections import Counter #importing required functions

def month_from_number(num):
    '''will return what month is associated with a number 1-12'''
    try:
        months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        print(months[num - 1])
    except ValueError:
        print('Input must be a number between 1-12')
    except IndexError:
        print('Input must be between 1-12')


def read_in_file(input_file_name):
    '''will make a list of all crimes and their data'''
    crime_list = []
    with open(input_file_name, 'r', encoding='utf-8-sig') as csvfile:
        contents = csv.reader(csvfile)
        for i in contents:
            crime_list.append(i)
    del crime_list[0]
    return crime_list

def create_reported_date_dict(input_file_name):
    '''will make a dictionary sorted by the type of crime'''
    reported_offense_dict = {}
    crime_list = read_in_file(input_file_name)
    for crimes in crime_list:
        crime_type = crimes[1]
        if crime_type in reported_offense_dict: #checking to see if type is in dictionary
            reported_offense_dict[crime_type] += 1
        else:
            reported_offense_dict[crime_type] = 1
    return reported_offense_dict


def create_reported_month_dict(input_file_name):
    '''will create a dictionary sorted by the month of the crime'''
    reported_month_dict = {}
    crime_list = read_in_file(input_file_name)
    for crimes in crime_list:
        crime_type = crimes[1]
        a = crime_type.split('/')
        month = a[0] #creating a variable that is specifically the month inside of index 1 of the list
        if month in reported_month_dict:
            reported_month_dict[month] += 1 #checking to see if month is in dictionary
        else:
            reported_month_dict[month] = 1
    return reported_month_dict

def create_offense_dict(input_file_name):
    '''will create a dictionary based on type of crime commited'''
    reported_offense_dict = {}
    crime_list = read_in_file(input_file_name)
    for crimes in crime_list:
        crime_type = crimes[7]
        if crime_type in reported_offense_dict:
            reported_offense_dict[crime_type] += 1 #checking to see if type is in dictionary
        else:
            reported_offense_dict[crime_type] = 1
    return reported_offense_dict

def create_offense_by_zip(input_file_name):
    '''will create a dictionary with key = type and value as a nested dict with key = zip and value = occurances'''
    crime_list = read_in_file(input_file_name)
    crime_type = []
    for crimes in crime_list:
        type = crimes[7]
        if type in crime_type:
            continue
        else:
            crime_type.append(type) #creating a list of types of crime in file
    final = {}

    for crime in crime_list:
        for type in crime_type:
            if crime[7] == type:
                if type in final:
                    final[type].append(crime[13])
                else:
                    final[type] = []
                    final[type].append(crime[13])
            else:
                continue #getting a dictionary of unsorted and unnumbered zip codes

    for types in final:
        zip_count = Counter(final[types])
        final[types] = zip_count #counting the occurences of zip codes as they relate to types of crime
    return final

y = 0 #checking to make sure input file is valid
while y == 0:
    try:
        input_file_name = input('Enter the name of the file you would like to pull data from : \n')
        y = 1
    except FileNotFoundError:
        print('File does not exsist. Try again.')

x = 0
while x == 0: #looping through a menu
    print('Sort by:') #printing menu
    print('Reported Date (A)')
    print('Reported Month (B)')
    print('Offense Type (C)')
    print('Offense by Zip Code (D)')
    print('Quit (Q)')
    choice = input('Enter your choice : \n')
    choice.upper() #determining functions to print in accorance to menu choice
    if choice == 'A':
        print(create_reported_date_dict(input_file_name))
    elif choice == 'B':
        print(create_reported_month_dict(input_file_name))
    elif choice == 'C':
        print(create_offense_dict(input_file_name))
    elif choice == 'D':
        print(create_offense_by_zip(input_file_name))
    elif choice == 'Q':
        print('Have a good day!')
        x == 1
        quit()
    else:
        print('That was not an option. Please try again.')




