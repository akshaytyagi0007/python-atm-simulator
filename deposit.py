from auth import Authentication
class Deposit(Authentication):
    def __init__(self, auth):
        self.accounts = auth.accounts
        self.current_account = auth.current_account

        if self.current_account is None:
            return

        try:
            amount = int(input("Enter amount to deposit: Rs. "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
            return

        self.current_account['amount'] += amount
        self._add_transaction("Deposit", amount)  # ✅ inherited from Authentication
        print(f"Rs. {amount} deposited successfully.")
        print(f"Current balance: Rs. {self.current_account['amount']}")