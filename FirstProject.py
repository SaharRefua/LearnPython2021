import json
login_successfully=True
def log_in ():

    user_name=input("Please enter your user name: \n")
    user_password=input("Please enter your user password: \n ")
    if user_name=="Sahar" or user_name=="sahar" and user_password=="Abcd1234"  :
        print("log-in successfully !")
        login_successfully=True
    elif  user_name=="Sahar" or user_name=="sahar" and user_password!="Abcd1234":
        print("wrong password Sahar , please try again ")
        log_in()
    else:
        print("Please try again and enter user name and password ")
        log_in()

def account_status ():
    pass


def Deposit(Deposit_value):
    f = open('data.json')
    data = json.load(f)

    value = data["Balance"]
    value=float(value)+float(Deposit_value)
    f.close()
    print(f"Your Balance in the bank Account is {value}\n")



def account_actions():
    sahar_answer=input("\nPlease let us know what are the action that you what to do in your account:\n 1.Deposit money to your account \n 2.Withdraw money from your account \n 3.Close your account")
    if sahar_answer==1:
        Deposit_value = input("How match money do you what to Deposit in your account?\n")
        Deposit(Deposit_value)
    # elif: sahar_answer == 2:
    #
    #
    # else: sahar_answer == 3:
    else:
        print("Wrong action please try again")


def upload_accout_data():
    f = open('data.json')
    data = json.load(f)
    f.close()
    value=data["Balance"]
    print(f"Your Balance in the bank Account is {value}\n")


print("Welcome to Sahar Bank accout\n")
#log_in()
# if login_successfully==True:
#      upload_accout_data()
account_actions()


