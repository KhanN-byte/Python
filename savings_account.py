class BalanceException(Exception):
    """Raised when an account does not have enough funds."""
    pass


class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = float(initial_amount)
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.")
        print(f"Balance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be greater than 0.")
            return

        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def _check_funds(self, amount):
        if self.balance < amount:
            raise BalanceException(
                f"Account '{self.name}' has insufficient funds: ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self._check_funds(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********")
            print("Beginning transfer... 🚀")

            self._check_funds(amount)
            self.balance -= amount
            account.balance += amount

            print("Transfer complete! ✅")
            self.get_balance()
            account.get_balance()
            print("**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be greater than 0.")
            return

        bonus_amount = amount * 1.05
        self.balance += bonus_amount
        print("\nDeposit complete (+5% reward).")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5.0

    def withdraw(self, amount):
        try:
            total = amount + self.fee
            self._check_funds(total)

            self.balance -= total
            print(f"\nWithdraw complete (includes ${self.fee:.2f} fee).")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
