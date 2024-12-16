# Bank Management System

## Overview

The **Bank Management System** is a Python-based console application designed to simulate basic banking functionalities. This system allows users to manage their accounts securely, perform transactions, and view account details. It is implemented with data persistence to retain user information across sessions.

---

## Features

### 1. **Account Creation**
- Users can create a new account by providing their details (e.g., name, age, phone number, etc.).
- Each account is assigned a unique account number automatically.

### 2. **Login**
- Users can log in securely using their account number and password.
- Ensures authorized access to individual accounts.

### 3. **Deposit Money**
- Allows users to deposit funds into their account.
- Updates the balance instantly.

### 4. **Withdraw Money**
- Facilitates withdrawals, ensuring the account has sufficient funds.
- Displays appropriate messages if the balance is insufficient.

### 5. **View All Accounts (Admin Access)**
- Enables administrators to view all user account details.
- Passwords remain hidden for security purposes.

### 6. **Data Persistence**
- All user data is stored in a file (`accounts.txt`).
- Data remains available even after the program is restarted.

---

## Requirements

- Python 3.6 or higher.

---

## How to Run

1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Run the program using the command:
   ```bash
   python bMS_main.py
