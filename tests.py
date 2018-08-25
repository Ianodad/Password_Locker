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
        test_add test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.add_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
