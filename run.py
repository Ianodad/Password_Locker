from user import User
from credi import Credi


def create_new_user(name, second, username, phone, email, password):
    '''
    create new user
    '''
    new_user = User(name, second, username, phone, email, password)
    return new_user


def add_new_user():
    '''
    adding new user to array
    '''

    user.add_user()


def remove_user():
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
    check ti display
    '''

    return Credi.display_accounts()


'''
Encode and decode password
'''


def encode(cls, password):
    '''
    using base64 to encode user password
    '''
    return base64.b64encode(password)


def decode(cls, username):

    return base64.b64decode(password)


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
            print("new User")
            print('*'*10)

            print("First name....")
            name = input()

            print("last name ...")
            second = input()

            while True:

                print("phone number ...")
                username = input()
                if user_exist(username):
                    print("user already exist")
                    break
        break
        # print ("Email address ...")
        # phone = input()

        # print ("email adress ...")
        # email = input()


        # print (" Password ...")
        # password = input()
if __name__ == '__main__':

    main()
