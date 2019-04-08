import pyperclip

class User:
  '''
  Class that create new instances of accounts
  '''
  user_list = [] #an empty list
   
  def __init__(self,account_name,user_name,password,number):
    
    self.account_name = account_name
    self.user_name = user_name
    self.password = password
    self.number = number

  def save_user_credentials(self): 
    '''
    save_pass method saves user object inot pass_list
    '''
    User.user_list.append(self)

  def delete_user_credentials(self):
    '''
    delete_pass method deletes a saved user from the pass_list
    '''
    User.user_user.remove(self)

  @classmethod
  def find_by_number(cls,number):
    '''
    method that takes a number and returns a user that matches the number
    
    Args:
    number : phone number to search for 
    Returns : 
    user that matches the number.
    '''
    for user_account in cls.user_list:
      if user_account.number == number:
        return user_account

  @classmethod
  def user_exist(cls,number):
    '''
    method that checks if the user exist in the list
    Args:
    number: phone number to search if it exists
    Returns :
    Boolean" True or false depending if the user exists
    ''' 
    for user_account in cls.user_list:
       if user_account.number == number:
            return True          

    return False 

  @classmethod 
  def display_users(cls):
    '''
    method that returns the user list
    '''
    return cls.user_list

  # @classmethod 
  # def copy_emails(cls,number):
  #   pass_found = Pass.find_by_number(number)
  #   pyperclip.copy(user_found.email)


class Loc_user:
  '''
  Class that generates new instances of users of the application
  '''
  user_loc_list = [] #an empty list
   
  def __init__(self,name,username,password):
    
    self.name = name
    self.username = username
    self.password = password
    
  def save_loc_user(self):
    '''
    adding new users
    '''
    Loc_user.user_loc_list.append(self)
    
