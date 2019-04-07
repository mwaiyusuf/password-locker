from pass import passdef create_pass(flname,usname,password,email):
'''
creating a new user 
'''
new_pass = Pass(flname,usname,password,email)
return new_pass
 def save_users(pass):
   ''' 
   function to save pass
   '''
   user.save_pass()
   def del_pass(user): 
     '''
     function to delete a pass
     '''
     pass.delete_pass()
     def find_pass(number):
       '''
       function that finds a usesr by number and rerurns into the use
       '''
       return Pass.find_by_number(password)
       def check_existing_users(number)
       '''
       function that check if a user exists with the number and return either true or false
       '''
       return Pass.user_exist(number)
       def display_users(): 
         '''
         function that returns the saved users
         '''
         return user.display_users() 
         def main(): 
           print("Hello, welcome. \n What is your name?")
           user_name = input()
           print(f"Hey {user_name}.What would you like to do?")
           
           while True:
             list = (
               '''
               1.create new account
               2.display the accounts
               3.search for account
               4.exist pass_locker
               '''
             )
             print(list)
             print("")
