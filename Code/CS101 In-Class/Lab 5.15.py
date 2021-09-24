user_name = input('Enter your company name : ')
user_acro = ''
for i in user_name:
    if i.isupper():
        user_acro += i
print(user_acro)
