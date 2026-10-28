class Customer:
    def __init__(self, cid, cname, acc_no, balance):
        self.cid = cid
        self.cname = cname
        self.acc_no = acc_no
        self.balance = balance
        self.credit_card = []

    def transfer_funds(self, beneficiary_cust_object, amount):
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif self.balance >= amount:
            self.balance -= amount
            beneficiary_cust_object.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient balance.")

    def display_info(self):
        print("Customer ID:", self.cid)
        print("Customer Name:", self.cname)
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)

        print("Assigned Cards:")
        if len(self.credit_card) == 0:
            print("No cards assigned.")
        else:
            for card in self.credit_card:
                print("Card Number:", card.card_no)


class Card:
    def __init__(self, card_no, cvv, expiry_date, balance):
        self.card_no = card_no
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.balance = balance

    def display_info(self):
        print("Card Number:", self.card_no)
        print("CVV:", self.cvv)
        print("Expiry Date:", self.expiry_date)
        print("Balance:", self.balance)


customers = []
cards = []

while True:
    print("BANK MANAGEMENT SYSTEM MENU")
    print("1. Create Customer objects")
    print("2. Create Card objects")
    print("3. Transfer funds between customer objects")
    print("4. Assign card objects to customer objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cid = input("Enter Customer ID: ")
        cname = input("Enter Customer Name: ")
        acc_no = input("Enter Account Number: ")
        balance = float(input("Enter Balance: "))

        customer = Customer(cid, cname, acc_no, balance)
        customers.append(customer)

        print("Customer created successfully!")

    elif choice == "2":
        card_no = input("Enter Card Number: ")
        cvv = input("Enter CVV: ")
        expiry_date = input("Enter Expiry Date: ")
        balance = float(input("Enter Card Balance: "))

        card = Card(card_no, cvv, expiry_date, balance)
        cards.append(card)

        print("Card created successfully!")

    elif choice == "3":
        sender_id = input("Enter Sender Customer ID: ")
        receiver_id = input("Enter Receiver Customer ID: ")

        sender = None
        receiver = None

        for customer in customers:
            if customer.cid == sender_id:
                sender = customer
            if customer.cid == receiver_id:
                receiver = customer

        if sender is not None and receiver is not None:
            if sender is receiver:
                print("Cannot transfer to the same customer.")
            else:
                amount = float(input("Enter Amount: "))
                sender.transfer_funds(receiver, amount)
        else:
            print("Customer not found.")

    elif choice == "4":
        cid = input("Enter Customer ID: ")
        card_no = input("Enter Card Number: ")

        customer_found = None
        card_found = None

        for customer in customers:
            if customer.cid == cid:
                customer_found = customer

        for card in cards:
            if card.card_no == card_no:
                card_found = card

        if customer_found is not None and card_found is not None:
            if card_found not in customer_found.credit_card:
                customer_found.credit_card.append(card_found)
                print("Card assigned successfully!")
            else:
                print("Card already assigned.")
        else:
            print("Customer or Card not found.")

    elif choice == "5":
        if len(customers) == 0:
            print("No customers available.")
        else:
            for customer in customers:
                customer.display_info()

    elif choice == "6":
        if len(cards) == 0:
            print("No cards available.")
        else:
            for card in cards:
                card.display_info()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")