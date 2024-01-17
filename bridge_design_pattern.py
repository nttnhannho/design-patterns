from abc import ABC, abstractmethod


class PaymentProcess(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class VisaPaymentProcess(PaymentProcess):
    def __init__(self, card_number, expired_date, cvv):
        self.card_number = card_number
        self.expired_date = expired_date
        self.cvv = cvv

    def pay(self, amount):
        print(f'Paying {amount} USD with Visa card {self.card_number}')


class MomoPaymentProcess(PaymentProcess):
    def __init__(self, phone):
        self.phone = phone

    def pay(self, amount):
        print(f'Paying {amount} VND with Momo {self.phone}')


class MemberRegistration:
    def __init__(self, payment_process):
        self.cost = 100
        self.payment_process = payment_process

    def register(self):
        self.payment_process.pay(self.cost)
        print('Registered!!!')


def main():
    visa_payment = VisaPaymentProcess('123.456', '12/25', '888')
    membership = MemberRegistration(visa_payment)
    membership.register()

    momo_payment = MomoPaymentProcess('0909333222')
    membership = MemberRegistration(momo_payment)
    membership.register()


if __name__ == '__main__':
    main()
