class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account number: {self._account_number}, balance: {self._balance}"


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        interest_amount = self._balance * self.interest
        self._balance += interest_amount

    def __str__(self):
        return f"Savings Account number: {self._account_number}, balance: {self._balance}, interest: {self.interest}"


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"Current Account number: {self._account_number}, balance: {self._balance}, overdraft limit: {self.overdraft_limit}"


class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def open_account(self, account_number):
        new_account = Account.create_account(account_number)
        self.add_account(new_account)
        print(f"Account {new_account.get_account_number()} opened.")

    def pay_dividends(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)
        print(f"Dividends paid to all accounts: {dividend_amount}")

    def update_account(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
                print("Interest added to account.")

            if isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print("Letter sent to account. Overdraft exceeded!")

    def close_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed.")
                return
        print(f"Account {account_number} not found.")

    def __str__(self):
        account_details = "\n".join(str(account) for account in self.accounts)
        return f"Bank's Accounts:\n{account_details}"


# Creating an instance of the Bank class to manage accounts
bank = Bank()

# Create different types of accounts
general_account = Account(100.0, "12345")
savings_account = SavingsAccount(1000.0, "6789", 0.02)
current_account = CurrentAccount(-2000.0, "76543", 500.00)

# Add accounts to the bank
bank.add_account(general_account)
bank.add_account(savings_account)
bank.add_account(current_account)

# print("Before update:")
# print(bank)

# # Update the bank's accounts
# bank.update_acoount()

# print("After update:")
# print(bank)

# # Pay dividends to all accounts
# bank.pay_dividends(50.00)

# print("After paying dividends:")
# print(bank)

# # Close an account
# bank.close_account("6789")

# print("After closing account:")
# print(bank)

# Open an account
bank.open_account("09876")
print(bank)
