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
    def find_account_exist(cls, username, password):
        '''
        checks to find password
        '''
        for account in cls.account_list:
            if account.username == username and account.password:
                '''
                condition to check through tthe loop
                '''
                return True
                '''
                if found return true
                '''
        return False

    @classmethod
    def find_account(cls, username, password):
        '''
       returning account 
        '''
        for account in cls.account_list:
            if account.username == username and account.password == password:
                return account

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.account_list
