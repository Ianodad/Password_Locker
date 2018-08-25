'''
we begin by import unittest and User form user.py
'''
import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        '''
        set up method
        '''
        self.new_user = User('ian', 'Odhiambo', 'ianodad', '0712724144', 'ianodad@gmail.com', 'Pythoncode1')

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        intiating test for users

        '''
        self.assertEqual(self.new_user.first_name, "ian")
        self.assertEqual(self.new_user.last_name, "Odhiambo")
        self.assertEqual(self.new_user.username, "ianodad")
        self.assertEqual(self.new_user.phone_number, "0712724144")
        self.assertEqual(self.new_user.email, "ianodad@gmail.com")
        self.assertEqual(self.new_user.password, "Pythoncode1")
    
    def test_add_user(self):
        '''
        test_add test case for adding new conatcts
        '''
        self.new_user.add_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
            '''
            test_save_multiple_user to save multiple contacts
            '''
            self.new_user.add_user()
            new_user_test = User('John', 'Doe', 'johndoe', '0712000000', 'johndoe@gmail.com', 'johndoe254')
            new_user_test.add_user()
            self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()
