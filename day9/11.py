class Payment:
    def process_payment(self, amount):
        print("Processing payment of", amount)

class CreditCard(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "done using Credit Card")

class UPI(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "done using UPI")

class NetBanking(Payment):
    def process_payment(self, amount):
        print("payment of", amount, "done using Net Banking")

payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

amount = 1000

for p in payments:
    p.process_payment(amount)
    
