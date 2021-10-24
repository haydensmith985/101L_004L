#Hayden Smith
#CS101_L004
#This program will output a use-defined file with a library of cars above
#a given MPG threshhold
#The program will check for errors in integer inputs as well as verifying
#the file names are valid and the files are correctly formatted
#########################################################################


def user_mpg():
    while True:
        try:
            mpg = int(input('Enter minimum combined MPG : \n'))
            if mpg > 100:
                print('MPG must be less than 100.')
            elif mpg <= 0:
                print('MPG must be more than 0. ')
            else:
                return mpg
        except ValueError:
            print('Invalid input--please try again.')

cars_list = []
final_list = []
def input_file():
    while True:
        try:
            file_name = input('Please enter the file you would like to pull information from : \n')
            f = open (file_name, 'r')
            contents = f.readlines()
            for i in range (0, len(contents)):
                l = (contents[i]).split('\t')
                cars_list.append(l)
            for h in range (1, len(cars_list)):
                print(cars_list[h][1], cars_list[h][7])
            print(final_list)
            return True
        except OSError:
            print('Invalid input file--please try again.')

output_file = open ('output.txt', 'w+')
outf = output_file.readlines
for i in range (1, len(final_list)):
    if int(final_list[i][7]) >= mpg:
        output_file.write(final_list[i][0], ' ', final_list[i][1], ' ', final_list[i][2], ' ', final_list[i][7])



mpg = user_mpg()
input_file()
print(outf)


