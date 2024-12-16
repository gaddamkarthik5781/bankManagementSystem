class Account:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.username = ""
        self.gender = ""
        self.phone = 0
        self.accountno = 0
        self.password = ""
        self.balance = 0.0

class Bank:
    accountnocounter = 100

    def __init__(self):
        self.acc = Account()

    def accountgenerate(self):
        Bank.accountnocounter += 1
        return Bank.accountnocounter

    def accountcreate(self):
        self.acc.accountno = self.accountgenerate()
        self.acc.name = input("Enter the name: ").strip()
        self.acc.age = int(input("Enter the age: "))
        self.acc.gender = input("Enter the Gender: ")
        self.acc.phone = int(input("Enter your Phone no: "))
        self.acc.username = input("Enter Username: ")
        self.acc.password = input("Enter your Password: ")

        with open("accounts.txt", "a") as outFile:
            outFile.write(f"{self.acc.accountno},{self.acc.name},{self.acc.age},"
                         f"{self.acc.gender},{self.acc.phone},{self.acc.username},"
                         f"{self.acc.password},{self.acc.balance}\n")

        print(f"Account created successfully! Your account number is: {self.acc.accountno}")

    def login(self):
        entered_acc_no = int(input("Enter your Account Number: "))
        entered_password = input("Enter your Password: ")

        try:
            with open("accounts.txt", "r") as inFile:
                for line in inFile:
                    account_data = line.strip().split(',')
                    if int(account_data[0]) == entered_acc_no and account_data[6] == entered_password:
                        print(f"Login successful! Welcome, {account_data[1]}!")
                        return True
                print("Invalid Account Number or Password!")
                return False
        except FileNotFoundError:
            print("Error opening file for reading!")
            return False

    def deposit(self):
        accountno = int(input("Enter the Account No: "))
        amount = float(input("Enter the Amount you want to deposit: "))

        try:
            with open("accounts.txt", "r") as inFile:
                lines = inFile.readlines()

            found = False
            with open("temp.txt", "w") as tempFile:
                for line in lines:
                    account_data = line.strip().split(',')
                    if int(account_data[0]) == accountno:
                        found = True
                        new_balance = float(account_data[7]) + amount
                        account_data[7] = str(new_balance)
                        print(f"Deposit successful! New Balance: {new_balance}")
                    tempFile.write(','.join(account_data) + '\n')

            import os
            os.remove("accounts.txt")
            os.rename("temp.txt", "accounts.txt")

            if not found:
                print("Account not found!")
        except FileNotFoundError:
            print("Error accessing file!")

    def withdraw(self):
        accountno = int(input("Enter the Account No: "))

        try:
            with open("accounts.txt", "r") as inFile:
                lines = inFile.readlines()

            found = False
            with open("temp.txt", "w") as tempFile:
                for line in lines:
                    account_data = line.strip().split(',')
                    if int(account_data[0]) == accountno:
                        found = True
                        current_balance = float(account_data[7])
                        print(f"Balance is : {current_balance}")
                        amount = float(input("Enter the Amount you want to Withdraw: "))
                        
                        if current_balance >= amount:
                            new_balance = current_balance - amount
                            account_data[7] = str(new_balance)
                            print(f"Withdraw successful! New Balance: {new_balance}")
                        else:
                            print("Insufficient balance!")
                    tempFile.write(','.join(account_data) + '\n')

            import os
            os.remove("accounts.txt")
            os.rename("temp.txt", "accounts.txt")

            if not found:
                print("Account not found!")
        except FileNotFoundError:
            print("Error accessing file!")

    def readAccountsFromFile(self):
        try:
            with open("accounts.txt", "r") as inFile:
                for line in inFile:
                    account_data = line.strip().split(',')
                    print(f"Account Number: {account_data[0]}")
                    print(f"Name: {account_data[1]}")
                    print(f"Age: {account_data[2]}")
                    print(f"Gender: {account_data[3]}")
                    print(f"Phone: {account_data[4]}")
                    print(f"Username: {account_data[5]}")
                    print(f"Balance: {account_data[7]}")
                    print("------------------------")
        except FileNotFoundError:
            print("Error opening file for reading!")

def main():
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. Login\n3. Deposit\n4. View All Accounts\n5. Withdraw\n6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                bank.accountcreate()
            elif choice == 2:
                bank.login()
            elif choice == 3:
                bank.deposit()
            elif choice == 4:
                bank.readAccountsFromFile()
            elif choice == 5:
                bank.withdraw()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Try again.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
