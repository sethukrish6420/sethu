import re
import csv

email_rules = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pwd_rules = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')


def check_mail(email):
    if re.fullmatch(email_rules, email):
      return True
    else:
      return False

def check_pwd(pwd):
    if len(pwd) < 16 and len(pwd) > 5 and re.fullmatch(pwd_rules, pwd):
      return True
    else:
      return False

def register():
    print('\nRegister New User\n')
    email = input('email id: ')
    if check_mail(email):
        password = input('password: ')
        if check_pwd(password):
            write_file(email, password)
            print('\nUser Registered Successfully')
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Username, Please Try Again...')

    

def login():
    email = input('email id: ')
    auth  = False
    if check_mail(email):
        password = input('password: ')
        if check_pwd(password):
            if search_file(email, password):
                print ('\nUser Logged In Successfully...')
            else:
                print('\nUser Not Found !!!')
                register()
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Username, Please Try Again...')

def forget_pwd():
    email = input('email id: ')
    if check_mail(email):
        if search_pwd(email):
            print ('\nUser Logged In Successfully...')
        else:
            print('\nUser Not Found !!!')
            register()
    else:
        print('\nInvalid Username, Please Try Again...')

def search_file(email, pwd , mode = 'r', encoding = 'UTF8', newline = ''):
    with open('sethu.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0] and pwd == row[1]:
                return True
        return False

def search_pwd(email, mode = 'r', encoding = 'UTF8', newline = ''):
    with open('sethu.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0]:
                print('\nPassword for '+ email + ' is '+ row[1])
                return True
        return False
        

def write_file(email, pwd , mode = 'a', encoding = 'UTF8', newline = ''):
    with open('sethu.csv', mode, encoding = encoding, newline = newline) as f:
        writer = csv.writer(f)
        writer.writerow([email, pwd])

if __name__ == "__main__":
   
    try:
        while True:
            print(''' \nPlease select an option \n
                1. Register
                2. Login
                3. Forget Password
                ''')
            option = int(input())
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forget_pwd()
            else:
                print("Invalid Option")
    except:
        print("An exception occurred")
