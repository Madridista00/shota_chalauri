# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
# class Payment:
#     """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
#     """
#     def process_credit(self, amount):
#         pass

from abc import ABC, abstractmethod

class Pay(ABC):
    def __init__(self, payment_type):
        self.payment_type = payment_type

    @abstractmethod
    def new_amount(self):
        pass

class PayPal(Pay):
    def __init__(self, virtual_money, online_transaction):
        super().__init__("paypal")
        self.virtual_money = virtual_money
        self.online_transaction = online_transaction

    def new_amount(self):
        return self.virtual_money - self.online_transaction

class Payment(Pay):
    def __init__(self, money, transaction):
        super().__init__("cash payment")
        self.money = money
        self.transaction = transaction

    def new_amount(self):
        return self.money - self.transaction

# Factory for creating payment objects
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type, *args):
        if payment_type.lower() == 'paypal':
            return PayPal(*args)
        elif payment_type.lower() == 'cash payment':
            return Payment(*args)
        else:
            raise ValueError("Invalid payment type")

# ========================
paypal1 = PaymentFactory.create_payment('paypal', 100, 20)
print(f"{paypal1.payment_type}")
print(f"New_balance: {paypal1.new_amount()}\n")

payment1 = PaymentFactory.create_payment('cash payment', 100, 20)
print(f"{payment1.payment_type}")
print(f"New_balance: {payment1.new_amount()}\n")