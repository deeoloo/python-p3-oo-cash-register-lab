#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {
            'title': title,
            'price': price,
            'quantity': quantity
        }

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.last_transaction:
            return
        
        last_price = self.last_transaction['price'] * self.last_transaction['quantity']
        self.total -= last_price
        
        # Remove the items from the items list
        for _ in range(self.last_transaction['quantity']):
            if self.last_transaction['title'] in self.items:
                self.items.remove(self.last_transaction['title'])
        
        # Reset total to 0.0 if all items removed
        if not self.items:
            self.total = 0.0