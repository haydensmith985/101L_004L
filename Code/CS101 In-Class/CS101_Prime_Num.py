#Hayden Smith
#CS101
#Sept 24 2021
repeat = True
while repeat == True:
    def menu(): #defining function for printing the menu options
        print('{:^40}'.format('Welcome to the Prime Number Calculator'))
        print('{:^40}'.format('Please chose from the options below:'))
        print('{:^40}'.format('a) Is my number prime?'))
        print('{:^40}'.format('b) Print all prime numbers less than / equal to my number.'))
        print('{:^40}'.format('c) Print the two prime numbers that add up to my number.'))
        print('{:^40}'.format('d) Quit by pressing q'))
    def check_prime(user_num): #defning a function to test if a given number is prime
        prime = True
        for i in range (2 , user_num):
            if user_num % i == 0:
                prime = False
                break
        return prime
    def prime_less_than(user_num): #defining a function to find all prime numbers less than user number
        less_than_prime_string = ''
        for i in range(2, user_num):
            is_prime = True
            is_prime = check_prime(i) #calling the check_prime function
            if is_prime == True:
                less_than_prime_string += str(i)
                less_than_prime_string += ' '
        print(less_than_prime_string)
    def prime_num_sum(user_num): #defning a function to find all combinations of numbers that add to a given number
        while user_num % 2 != 0:
            user_num = input('{:^30}'.format('You will need to enter an even number: '))
        prime_lib_low = []
        prime_lib_high = []
        for i in range (2, user_num // 2):
            prime = check_prime(i)
            if prime == True:
                prime_lib_low.append(i)
        for i in range (user_num // 2, user_num):
            prime = check_prime(i)
            if prime == True:
                prime_lib_high.append(i)
        for i in prime_lib_low:
            for j in prime_lib_high:
                added_num = i + j
                if added_num == user_num:
                    print('{} + {} = {}'.format(i, j, user_num))
    menu() #calling menu function
    choice = input() #getting user choice
    if choice == 'q' or choice == 'Q': #getting menu choice and calling according functions
        print('Thank you for playing!')
        quit()
    user_num = int(input('Enter your number : \n')) #getting user input
    if choice == 'a' or choice == 'A':
        print(check_prime(user_num))
    if choice == 'b' or choice == 'B':
        print(prime_less_than(user_num))
    if choice == 'c' or choice == 'C':
        prime_num_sum(user_num)
    rep = input('Would you like to play again? (Y / N)')
    if rep != 'y' and rep != 'Y':
        quit()
    
