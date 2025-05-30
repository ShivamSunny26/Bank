class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ${amount:.2f} into account {self.account_number}.')
        print(f'New Balance: ${self.balance:.2f}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_numeber}")
            print(f'New Balance: ${self.amount:.2f}')
    
    def get_balance(self):
        return self.balance
    
    
class Bank:
    def __init__(self):
        self.accounts = {}

    def load_accounts(self, cursor):
        cursor.execute("SELECT account_number, account_holder, balance FROM accounts")
        for (account_number, account_holder, balance) in cursor:
            self.accounts[account_number] = BankAccount(account_number, account_holder, float(balance))

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if account_number in self.accounts:
            return "Accounts already exists"
        else:
            new_account = BankAccount(account_number, account_holder, initial_balance)
            self.accounts[account_number] = new_account
            return "Account created successfully"
    def get_account(self, account_nnumber):
        return self.accounts.get(account_nnumber)
    def list_accounts(self):
        return [(account_number, account.account_holder, account.balance) for account_number ,account in self.accounts.items()]    
    