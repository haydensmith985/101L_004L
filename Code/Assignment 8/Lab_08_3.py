#Hayden Smith
#October 22 2021
#CS101_L004
#
#This is the third version of the program--this version will utilize a csv reader to break apart data more effifciently
#
#This program will ask the user for a predefined MPG value that will be checked across every line of a user defined file
#The program will sort the cars that meet the criteria and display them as well as creating a new file to store the data
#
#This program will handle errors in mainly try and except blocks, but also with value type changes to ensure proper use in code

import csv #importing csv file library to use for vehicle files

t = 1
while t == 1:
    try:
        user_mpg = int(input('Please enter a minimum MPG : \n')) #getting MPG value from the user
        if user_mpg <= 0:
            print('The MPG entered must be greater than zero.') #handling values outside of bounds
        elif user_mpg > 100:
            print('The MPG entered must be no more than 100.')
        else:
            t = 2 #breaking out of loop
    except ValueError:
        print('The input enteted is not a number. Please try again.') #handling input that is not an integer

x = 0
while x == 0:
    try:
        holder_list = [] #creating a holder list to append new sorted info into
        f = input('Please enter the file name which you would like to pull information from : \n')
        with open(f, 'r') as car_table:
            table = csv.reader(car_table, delimiter = '\t') #opening the user file as a csv to split data into usable chunks
            for element in table:
                holder_list.append(element) #appending nested list elements into holder list
    except OSError:
        print('User input file is invalid:', f) #handling errors in file naming
    except FileNotFoundError:
        print(f, 'does not exsist.')
    try:
        f2 = input('Please enter the file name in which you would like to store your data : \n')
        holder_list_2 = [] #creating another holder list to write final information into
        with open(f2, 'w') as output_table:
            for i in holder_list[1:]:
                if int(i[7]) >= user_mpg: #checking to make sure a row of information is within the limits of the user
                    holder_list_2.append(i)
                for row in holder_list_2:
                    year = row[0] #defining the important parts of each car
                    make = row[1]
                    model = row[2]
                    mpg = row[7]
                    print('{:<5}{:<20}{:<40}{}'.format(str(year), make, model, str(mpg))) #formatting output
                    output_table.write(('{:<5}{:<20}{:<40}{}'.format(str(year), make, model, str(mpg)))) #formatting file data
                x = 1
    except FileNotFoundError:
        print(f2, 'could not be made.') #error handling in picking a new file to write to
    except OSError:
        print('The output file entered was invalid. Please try again.')





        