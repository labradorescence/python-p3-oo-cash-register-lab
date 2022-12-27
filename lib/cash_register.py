#!/usr/bin/env python3
class CashRegister:
      def __init__(self, discount=0):
            self.discount = discount
            self.total = 0
            self.last_transaction = 0
            self.items = []
      
      def add_item(self, item_name, price, quantity=1):
            self.last_transaction = price * quantity
            self.total+=self.last_transaction

            for _ in range(quantity):
                  self.items.append(item_name)

      def apply_discount(self):
          if(self.discount > 0):
            disc_percent = (100 - float(self.discount))/100

            self.total = int(self.total * disc_percent)

            print(f"After the discount, the total comes to ${self.total}.")
          else:
            print("There is no discount to apply.")

      def void_last_transaction(self):
            self.total -= self.last_transaction

new_cash = CashRegister(10)
new_cash.add_item("peach", 10, 2)
new_cash.add_item("eggs", 1.99, 2)
new_cash.add_item("tomato", 1.76, 3)
print(new_cash.total, new_cash.last_transaction, new_cash.items)
new_cash.apply_discount()
print(new_cash.total)
new_cash.void_last_transaction()
print(new_cash.total)
print(new_cash.items)