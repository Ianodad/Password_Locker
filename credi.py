class Credi:

    account_list = []

    def __init__(self, account, username, password):

        self.account = account
        self.username = username
        self.password = password

    def add_account(self):
        '''
        add new user
        '''
        Credi.account_list.append(self)

    def delete_account(self):

        Credi.account_list.remove(self)

    @classmethod
    def find_account_exist(cls, username):
        '''
        checks to find password
        '''
        for account in cls.account_list:
            if account.username == username:
                '''
                condition to check through tthe loop
                '''
                return True
                '''
                if found return true
                '''
        return False

    @classmethod
    def find_account(cls, username):
        '''
       returning account 
        '''
        for account in cls.account_list:
            if account.username == username:
                return account
