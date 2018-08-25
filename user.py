class User:

    def __init__(self, first_name, last_name, username, phone_number: int, email):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.email = email


new_user = User('ian', 'Odhiambo', 'ianodad',
                '0712724144', 'ianodad@gmail.com')

print(new_user.first_name)
