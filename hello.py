class Customer:
    def __init__(self, name, password):
        import random
        self.name = name
        self.password = password
        self.account_number = random.randint(100000, 999999)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

    def transfer(self, amount, recipient_account_number, customers):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            for customer in customers:
                if customer.account_number == recipient_account_number:
                    customer.balance += amount
                    self.balance -= amount
                    print(f"Transfer successful. New balance: {self.balance}")
                    return
            print("Recipient account not found.")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

class Admin:
    def __init__(self):
        self.customers = []

    def register_customer(self, name, password):
        customer = Customer(name, password)
        self.customers.append(customer)
        print(f"Customer registered successfully. Account number: {customer.account_number}")

    def get_total_balance(self):
        total_balance = sum(customer.balance for customer in self.customers)
        print(f"Total balance: {total_balance}")

    def get_customer_list(self):
        for customer in self.customers:
            print(f"Name: {customer.name}, Account Number: {customer.account_number}, Balance: {customer.balance}")

    def admin_transfer(self, amount, sender_account_number, recipient_account_number):
        for customer in self.customers:
            if customer.account_number == sender_account_number:
                sender_customer = customer
            elif customer.account_number == recipient_account_number:
                recipient_customer = customer
        if sender_customer and recipient_customer:
            if amount > sender_customer.balance:
                print("Insufficient balance.")
            else:
                sender_customer.balance -= amount
                recipient_customer.balance += amount
                print(f"Transfer successful. Sender balance: {sender_customer.balance}, Recipient balance: {recipient_customer.balance}")
        else:
            print("Account not found.")

def main():
    admin = Admin()

    while True:
        print("1. Register")
        print("2. Customer Login")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")

            password = input("Enter your password: ")
            admin.register_customer(name, password)

        elif choice == "2":
            account_number = int(input("Enter your account number: "))

            password = input("Enter your password: ")
            for customer in admin.customers:
                if customer.account_number == account_number and customer.password == password:
                    while True:
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Transfer")
                        print("4. Check Balance")
                        print("5. Change Password")
                        print("6. Logout")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            amount = float(input("Enter amount to deposit: "))
                            customer.deposit(amount)
                        elif choice == "2":
                            amount = float(input("Enter amount to withdraw: "))
                            customer.withdraw(amount)
                        elif choice == "3":
                            amount = float(input("Enter amount to transfer: "))
                            recipient_account_number = int(input("Enter recipient's account number: "))
                            customer.transfer(amount, recipient_account_number, admin.customers)
                        elif choice == "4":
                            print(f"Balance: {customer.balance}")
                        elif choice == "5":

                            new_password = input("Enter new password: ")
                            customer.change_password(new_password)
                        elif choice == "6":
                            break
                        else:
                            print("Invalid")





