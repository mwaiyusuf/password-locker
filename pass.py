import pyperclip


class Pass:
  '''
  '''
  pass_list = [] #an empty list
   
  def __init__(self,full_name,user_name,password,email):
    
    self.full_name = full_name
    self.user_name = user_name
    self.password = passwsord
    sel.email = email

    def save_pass(self): 
      '''
      save_pass method saves user object inot pass_list
      '''
      Pass.pass_list.append(self)

      def delete_pass(self):
        '''
        delete_pass method deletes a saved user from the pass_list
        '''
        Pass.pass_list.remove(self)
        @classmethod
        def find_by_number(cls,number):
          '''
          method that takes a number and returns a user that matches the number
          
          Args:
          number : phone number to search for 
          Returns : 
          user that matches the number.
          '''
          for pass in cls.pass_list:
            if pass.password == password:
              rerurn pass
              @classmethod
              def pass_exist(cls,number); 