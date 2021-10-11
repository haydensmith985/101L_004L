def encode(shift, string):
    string = string.upper()
    encrypted_string = ''
    for char in string:
        ord_val = ord(char)
        char_pos = ord_val - ord("A")
        new_char_pos = (char_pos + shift) % 26
        new_char = chr(new_char_pos)
        encrypted_string = encrypted_string + new_char
    return encrypted_string

def decode(shift, string):
    string = string.upper()
    decrypted_string = ''
    for char in string:
        ord_val = ord(char)
        char_pos = ord_val - ord("A")
        new_char_pos = (char_pos - shift) % 26
        new_char = chr(new_char_pos)
        decrypted_string = decrypted_string + new_char
    return decrypted_string
def print_menu():
    print('Welcome to the string encoder! Please select an option: ')
    print('A) Encode a string')
    print('B) Decode a string')
    print('C) Quit program')



print_menu()
x = 1
while x == 1:
    menu_selection = input()
    menu_selection = menu_selection.upper()
    if menu_selection == 'A':
        user_string = input('Enter a string to encode : \n')
        user_shift = int(input('Enter a shift value : \n'))
        print(user_string, 'shifted', user_shift, 'characters looks like:')
        print(encode(user_shift, user_string))
    elif menu_selection == 'B':
        user_string = input('Enter a string to encode : \n')
        user_shift = int(input('Enter a shift value : \n'))
        print(user_string, 'shifted', user_shift, 'characters looks like:')
        print(decode(user_shift, user_string))
    elif menu_selection == 'C':
        x = 0
        print('Thank you for using the string encoder! Have a good day.')
    else:
        print('The input given did not match the menu options. Please try again.')
        print_menu()

