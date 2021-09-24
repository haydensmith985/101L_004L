user_char = input('Enter your special character : \n')
user_phrase = input('Enter a phrase : \n')
user_list = user_phrase.split(' ')
for w in user_list:
    if (w.find(user_char) != -1):
        print(w)