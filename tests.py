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


    def test_delete_contact(self):
        ''' 
        This here is the to test is we can remove obbejct from list
        '''
        self.new_user.add_user()
        new_user_test = User('John', 'Doe', 'johndoe', '0712000000', 'johndoe@gmail.com', 'johndoe254')
        new_user_test.add_user()
        self.new_user.delete_user()  # Deleting obeject of the new user
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_exist(self):

        self.new_user.add_user()
        new_user_test = User('John', 'Doe', 'johndoe', '0712000000', 'johndoe@gmail.com', 'johndoe254')
  # new contact
        new_user_test.add_user()

        user_exists = User.find_user_exist("johndoe")

        self.assertTrue(user_exists)
    
    # def test_user_by_username(self):
    #     '''
    #     test to check if we can find a contact by phone number and display information
    #     '''

    #     self.new_user.save_contact()
    #     test_contact = Contact("Test", "user", "0711223344",
    #                            "test@user.com")  # new contact
    #     test_contact.save_contact()

    #     found_contact = Contact.find_by_number("0711223344")

    #     self.assertEqual(found_contact.email, test_contact.email)


if __name__ == '__main__':
    unittest.main()
