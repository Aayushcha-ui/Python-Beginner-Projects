accounts = {}


def create_account():
    name = input("Enter your name: ")
    account_number = int(input("Enter account number: "))

    if account_number in accounts:
        print("Account already exists")
        return

    accounts[account_number] = {
        "name": name,
        "balance": 0
    }

    print("Account created successfully")


def deposit():
    account_number = int(input("Enter account number: "))

    if account_number not in accounts:
        print("Account not found")
        return

    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter valid amount")
        return

    accounts[account_number]["balance"] += amount

    print("Money deposited")
    print("Balance:", accounts[account_number]["balance"])


def withdraw():
    account_number = int(input("Enter account number: "))

    if account_number not in accounts:
        print("Account not found")
        return

    amount = int(input("Enter withdrawal amount: "))

    if amount > accounts[account_number]["balance"]:
        print("Not enough balance")
        return

    accounts[account_number]["balance"] -= amount

    print("Money withdrawn")
    print("Balance:", accounts[account_number]["balance"])


def check_balance():
    account_number = int(input("Enter account number: "))

    if account_number not in accounts:
        print("Account not found")
        return

    print("Name:", accounts[account_number]["name"])
    print("Balance:", accounts[account_number]["balance"])


def main():

    while True:

        print("\n===== BANK SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Wrong choice")


main()