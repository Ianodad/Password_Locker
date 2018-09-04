from user import User
from credi import Credi
import base64
import secrets
import string


def create_new_user(name, second, username, phone, email, password):
    '''
    create new user
    '''
    new_user = User(name, second, username, phone, email, password)
    return new_user


def add_new_user(user):
    '''
    adding new user to array
    '''

    user.add_user()


def remove_user(user):
    '''
    delete new user info
    '''
    user.delete_user()


def user_exist(username):
    '''
    check account exist
    '''
    return User.find_user_exist(username)


def find_User(username):
    '''
    locate user in array
    '''
    return User.find_username(username)


def dispaly_users():
    '''
    check to dislpay users
    '''
    return User.display_user()


def check_validation(username, password):

    return User.check_password(username, password)


'''
METHOD FOR CALLING CREDINTIALS
'''


def create_new_account(account, username, password):
    '''
    create new account
    '''
    new_account = Credi(account, username, password)
    return new_account


def add_account():
    '''
    add account to list of others
    '''

    credi.add_account()


def remove_account():
    '''
    delete account from accounts
    '''
    credi.delete_account()


def account_exist():
    '''
    loop throuh list to check account already there
    '''
    return Credi.find_account_exist()


def find_account():
    '''
    check if account and return
    '''

    return Credi.find_account()


def display_account_info():
    '''
    check the display
    '''

    return Credi.display_accounts()


def gen_password():
    alphabet = string.ascii_letters + string.digits
    passw = ''.join(secrets.choice(alphabet) for i in range(20))

    return passw


'''
Encode and decode password
'''


def encode(password):
    '''
    using base64 to encode user password
    '''
    return base64.urlsafe_b64encode(password.encode('UTF-8')).decode('ascii')


def decode(password):

    return base64.b64decode(b'password')


'''
SHOW THE RUN
'''


def main():
    print('_'*50)
    print(' '*50)
    print(' '*10 + 'WELCOME TO PASSWORD LOCKER')
    print(' '*50)
    print('='*50)

    # print("whats your name?")

    # user_name = input()

    # print(f"Where would you like to begin? {user_name}")

    while True:
        print('-'*50)
        print("create new user: nc")
        print('-'*50)
        print("login user: lu")
        print('-'*50)

        codeform = input().lower()

        if codeform == 'nc':
            print("new User forms")
            print('~'*20)

            print("First name....")
            name = input()
            print('~'*20)

            print("last name ...")
            second = input()
            print('~'*20)

            print("user name ...")
            username = input()
            print('~'*20)

            print("phone ....")
            phone = input()
            print('~'*20)

            print("email ... ")
            email = input()
            print('~'*20)

            print("password ..")
            password = str(input())
            password = encode(password)

            print('checking authetication ...')
            if user_exist(username):
                print('l')
                continue
            else:
                print("succeful added")

            add_new_user(create_new_user(
                name, second, username, phone, email, password))
            print(f"New Use added {name} {second} created")

            print('\n')

        elif codeform == 'lu':

            print('Enter user name')
            user = input()

            if user_exist(user):
                continue
            else:
                print("whats next")

            print('Please enter password')
            password = input()
            password = decode(password)

            if check_validation(user, password):
                print("auth ready go")
                print("welcome to the where do you want to start")

                while True:
                    print('-'*50)
                    print("create new account: ca")
                    print('-'*50)
                    print("check account details: cd")
                    print('-'*50)

                    acode = input()

                    if acode == 'ca':
                        print("next time")

                    else:
                        print("I really didn't get that. Please use the short codes")
            else:
                continue

                #     while True:

                # break
                # print ("Email address ...")
                # phone = input()

                # print ("email adress ...")
                # email = input()

                # print (" Password ...")
                # password = input()


if __name__ == '__main__':

    main()
