#!/usr/bin/env python3.6
from user import User # Importing the user class
from user import Loc_user #importing the loc_user class

def create_user_acc(account_name,user_name,number,password):
  '''
  creating a new user 
  '''
  new_user = User(account_name,user_name,number,password)
  return new_user 

def save_users_credentials(user):
  ''' 
  function to save user credentials
  '''
  user.save_user_credentials()

def del_user_credentials(user): 
  '''
  function to delete a user
  '''
  user.delete_user_credentials()

def find_user_credentials(number):
  '''
  function that finds a user by number and rerurns into the user
  '''
  return User.find_by_number(number)

def check_existing_accounts(number):
  '''
  function that check if a user exists with the number and return either true or false
  '''
  return User.user_exist(number)

def display_users(): 
  '''
  function that returns the saved users accounts
  '''
  return User.display_users() 

def create_loc_account(fname,loc_username,loc_password):
  '''
  Function to create loc account
  '''
  new_loc_user = Loc_user(fname,loc_username,loc_password)
  return new_loc_user

def save_loc_user(loc_user):
  '''
  function to save
  '''
  loc_user.save_loc_user()

def main(): 
  print("Hello, welcome. \n What is your name?")
  print("\n")
  name = input("Enter name:")
  user_name = input("Create a username: ")
  password = input("Type password: ")
  print(f"Hey {user_name}.What would you like to do?")
           
  while True:

    save_loc_user(create_loc_account(name,user_name,password))
  
    print("Use these short codes : 1 - create a new user-account, 2 - display user-accounts, 3 -find a user, 4 -exit the Password locker ")

    short_code = input().lower()

    if short_code == '1':
        print("New account")
        print("-"*10)

        print ("Account ....")
        account_name = input()

        print("User-name ...")
        user_name = input()

        print("Phone number ...")
        number = input()       

        print("Password ...")
        password = input()

        save_users_credentials(create_user_acc(account_name,user_name,number,password))# Add and save new user credentials account
        print('\n')
        print(f"Your {account_name} credentials has been added.")
         
    elif short_code == '2':

      if display_users():
          print("Here is a list of all your users")
          print('\n')

          for user in display_users():
              print(f"{user.account_name} {user.user_name}  {user.number} .....{user.password}")

              print('\n')
      else:
          print('This user-account details cannot be found!')
          print('\n')

    elif short_code == '3':

        print("Enter the number you want to search for")

        search_number = input()
        if find_user_credentials(search_number):
            search_user = find_user(search_number)
            print(f"{search_user.account_name} {search_user.user_name}")
            print('-' * 20)
            print(f"Password.......{search_user.password}")
           
        else:
            print("The user credentials  does not exist")

    elif short_code == "4":
        print("Bye .......")
        break
    else:
        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
  main()