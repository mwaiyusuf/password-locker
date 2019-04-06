import unittest # Importing the unittest module
import pyperclip #importing a module
from pass import Pass # Importing the pass class

class Testpass(unittest.TestCase):

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
         self.assertEqual(self.new_pass.first_name,"James")
        self.assertEqual(self.new_pass.last_name,"Muriuki")
        self.assertEqual(self.new_pass.phone_number,"0712345678")
        self.assertEqual(self.new_pass.email,"james@ms.com")


if __name__ == '__main__':
    unittest.main()