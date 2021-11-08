#Hayden Smith
#CS101L_004
#This program will take in text and output the top ten words over three characters used
#Program will display number of unique words and the number of words only printed once
#Program makes use of 'Counter' function to create a frequency chart

from collections import Counter #importing function
x = 1
while x == 1:
    try:
        f = input('Enter the name of the file you would like to open: \n') #opening a file
        with open(f, 'r') as text:
            passage = text.read()
            passage = passage.replace('.', '')
            passage = passage.replace('\n', '') #stripping periods and newlines
            words_list = passage.split(' ')
            x = 2
    except FileNotFoundError:
        print('File does not exsist. Try again.')

long_words = [] #creating a list of words over three characters

for words in words_list:
    if len(words) > 3:
        long_words.append(words)

frequency_counter = Counter(long_words) #making a counter dictionary of word frequencies

frequency_dict = {}

for key, value in frequency_counter.items(): #converting counter into dict
    frequency_dict[key] = value

frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)) #sorting dict

num = 1
printed = 0
print('Top ten words used:') #printing out the top ten words
for words, numbers in frequency_dict.items():
    if printed < 10:
        print('#' + str(num) + ':', words)
        print('Number of times used:', numbers) #printing highest used words
        num += 1
        printed += 1
    else:
        continue

unique_words = len(frequency_dict) #figuring out number of words
print_one_words = 0
for words, numbers in frequency_dict.items(): #getting number of words printed once
    if numbers == 1:
        print_one_words += 1
    else:
        continue

print('\nNumber of unique words:', unique_words) #ouput of unique/single printed words
print('\nNumber of words printed once:', print_one_words)