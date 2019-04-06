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
    self.new_pass.save_pass()  #saving the new user pass
    self.assertEqual(len(Pass.pass_list),1)

    def tearDown(self):
      '''
      tearDown method that does clean up after each test case has execute
      '''
      Pass.pass_list=[]

      def test_save_mulitple_pass(self):
        '''
        test_save_mulitple_pass to check if we can save mulitple pass objects to our list
        '''
        self.new_pass.save_pass()
        test_pass = Pass("test","user","0732442483","test@pass.com") #new pass user
        test_pass.save_pass()
        self.assertEqual(len(Pass.pass_list),2)
if __name__ == '__main__':
    unittest.main()