import base64


class User:

    user_list = []

    def __init__(self, first_name, last_name, username, phone_number, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def add_user(self):
        '''
        add new user

        '''
        User.user_list.append(self)

    def delete_user(self):

        User.user_list.remove(self)

    def decode_Password(self):
        self.password = base64.b64decode(self.password)

    @classmethod
    def find_user_exist(cls, username):
        '''
        checks to find if user exsist in array
        '''
        for user in cls.user_list:
            if user.username == username:
                '''
                condition to check through tthe loop
                '''
                return True
                '''
                if found return true
                '''
        return False

    @classmethod
    def find_username(cls, username):
        '''
        check its username exist trough 
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def display_user(cls):
        '''
        method that returns user info
        '''
        return cls.user_list

    @classmethod
    '''
    using base64 to encode user password
    '''
    
    def encode(cls, username):
      for user in cls.user_list:
        if user.username == username:
          user.password = base64.b64encode(user.password)
          return(user.password)
