#Hayden Smith
#CS101L_004 Cypher Lab
#This lab will ask the user for a string to encrypt/decrypt and a shift amount
#The program will convert the string into its unicode position and increase/decrease its position based on the shift value
#The program will create a new string with the new shifted characters and output the result
#The program will only accept value answers for the menu choice
#The program will only accept valid input for a string

def encrypt(text, shift): #encryption function
    text.upper()
    final = ''
    for c in text:
        c_ascii = ord(c)
        c_place = c_ascii - ord('A')
        c_place_new = (c_place + shift) % 26
        new_ascii = c_place_new + ord('A')
        c_final = chr(new_ascii)
        final += c_final
    return final

def decrypt(text, shift): #decryption function
    text.upper()
    final = ''
    for c in text:
        c_ascii = ord(c)
        c_place = c_ascii - ord('A')
        c_place_new = (c_place - shift) % 26
        new_ascii = c_place_new + ord('A')
        c_final = chr(new_ascii)
        final += c_final
    return final

def print_menu(): #menu print function
    print('Welcome to the string encryptor!')
    print('Please choose from the following options:')
    print('A) Encrypt a string')
    print('B) Decrypt a string')
    print('C) Quit')

x = 1
while x == 1: #Functional code loop
    print_menu()
    user_choice = input('Selection : ')
    if user_choice == 'a' or user_choice == 'A':
        text = input('Enter a string to encrypt : \n')
        shift = int(input('Enter a shift amount : \n'))
        print('Encrypted string:', encrypt(text, shift), '\n\n')
    elif user_choice == 'b' or user_choice == 'B':
        text = input('Enter a string to decrypt : \n')
        shift = int(input('Enter a shift amount : \n'))
        print('Decrypted string:', decrypt(text, shift), '\n\n')
    elif user_choice == 'c' or user_choice == 'C':
        print('Thank you. Have a nice day!')
        x = 0
    else:
        print('Your selection is not valid. Please try again.\n\n')
        continue