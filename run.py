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
