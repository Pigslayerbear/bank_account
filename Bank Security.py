import hashlib
import os.path
accounts = {}
salts = []

#-------------------------------------------------------------------------------------------

def has_num(password):
        numbers = "1 2 3 4 5 6 7 8 9 0".split(" ")
        for character in password:
                if character in numbers:
                        return True
        return False


#-------------------------------------------------------------------------------------------

def has_letter(password):
        alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
        for character in password:
                if character in alphabet:
                        return True
        return False

#-------------------------------------------------------------------------------------------

def on_rainbow_table(password):
        f = open("top10,000password.txt" , 'r')

        if password in f:
                table_prone = input("Your password in prone to rianbow table hacking. Would you like to continue using this password? 'Yes' or 'No' ")
                
                if table_prone == 'Yes' or table_prone == 'yes':
                        password = input("Please re-enter your password. ")
                        
                if table_prone == 'No' or table_prone == 'no':
                        password = input("Please enter a new password. ")
                        
        else:
                print("Your password is not contained in the top 10,000 passwords. Good For You!")
        f.close()
        



#-------------------------------------------------------------------------------------------

def salt_password(password):
        indexA =  ord('a')
        password = password.lower()
        last_letter = password[-1]
        
        if not last_letter.isalnum():
                index = 0
                
        elif last_letter.isnumeric():
                index = int(last_letter)
                
        else:
                indexL = ord(last_letter)
                index = indexL - indexA
                
        salt = salts[index]
        return salt
        
#-------------------------------------------------------------------------------------------

def get_salts():

        f = open("salt.txt", "r")

        
        for line in f:
                salts.append(line.strip("\n"))

        
        
#-------------------------------------------------------------------------------------------

def read_file():
        if not os.path.isfile("accounts.txt"):
                return
        f = open("accounts.txt", "r")

        for line in f:
                words = line.split(" ")
                words.pop()
                username = words[0]
                password = words[1]
                PIN = words[2]
                balance = int(words[3])
                info_name = words[4]
                info_adress = words[5]
                info_phoneNumber = words[6]
                info_email = words[7]
                accounts.update({username : [password, PIN, balance, info_name, info_adress, info_phoneNumber, info_email]})
        f.close()

#-------------------------------------------------------------------------------------------

def write_file():
        f = open("accounts.txt", "w")
        for username in accounts:
                f.write(username + " ")
                info = accounts[username]
                for item in info:
                        f.write(str(item) + " " )
                f.write("\n")
        f.close()
        
#-------------------------------------------------------------------------------------------

def hasher(password):
        b = bytes(password, 'utf-8')
        m = hashlib.sha256(b)
        m = m.hexdigest()
        return m

#-------------------------------------------------------------------------------------------

def withdrawl(username):
        transfer_option = input("Please enter your PIN number ")
        
        if transfer_option == accounts[username][1]:
                cash_withdrawl = int(input("How much money would you like to withdrawl? $"))
                
                if cash_withdrawl < accounts[username][2]:
                        accounts[username][2] -= cash_withdrawl
                        print("Cash Withdrawn. You now have $" , accounts[username][2])
                else:
                        print("Insufficient Funds!")
        else:
                print("Incorrect PIN number")
                        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def transfer():
        transfer_option = input("Please enter your PIN number ")
        transfer_name = accounts[username]
        if transfer_option == accounts[username][1]:
                transfer_name = input("Who's acount wold you like to send money to? ")
                
                if not accounts.get(transfer_name):
                        print(transfer_name ,"is not a valid account name" )
                        return
                
                transfer_funds = int(input("How much money would you like to transfer? $"))
                        
                if transfer_funds < accounts[username][2]:
                        accounts[username][2] -= transfer_funds
                        accounts[transfer_name][2] += transfer_funds
                        print("Transfer Complete!")
                                
                else:
                        print("Insufficient Funds! Transfer Incomplete")
        
        else:
                print("Incorrect Pin")
                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
        
