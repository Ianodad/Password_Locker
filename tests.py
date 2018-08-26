'''
we begin by import unittest and User form user.py
'''
import unittest
from user import User
from credi import Credi


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        set up method
        '''
        self.new_user = User('ian', 'Odhiambo', 'ianodad',
                             '0712724144', 'ianodad@gmail.com', 'Pythoncode1')

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
        new_user_test = User('John', 'Doe', 'johndoe',
                             '0712000000', 'johndoe@gmail.com', 'johndoe254')
        new_user_test.add_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_contact(self):
        ''' 
        This here is the to test is we can remove obbejct from list
        '''
        self.new_user.add_user()
        new_user_test = User('John', 'Doe', 'johndoe',
                             '0712000000', 'johndoe@gmail.com', 'johndoe254')
        new_user_test.add_user()
        self.new_user.delete_user()  # Deleting obeject of the new user
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_exist(self):

        self.new_user.add_user()
        new_user_test = User('John', 'Doe', 'johndoe',
                             '0712000000', 'johndoe@gmail.com', 'johndoe254')
  # new contact
        new_user_test.add_user()

        user_exists = User.find_user_exist("johndoe")

        self.assertTrue(user_exists)

    def test_user_by_username(self):
        '''
        test to check if we can find a user by username
        '''

        self.new_user.add_user()
        new_user_test = User('John', 'Doe', 'johndoe', '0712000000',
                             'johndoe@gmail.com', 'johndoe254')  # new contact
        new_user_test.add_user()

        user_found = User.find_username("johndoe")
        '''
        we set assertEqual to compare the instance of phone number
        '''
        self.assertEqual(user_found.phone_number, new_user_test.phone_number)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_user(), User.user_list)

    # def test_encode_password(self):
    #     '''
    #     method to test enodeing of user pass word
    #     '''
    #     self.new_user.add_user()

    #     new_user_test = User('John', 'Doe', 'johndoe', '0712000000',
    #                          'johndoe@gmail.com', 'johndoe254')
    #     new_user_test.add_user()

    #     encoded = User.encode("johndoe")
    #     self.assertIsNot(encoded.password, new_user_test.password)


class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        set up method test
        '''
        self.new_account = Credi('twitter', 'ianodad', 'rettiwt')

    def test_init(self):
        '''
        intiating test for users
        '''
        self.assertEqual(self.new_account.account, "twitter")
        self.assertEqual(self.new_account.username, "ianodad")
        self.assertEqual(self.new_account.password, "rettiwt")

    def test_add_account(self):
        '''
        test_add account
        '''
        self.new_account.add_account()  # saving the new contact
        self.assertEqual(len(Credi.account_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credi.account_list = []

    def test_save_multiple_users(self):
        '''
        test_save_multiple_account 
        '''
        self.new_account.add_account()
        new_account_test = Credi('Instagram', 'malcom', 'gram')
        new_account_test.add_account()
        self.assertEqual(len(Credi.account_list), 2)

    def test_delete_account(self):
        ''' 
        This here is the to test is we can remove obbejct from list
        '''
        self.new_account.add_account()
        new_account_test = Credi('Instagram', 'malcom', 'gram')
        new_account_test.add_account()
        self.new_account.delete_account()  # Deleting obeject of the new user
        self.assertEqual(len(Credi.account_list), 1)

    def test_find_account_exist(self):

        self.new_account.add_account()
        new_account_test = Credi('Instagram', 'malcom', 'gram')
        new_account_test.add_account()

        account_exists = Credi.find_account_exist("malcom", "gram")

        self.assertTrue(account_exists)

    def test_user_by_username(self):
        '''
        test to check if we can find a user by username
        '''

        self.new_account.add_account()
        new_account_test = Credi('Instagram', 'malcom', 'gram')
        new_account_test.add_account()

        account_exists = Credi.find_account("malcom", 'gram')
        '''
        we set assertEqual to compare the instance of password
        '''
        self.assertEqual(account_exists.account,
                         new_account_test.account)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts
        '''

        self.assertEqual(Credi.display_accounts(), Credi.account_list)


if __name__ == '__main__':
    unittest.main()
