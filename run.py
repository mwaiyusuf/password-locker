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
       return Pass.pass_exist(number)
       def display_users(): 
         '''
         function that returns the saved users
         '''
         return pass.display_users() 
         def main(): 
           print("Hello, welcome. \n What is your name?")
           pass_name = input()
           print(f"Hey {pass_name}.What would you like to do?")
           
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
        print("Use these short codes : 1 - create a new user, 2 - display users, 3 -find a user, 4 -exit the Password locker ")

        short_code = input().lower()

        if short_code == '1':
            print("New pass")
            print("-"*10)

            print ("First name ....")
            fl_name = input()

            print("Last name ...")
            us_name = input()

            print("Phone number ...")
            password_number = input()

            print("Email address ...")
            e_address = input()

           

            print("confirm password ...")
            password1 = input()
         save_users(create_user(fl_name,us_name,password_number,e_address, )) # create and save new user.
            print ('\n')
            print(f"New User {fl_name} {us_name} created")
            print ('\n')

        elif short_code == '2':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for pass in display_users():
                    print(f"{pass.first_name} {pass.us_name} .....{pass.password_number}")

                    print('\n')
                else:
                    print('\n')

                    print('\n')

        elif short_code == '3':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_users(search_number):
                search_pass = find_pass(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)
                 print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "4":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()