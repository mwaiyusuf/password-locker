import unittest # Importing the unittest module
import pyperclip #importing a module
from pass import Pass # Importing the pass class

class TestPass(unittest.TestCase):

    '''
    Test class that defines test cases for the pass class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_pass = Pass("James","Muriuki","0712345678","james@ms.com") # create pass object
 def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
         self.assertEqual(self.new_pass.full_name,"James")
        self.assertEqual(self.new_pass.user_name,"Muriuki")
        self.assertEqual(self.new_pass.password,"0712345678")
        self.assertEqual(self.new_pass.email,"james@ms.com")
   def test_save_pass(self):
     '''
     test_save_pass test case to test if the user object is saved into the pass list
     '''

if __name__ == '__main__':
    unittest.main()