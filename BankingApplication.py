class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount, depositor_name=None):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            self.balance += amount
            # Use the depositor's name if provided, otherwise, use the account holder's name
            depositor_name = depositor_name or self.account_holder
            print(f"{depositor_name} deposited {amount}. New balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Deposit operation completed.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Withdrawal operation completed.")

    def check_balance(self):
        try:
            if self.balance < 0:
                raise ValueError("Negative balance detected.")
            print(f"Current balance of {self.account_holder}: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Balance check completed.")

    def transfer(self, amount, recipient):
        try:
            if amount <= 0:
                raise ValueError("Transfer amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient funds for transfer.")
            self.balance -= amount
            recipient.balance += amount
            print(f"{self.account_holder} transferred {amount} to {recipient.account_holder}. Your new balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Transfer operation completed.")

def main():
    account1 = BankAccount("Abc", 1000)
    account2 = BankAccount("Xyz", 500)

    while True:
        print("\nWelcome to the Banking Application")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")
       
        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                depositor_name = input("Enter the depositor's name: ")
                amount = float(input("Enter the amount to deposit: "))
                account1.deposit(amount, depositor_name)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                account1.withdraw(amount)
            elif choice == 3:
                account1.check_balance()
            elif choice == 4:
                amount = float(input("Enter the amount to transfer: "))
                account1.transfer(amount, account2)
            elif choice == 5:
                print("Exiting banking application.")
                break
            else:
                print("Invalid choice, please select a valid option (1-5).")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print("Operation was successful.")

if __name__ == "__main__":
    main()