def login():
        print("Logging in")
        username = input("Please enter username " )
        
        if not accounts.get(username):
            print("Please enter a valid username " )
            return
        actual_password = accounts[username][0]
        
        for i in range (0,6):
            password = input("Please enter your password ")
            password = password + salt_password(password)
            password = hasher(password)
            
            if i == 5:
                print("Locked out sucks 2 b u")
                break

            elif password == actual_password:
                print("Welcome, " + username + "!")
                option = input("To access account balance press 'B'. To transfer funds press 'T'. To deposite funds press 'D'. To withdrawl funds press 'W'. To access information press 'I'")
                accountBalance = accounts[username][2]
                
                if option == 'B' or option == 'b':
                        print("Your current account balance is- $" , accountBalance)
                
                elif option == 'T' or option == 't':
                        transfer()

                elif option == 'D' or option == 'd':
                        cash_deposite = int(input("How much money would you like to deposite? $"))
                        
                        if cash_deposite == 666:
                                print("Hello boss, Mr.Satan sir. How's the weather down there?")
                                print("$666,666,666 has been added to your account")
                                accounts[username][2] += 666666666
                                
                        else:
                                accounts[username][2] = cash_deposite
                                print("Cash deposited. You now have $" , accounts[username][2])

                elif option == 'W' or option == 'w':
                        withdrawl(username)

                elif option == 'I' or option == 'i':
                        information = accounts[username][3]
                        print("Name- " , info_name)
                        print("Adress- " , info_adress)
                        print("Phone Nummber- " , info_phoneNumber)
                        print("Email- " , info_email)
                                
                break
            else:
                print("Wrong password- Try again." )
        
                
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

read_file()
get_salts()
salt_password("TAC")
message = input("Enter 'C' to create new bank acount, or 'L' to login. To quit press 'Q' ")

while message != 'Q' and message != 'q':
        
    if message == 'C' or message == 'c':
        
        username = input("Create a username ")
        while accounts.get(username):
                username = input("Username taken- please enter a different username ")

        if username == "":
                username = input("Username invalid- please enter a different username ")

        if username == " ":
                username = input("Username invalid- please enter a different username ")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        password = input("Create a password ")


        f = open("top10,000password.txt" , 'r')
        passlist = []
        
        for line in f:
                passlist.append(line.strip("\n"))
        
        if password in passlist:
                table_prone = input("Your password in prone to rianbow table hacking. Would you like to continue using this password? 'Yes' or 'No' ")
                
                if table_prone == 'Yes' or table_prone == 'yes':
                        password = input("Please re-enter your password. ")
                        
                if table_prone == 'No' or table_prone == 'no':
                        password = input("Please enter a new password. ")
        f.close()
        
        if len(password) < 8:
                too_short = input("Your passwords is unsicure(too short, must be 8 characters). Would You like to continue using this password? 'Yes' or 'No' ")
                
                if too_short == 'Yes' or too_short == 'yes':
                        password = input("Please re-enter your password. ")
                        
                if too_short == 'No' or too_short == 'no':
                        password = input("Please enter a new password. ")


        valid2 = has_num(password)
        if not valid2:
                no_num = input("Your password is unsicure(no numbers). Would you like to continue using this password? 'Yes' or 'No' ")

                if no_num == 'Yes' or no_num == 'yes':
                        password = input("Please re-enter your password. ")

                if no_num == 'No' or no_num == 'no':
                        password = input("Please enter a new password")



        valid = has_letter(password)
        if not valid:
                no_letter = input("Your password is unsicure(no letters). Would you like to continue using this password? 'Yes' or 'No' ")

                if no_letter == 'Yes' or no_letter == 'yes':
                        password = input("Please re-enter your password. ")

                if no_letter == 'No' or no_letter == 'no':
                        password = input("Please enter a new password")


                
        password = password + salt_password(password)
        password = hasher(password)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        PIN = input("Please enter a PIN to secure your info. ")
        
        while len(PIN) != 4:
            PIN = input("PIN must be 4 didgits. Try again. ")
            
        question_1 = input("would You like to add personal information. 'Yes' or 'No'")
        
        if question_1 == 'Yes' or question_1 == 'yes':
                info_name = input("What is your name? ")
                info_adress = input("What is your adress? ")
                info_phoneNumber = int(input("what is your phone number(NO DASHES) "))
                info_email = input("What is your email")
                print("Information inputed")

        if question_1 == "No" or question_1 == 'no':
                info_name = "*"
                info_adress = "*" 
                info_phoneNumber = "*"  
                info_email = "*"
                print("No information inputed")
        
                
        accounts.update({username : [password, PIN, 0, info_name, info_adress, info_phoneNumber, info_email]})
        
    elif message == 'L' or message == 'l':
       login()
       
    else:
        print("Please enter Valid option ")

    message = input("Enter 'C' to create new bank acount, or 'L' to login. To quit press 'Q' ")

write_file()
