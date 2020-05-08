import random
import os

user_choice = input("Do you want to login or close app: ").lower()
if user_choice == "login":
    print("Welcome, we would require a few details")
    username1 = input("Enter username: ")
    password1 = input("Enter password: ")
    file = open("staff.txt", "r")
    for row in file:
        detail = row.split(",")
        username = detail[0]
        password = detail[1]
    if username1 == username and password1 == password:
        print("successful login!")

    else:
        print("Error message, Try again!")

    session = open('user session.txt', 'w')

    print("Do you want to: \n1. Create new bank account\n2. Check Account Details\n3. Logout")
    user_option = int(input("Choose 1, 2, or 3: "))
    if user_option == 1:
     acct_name = input("Account name: ")
     acct_balance = float(input("Opening Balance: "))
     acct_type = input("Account Type: ")
     acct_email = input("Account Email: ")
     print("Account number loading...")
     acct_number = ''.join(map(str, [random.randint(1,9) for a in range(0,10)]))

     print("Your account number is:", acct_number)
     print("Do you want to: \n1. Create new bank account\n2. Check Account Details\n3. Logout")

     customer = open('customer.txt', 'w+')
     customer.write("Account Name: %s \n" % acct_name)
     customer.write("Account Balance: %s \n" % acct_balance)
     customer.write("Account Type: %s \n" % acct_type)
     customer.write("Account Email: %s \n" % acct_email)

    elif user_option == 2:
     int(input("Enter account number: "))
     with open("customer.txt", "r") as file:
        print(file.read())


    elif user_option == 3:
        os.remove("user session.txt")



else:
    print("Thank you for your time, Goodbye!")
