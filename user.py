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
    
    # @classmethod
    # def user_find_(cls, number):
    #     '''
    #     check its username exist
    #     '''
    #     for user in cls.user_list:
    #         if user.phone_number == user:
    #             return user

    

# new_user = User('ian', 'Odhiambo', 'ianodad',
#                 '0712724144', 'ianodad@gmail.com', 'Pytoncode1')



