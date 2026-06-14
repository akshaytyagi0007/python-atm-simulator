from auth import Authentication
from withdrawal import Withdrawal
from deposit import Deposit


class ATM:
    def __init__(self):
        print("=" * 35)
        print("       Welcome to Python ATM")
        print("=" * 35)

        self.auth = Authentication()

        if self.auth.current_account is None:
            return

        while True:
            print("\n--- Main Menu ---")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Details")
            print("4. Mini Statement")
            print("5. Exit")
            print("-----------------")

            choice = input("Select option: ").strip()

            if choice == '1':
                Withdrawal(self.auth)
            elif choice == '2':
                Deposit(self.auth)
            elif choice == '3':
                self.auth.show()
            elif choice == '4':
                self._mini_statement()
            elif choice == '5':
                print("\nThank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please select 1-5.")

    def _mini_statement(self):
        transactions = self.auth.current_account.get('transactions', [])
        if not transactions:
            print("\nNo transactions found.")
            return

        print("\n--- Last 5 Transactions ---")
        for txn in transactions[-5:]:
            print(f"{txn['date']}  |  {txn['type']:<12}  |  Rs. {txn['amount']}")
        print("---------------------------")


ATM()