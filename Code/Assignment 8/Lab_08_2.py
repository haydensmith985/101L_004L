x = 1
while x == 1:
    try:
        user_mpg = int(input('Enter a minimum MPG : \n'))
        if user_mpg <= 0:
            print('Invalid input, MPG must be greater than zero.')
        elif user_mpg > 100:
            print('Invalid input-- MPG must be no more than 100.')
        else:
            x = 0
    except TypeError:
        print('Invalid input--please enter a number between 1 and 100.')

y = 1
while y == 1:
    try:
        input_file_name = input('Enter a file to pull information from : \n')
        input_file = open(input_file_name, 'r')
        y = 0
    except OSError:
        print('The file name you entered is invalid--please try again.')

cars_table = []

file_contents = input_file.readlines()

for i in range (0, len(file_contents)):
    line = (file_contents[i]).split('\t')
    cars_table.append(line)

output = open('output.txt', 'w')

for c in range (1, len(cars_table)):
    if int(cars_table[c][7]) >= user_mpg:
        output.write(cars_table[c][0])
        output.write(cars_table[c][1])
        output.write(cars_table[c][2])
        output.write(cars_table[c][7])


