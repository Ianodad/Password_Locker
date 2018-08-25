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
    

# new_user = User('ian', 'Odhiambo', 'ianodad',
#                 '0712724144', 'ianodad@gmail.com', 'Pytoncode1')



