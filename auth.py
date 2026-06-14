from datetime import datetime

class Authentication:
    def __init__(self):
        self.accounts = [
            {'First_Name': 'Akshay Tyagi',   'card': 954495846293, 'pin': 9035, 'amount': 1000, 'transactions': []},
            {'First_Name': 'Ravi Sharma',    'card': 226054988336, 'pin': 1234, 'amount': 2500, 'transactions': []},
            {'First_Name': 'Priya Mehta',    'card': 334521876540, 'pin': 4567, 'amount': 750,  'transactions': []},
            {'First_Name': 'Amit Verma',     'card': 445698123478, 'pin': 2890, 'amount': 5000, 'transactions': []},
            {'First_Name': 'Sneha Patel',    'card': 556781234590, 'pin': 3721, 'amount': 3200, 'transactions': []},
            {'First_Name': 'Rahul Gupta',    'card': 667894325601, 'pin': 6543, 'amount': 800,  'transactions': []},
            {'First_Name': 'Anjali Singh',   'card': 778906541238, 'pin': 8910, 'amount': 4500, 'transactions': []},
            {'First_Name': 'Vikram Yadav',   'card': 889012345670, 'pin': 1122, 'amount': 1500, 'transactions': []},
            {'First_Name': 'Pooja Joshi',    'card': 990123456781, 'pin': 3344, 'amount': 2200, 'transactions': []},
            {'First_Name': 'Suresh Kumar',   'card': 101234567892, 'pin': 5566, 'amount': 600,  'transactions': []},
            {'First_Name': 'Neha Agarwal',   'card': 112345678903, 'pin': 7788, 'amount': 9000, 'transactions': []},
            {'First_Name': 'Karan Malhotra', 'card': 223456789014, 'pin': 9900, 'amount': 3750, 'transactions': []},
            {'First_Name': 'Deepika Nair',   'card': 334567890125, 'pin': 2233, 'amount': 1800, 'transactions': []},
            {'First_Name': 'Arjun Chopra',   'card': 445678901236, 'pin': 4455, 'amount': 7200, 'transactions': []},
            {'First_Name': 'Meera Iyer',     'card': 556789012347, 'pin': 6677, 'amount': 950,  'transactions': []},
            {'First_Name': 'Rohit Bhatia',   'card': 667890123458, 'pin': 8899, 'amount': 4100, 'transactions': []},
            {'First_Name': 'Kavita Pillai',  'card': 778901234569, 'pin': 1357, 'amount': 2900, 'transactions': []},
            {'First_Name': 'Nikhil Saxena',  'card': 889012345670, 'pin': 2468, 'amount': 5500, 'transactions': []},
            {'First_Name': 'Divya Reddy',    'card': 990123456781, 'pin': 1470, 'amount': 3300, 'transactions': []},
            {'First_Name': 'Manish Tiwari',  'card': 101234567892, 'pin': 2580, 'amount': 8000, 'transactions': []},
        ]
        self.card_number = None
        self.card_pin = None
        self.current_account = None
        self.authenticate()

    def _get_card_number(self):
        try:
            self.card_number = int(input("Please enter your card number: "))
        except ValueError:
            print("Invalid input. Card number must be numeric.")
            exit()

    def _get_card_pin(self):
        try:
            self.card_pin = int(input("Please enter your PIN: "))
        except ValueError:
            print("Invalid input. PIN must be numeric.")
            exit()

    def authenticate(self):
        for attempt in range(3):
            self._get_card_number()
            self._get_card_pin()

            for acc in self.accounts:
                if acc['card'] == self.card_number and acc['pin'] == self.card_pin:
                    self.current_account = acc
                    print(f"\nWelcome, {acc['First_Name']}!")
                    return

            remaining = 2 - attempt
            if remaining > 0:
                print(f"Invalid credentials. {remaining} attempt(s) left.\n")

        print("\nCard blocked due to multiple failed attempts.")

    def _add_transaction(self, txn_type, amount):  # ✅ defined once here
        txn = {
            'type': txn_type,
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.current_account['transactions'].append(txn)

    def show(self):
        print(f"\n--- Account Details ---")
        print(f"Name   : {self.current_account['First_Name']}")
        print(f"Card   : **** **** {str(self.current_account['card'])[-4:]}")
        print(f"Balance: Rs. {self.current_account['amount']}")
        print("-----------------------")