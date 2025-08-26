users = {
    "MR74": {
        "user_name": "Mohan Roy",
        "phone_no": 96885455263,
        "account_no": 968574,
        "account_pin": 2363,
        "account_history": {
            "withdraw_history": [],
            "diposit_history": []
        },
        "account_balance": 250000
    },
    "HP47": {
        "user_name": "Hari Patel",
        "phone_no": 5896856985,
        "account_no": 568547,
        "account_pin": 4658,
        "account_history": {
            "withdraw_history": [],
            "diposit_history": []
        },
        "account_balance": 150000
    },
    "RS12": {
        "user_name": "Raju Shah",
        "phone_no": 4585965856,
        "account_no": 325412,
        "account_pin": 2552,
        "account_history": {
            "withdraw_history": [],
            "diposit_history": []
        },
        "account_balance": 100000
    },
    "RS90": {
        "user_name": "Rita Soni",
        "phone_no": 3256545566,
        "account_no": 568890,
        "account_pin": 4444,
        "account_history": {
            "withdraw_history": [],
            "diposit_history": []
        },
        "account_balance": 500000
    },
    "SP52": {
        "user_name": "Siya Patel",
        "phone_no": 8899665577,
        "account_no": 663252,
        "account_pin": 4224,
        "account_history": {
            "withdraw_history": [],
            "diposit_history": []
        },
        "account_balance": 550000
    }
}

options = """ 
1. Withdraw Money
2. Deposit Money
3. Withdraw History
4. Deposit History
5. Available Balance
6. Show Account Details
7. Exit
"""

active_user = ""
amt = 0

transSuccess = "Transaction Successful :)\nThank you for banking."
transFailure = "Transaction Failed ):\nThank you for banking."


# Utils 

def authUser(uid, upin):
    user = users.get(uid)
    # print(user)
    if not user:
        # print("User does not exist.")
        return False
    else:
        opin = user.get("account_pin")
        if (upin == opin):
            # global active_user
            # active_user = user
            print("User logged in.")
        else:
            print("User login failed.")
        return True
    
def withdrawMoney(user_id):
    global withdraw_history
    amt = int(input("Enter amount to withdraw: "))
    user = users.get(user_id)
    user_available_balance = user.get("account_balance")
    # if active_user:
    if amt <= user_available_balance:
        if amt >= 500:
            if amt % 500 == 0:
                print(f"{amt} withdrawed.")
                user_available_balance = user_available_balance - amt
                print(f"available balance: {user_available_balance}")
                ac_history= user.get("account_history")
                withdraw_history = ac_history.get("withdraw_history")
                withdraw_history.append(amt)
            else:
                print(f"Amount must be in multiple of 500\n{transFailure}")
        else:
            print(f"Amount must be greater than 500\n{transFailure}")
    else:
        print(f"Insufficient Balance: {user_available_balance}\n{transFailure}")

def depositMoney(amt, user_id):
    global deposit_history
    user = users.get(user_id)
    user_available_balance = user.get("account_balance")
    # if active_user:
    if amt >= 5000:
        if amt % 500 == 0:
            print(f"{amt} deposited.")
            user_available_balance += amt
            ac_history = user.get("account_history")
            deposit_history = ac_history.get("deposit_history")
            deposit_history.append(amt)
        else:
            print(f"Amount must be in multiple of 500\n{transFailure}")
    else:
        print(f"Amount must be greater than 5000\n{transFailure}")

def withdrawHistory():
    global withdraw_history
    print("Withdraw History: ")
    for transaction in withdraw_history:
        print(transaction, end=", ")

def depositHistory():
    global deposit_history
    print("Deposit History: ")
    for transaction in deposit_history:
        print(transaction, end=", ")

def showAccountBalance(user_id):
    user = users.get(user_id)
    account_balance = user.get("account_balance")
    print(f"Available Balance: {account_balance}")

def showBankDetails(user_id):
    user = users.get(user_id)
    print(f"User Name: {user.get("user_name")}")
    print(f"Account Number: {user.get("account_no")}")
    print(f"Phone Number: {user.get("phone_no")}")
    print(f"Available Balance: {user.get("account_balance")}")
# ------------------------------------------------

# user_id = input("Enter your id: ")
# user_pin = int(input("Enter your pin: "))

# auth = authUser(user_id, user_pin)
# print(auth)

# if auth:
#     active_user = user_id
# print(active_user)


if __name__ == "__main__":
    user_id = input("Enter your id: ").upper()
    user_pin = int(input("Enter your pin: "))

    if(authUser(user_id, user_pin)):
        print(options)
        opt = int(input("Select Option: "))
        if(opt == 1):
            withdrawMoney(user_id)