# 🏧 Python ATM Simulator

A command-line ATM simulation built using Python OOP concepts like inheritance, encapsulation, and exception handling.

---

## 📁 Project Structure

```
atm_project/
├── auth.py         # Authentication class (base class)
├── withdrawal.py   # Withdrawal class
├── deposit.py      # Deposit class
├── atm.py          # ATM menu & entry point
└── README.md
```

---

## ⚙️ Features

- ✅ Card & PIN authentication with 3 attempts
- ✅ Card gets blocked after 3 failed attempts
- ✅ Withdraw money with balance check
- ✅ Deposit money
- ✅ View account details (card number masked)
- ✅ Mini statement (last 5 transactions with date & time)
- ✅ Input validation with try/except
- ✅ Transaction history using inheritance

---

## 🚀 How to Run

```bash
python atm.py
```

---

## 🧪 Sample Credentials

| Name          | Card Number   | PIN  | Balance  |
|---------------|---------------|------|----------|
| Akshay Tyagi  | 954495846293  | 9035 | Rs. 1000 |
| Ravi Sharma   | 226054988336  | 1234 | Rs. 2500 |
| Priya Mehta   | 334521876540  | 4567 | Rs. 750  |

---

## 🧠 OOP Concepts Used

| Concept         | Where Used                                      |
|-----------------|-------------------------------------------------|
| Class           | Authentication, Withdrawal, Deposit, ATM        |
| Inheritance     | Withdrawal and Deposit inherit Authentication   |
| Encapsulation   | Private methods like `_add_transaction()`       |
| Exception       | try/except on all user inputs                   |

---

## 📌 Sample Output

```
===================================
       Welcome to Python ATM
===================================
Please enter your card number: 954495846293
Please enter your PIN: 9035

Welcome, Akshay Tyagi!

--- Main Menu ---
1. Withdraw
2. Deposit
3. Show Details
4. Mini Statement
5. Exit
```

---

## 👨‍💻 Author

**Akshay Tyagi**  
Python Developer