import InsufficientBalanceException
import InvalidAmountEntered
import InvalidBankDetails

class BankAccount:

    bank_name = "ABC Bank"
    min_balance = 1000

    def __init__(self, acct_no, cust_name, acct_type, bal):
        self.account_number = acct_no
        self.customer_name = cust_name
        self.account_type = acct_type
        self.balance = int(bal)

    def display_acct_details(self):
        print("Cutomer account details:")
        print("Bank Name:", BankAccount.bank_name)
        print("Account Number: ", self.account_number)
        print("Customer Name: ", self.customer_name)
        print("Account Type: ", self.account_type)
        print("Balance: ",self.balance)

    def validate_acct_details(self):
        if len(self.account_number) == 10:
            if self.account_number.isdigit():
                if self.account_type in ("Savings Account", "Current Account"):
                    print("Account details validated succesfully...")
                    self.perform_banking_operation()
                    print("----------------------------------------------")
                else:
                    raise InvalidBankDetails("Invalid Bank Details Entered. Please enter valid account type...")
            else:
                raise InvalidBankDetails("Invalid Bank Details Entered. Please enter 10-digits account number...")
        else:
            raise InvalidBankDetails("Invalid Bank Details Entered. Please enter 10-digits account number...")

    def perform_banking_operation(self):
        option = input("Select 1 Option: \n 1. Deposit Amount \n 2. Withdraw Amount")
        match (option):
            case '1':
                dept_amt = input("Enter the amount to be deposited: ")
                self.deposit_money(int(dept_amt))
            case '2':
                wd_amt = input("Enter the amount to be withdraw: ")
                self.withdraw_money(int(wd_amt))
            case _:
                print("Enter correct option...")

    def deposit_money(self, deposit_amt):
        if deposit_amt > 0:
            self.balance += deposit_amt
            print("Amount deposited successfully...")
            self.display_acct_details()
        else:
            raise InvalidAmountEntered("Invalid Amount is Entered")

    def withdraw_money(self, withdraw_amt):
        if withdraw_amt <= 0 :
            raise InvalidAmountEntered("Invalid Amount is Entered")

        if self.balance - withdraw_amt < BankAccount.min_balance:
            raise InsufficientBalanceException("Insufficient Balance: Cannot Withdraw as Minimum balance required Rs. 1000")

        self.balance -= withdraw_amt
        print("Amount withdrawed successfully...")
        self.display_acct_details()

b1 = BankAccount("1234567890","Harsha","Savings Account", 10000)
b1.validate_acct_details()

b2 = BankAccount("1234556620","Ram","Savings Account", 15000)
b2.validate_acct_details()

b3 = BankAccount("1234556620","Radha","Current Account", 20000)
b3.validate_acct_details()


