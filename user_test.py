import unittest # Importing the unittest module
import pyperclip #importing a module
from user import User # Importing the user class
from user import Loc_user #importing the loc_user class

class TestPass(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_user = User("Facebook","Muriuki","0712345678","james@ms.com") # create user credentials object
      self.new_loc_user = Loc_user("Jemmila","Jem","moringa")

    def test_init(self): 
      '''
      test_init test case to test if the object is initialized properly
      '''
      self.assertEqual(self.new_user.account_name,"Facebook")
      self.assertEqual(self.new_user.user_name,"Muriuki")
      self.assertEqual(self.new_user.password,"0712345678")
      self.assertEqual(self.new_user.number,"072588645")
      self.assertEqual(self.new_loc_user.name,"Jemmila")
      self.assertEqual(self.new_loc_user.username,"Jem")
      self.assertEqual(self.new_loc_user.password,"moringa")

    def test_save_credentials(self):
      '''
      test_save_user test case to test if the user object is saved into the user list 
      '''
      self.new_user.save_user_credentials()  #saving the new user pass
      self.assertEqual(len(User.user_list),1)

    def tearDown(self):
      '''
      tearDown method that does clean up after each test case has execute
      '''
      User.user_list=[]
      Loc_user.user_loc_list = []

    def test_save_mulitple_user(self):
      '''
      test_save_mulitple_user to check if we can save mulitple user objects to our list
      '''
      self.new_user.save_user_credentials()
      test_user = User("test","user","0732442483","test@pass.com") #new pass user
      test_user.save_user_credentials()
      self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
      '''
      test_delete_user to test if we can get rid off user list
      '''
      self.new_user.save_user_credentials()
      test_user = user("test","pass","07324424856","test@gmail.vom") #new pass
      test_user.save_user_credentials()
      self.assertEqual(len(User.user_list),2)
          
    def test_find+user_by_number(self):
      '''
      test to check if there is a user by phone number and display
      '''
      self.new_user.save_user()
      test_user = user("Test","pass","0799315832","mwaigalo5@pass.com") #new pass
      test_user.save_user()
      found_User = User.find_by_number("0727765213")
      self.assertEqual(found_user.number,test_user.number)

    def test_user_exists(self):
      '''
      test to check if a boolean can be return,when a user be found
      '''
      self.new_user.save_user()
      test_user = user("test","pass","0721817801","mom@pass.com") #new pass
      test_user.save_user()
      user_exists = User.user_exist("0721817801")
      self.assertTrue(user_exist)

    def test_display_all_users(self):
      '''
      method that returns all user saved
      '''
      self.assertEqual(user.display_users(),user.user_list)

    def test_copy_email(self):
      '''
      testing to confirm that we are copying the email address from a found user
      '''
      self.assertEqual(self.new_user.number,pyperclip.paste())

    def test_save_loc_user(self):
      '''
      testing to verify new user has saved
      '''
      self.new_loc_user.save_loc_user()
      self.assertEqual(len(Loc_user.user_loc_list),1)

if __name__ == '__main__':
    unittest.main()